# Ouvre un menu (clic sur un point), y trouve une entree par son nom et la clique.
# Tout se passe dans UN seul processus : entre deux appels, le menu se referme
# et les positions changent, ce qui fait cliquer a cote — et parfois ailleurs.
# -Sous permet d'aller chercher une entree dans un sous-menu.
param(
  [Parameter(Mandatory=$true)][int]$X,
  [Parameter(Mandatory=$true)][int]$Y,
  [Parameter(Mandatory=$true)][string]$Entree,
  [string]$Sous = "",
  [switch]$Lister,
  [switch]$Fermer
)
Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes, WindowsBase
Add-Type -AssemblyName System.Windows.Forms
Add-Type -TypeDefinition 'using System;using System.Runtime.InteropServices;public class Mn{[DllImport("user32.dll")]public static extern bool SetProcessDPIAware();[DllImport("user32.dll")]public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);[DllImport("user32.dll")]public static extern bool SetCursorPos(int x,int y);[DllImport("user32.dll")]public static extern void mouse_event(uint f,uint dx,uint dy,uint d,UIntPtr e);[DllImport("user32.dll")]public static extern void keybd_event(byte k,byte s,uint f,UIntPtr e);}'
try { [void][Mn]::SetThreadDpiAwarenessContext([IntPtr](-4)) } catch { }
[void][Mn]::SetProcessDPIAware()

function Cliquer($cx, $cy) {
  [void][Mn]::SetCursorPos($cx - 60, $cy); Start-Sleep -Milliseconds 120
  [void][Mn]::SetCursorPos($cx, $cy); Start-Sleep -Milliseconds 250
  [Mn]::mouse_event(2, 0, 0, 0, [UIntPtr]::Zero)
  Start-Sleep -Milliseconds 60
  [Mn]::mouse_event(4, 0, 0, 0, [UIntPtr]::Zero)
}
function Surligne {
  # Quelle entree porte le focus clavier ? C'est la seule facon sure de savoir
  # ou l'on en est : le nombre de fleches a envoyer depend de l'entree deja
  # surlignee a l'ouverture, qui varie.
  $root = [System.Windows.Automation.AutomationElement]::RootElement
  $c = New-Object System.Windows.Automation.AndCondition(
        (New-Object System.Windows.Automation.PropertyCondition(
          [System.Windows.Automation.AutomationElement]::ControlTypeProperty,
          [System.Windows.Automation.ControlType]::MenuItem)),
        (New-Object System.Windows.Automation.PropertyCondition(
          [System.Windows.Automation.AutomationElement]::HasKeyboardFocusProperty, $true)))
  $e = $root.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $c)
  if ($e) { return $e.Current.Name } else { return "" }
}
function ActiverClavier($items, $nom) {
  for ($k = 0; $k -lt 30; $k++) {
    if ((Surligne) -eq $nom) {
      [System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
      Start-Sleep -Milliseconds 800
      return $true
    }
    [System.Windows.Forms.SendKeys]::SendWait("{DOWN}")
    Start-Sleep -Milliseconds 160
  }
  return $false
}
function Activer($item) {
  # Un clic simule n'active pas toujours une entree de menu : le menu attend un
  # survol prealable. L'appel UIA Invoke, lui, declenche l'action directement.
  try {
    $ip = $item.El.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern)
    $ip.Invoke(); return "invoke"
  } catch {
    Cliquer $item.X $item.Y; return "clic"
  }
}
function Entrees {
  # Deux pieges. La barre de menus de l'application est toujours presente dans
  # l'arbre UIA et se melangerait aux entrees du menu ouvert. Et tous les menus
  # ne sont pas de classe #32768 : celui de l'Explorateur ne l'est pas. On
  # enumere donc largement, puis on ne garde que ce qui tombe SOUS le point
  # d'ouverture et sur le meme ecran.
  $root = [System.Windows.Automation.AutomationElement]::RootElement
  $cItem = New-Object System.Windows.Automation.PropertyCondition(
            [System.Windows.Automation.AutomationElement]::ControlTypeProperty,
            [System.Windows.Automation.ControlType]::MenuItem)
  $res = @()
  foreach ($e in $root.FindAll([System.Windows.Automation.TreeScope]::Descendants, $cItem)) {
    $r = $e.Current.BoundingRectangle
    if ($r.Width -le 0) { continue }
    if ($r.Y -lt ($Y + 20)) { continue }
    if ([math]::Abs($r.X - $X) -gt 1200) { continue }
    $res += [pscustomobject]@{ Nom = $e.Current.Name
                               X = [int]($r.X + $r.Width / 2)
                               Y = [int]($r.Y + $r.Height / 2)
                               El = $e }
  }
  return $res
}

Cliquer $X $Y
Start-Sleep -Milliseconds 1300
$items = Entrees
if ($Lister) { $items | ForEach-Object { "{0,-30} ({1},{2})" -f $_.Nom, $_.X, $_.Y }; exit 0 }

$cible = $items | Where-Object { $_.Nom -eq $Entree } | Select-Object -First 1
if (-not $cible) {
  "entrees vues : " + ($items | ForEach-Object { $_.Nom }) -join " / "
  Write-Error "entree '$Entree' introuvable"; exit 1
}
if ($Sous -ne "") {
  # Survol progressif : le sous-menu ne s'ouvre pas sur un saut de curseur.
  for ($i = 1; $i -le 6; $i++) {
    [void][Mn]::SetCursorPos($cible.X - 60 + [int](60 * $i / 6), $cible.Y)
    Start-Sleep -Milliseconds 150
  }
  # On ouvre le sous-menu au clavier : descendre jusqu'a l'entree, puis Droite.
  $vu = $false
  for ($k = 0; $k -lt 30; $k++) {
    if ((Surligne) -eq $Entree) { $vu = $true; break }
    [System.Windows.Forms.SendKeys]::SendWait("{DOWN}")
    Start-Sleep -Milliseconds 160
  }
  if (-not $vu) { Write-Error "'$Entree' jamais surlignee"; exit 1 }
  [System.Windows.Forms.SendKeys]::SendWait("{RIGHT}")
  Start-Sleep -Milliseconds 1500
  $enfants = Entrees | Where-Object { $_.Nom -ne $Entree }
  $fils = $enfants | Where-Object { $_.Nom -eq $Sous } | Select-Object -First 1
  if (-not $fils) {
    "entrees vues : " + (($enfants | ForEach-Object { $_.Nom }) -join " / ")
    Write-Error "sous-entree '$Sous' introuvable"; exit 1
  }
  if (ActiverClavier $enfants $Sous) { "active au clavier : $Entree > $Sous" }
  else { Write-Error "'$Sous' jamais surlignee"; exit 1 }
} else {
  if (ActiverClavier $items $Entree) { "active au clavier : $Entree" }
  else { Write-Error "'$Entree' jamais surlignee"; exit 1 }
}
