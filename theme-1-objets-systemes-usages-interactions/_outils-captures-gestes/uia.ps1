# Boite a outils UI Automation : lister, cliquer, redimensionner, lire.
# Sert quand les coordonnees ecran sont peu fiables (plusieurs ecrans, mise a l'echelle).
param(
  [Parameter(Mandatory=$true)][string]$Window,   # sous-chaine du titre de la fenetre
  [string]$Action = "lister",                    # lister | clic | cocher | resize | rect | texte
  [string]$Name = "",                            # nom de l'element vise
  [string]$Type = "",                            # ControlType : Button, CheckBox, RadioButton, Edit, ...
  [int]$W = 0, [int]$H = 0, [int]$X = 0, [int]$Y = 0,
  [int]$Profondeur = 4
)
Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes, WindowsBase
$root = [System.Windows.Automation.AutomationElement]::RootElement
$cond = New-Object System.Windows.Automation.PropertyCondition(
          [System.Windows.Automation.AutomationElement]::ControlTypeProperty,
          [System.Windows.Automation.ControlType]::Window)
$win = $null
foreach ($cand in $root.FindAll([System.Windows.Automation.TreeScope]::Children, $cond)) {
  if ($cand.Current.Name -like "*$Window*") { $win = $cand; break }
}
if (-not $win) {
  # Les boites de dialogue de LibreOffice ne sont pas filles de la racine :
  # elles sont imbriquees dans la fenetre du document. On redescend.
  foreach ($cand in $root.FindAll([System.Windows.Automation.TreeScope]::Descendants, $cond)) {
    if ($cand.Current.Name -like "*$Window*") { $win = $cand; break }
  }
}
if (-not $win) { Write-Error "fenetre '$Window' introuvable"; exit 1 }

function Trouver($parent, $nom, $type) {
  $conds = @()
  if ($nom -ne "") { $conds += New-Object System.Windows.Automation.PropertyCondition(
      [System.Windows.Automation.AutomationElement]::NameProperty, $nom) }
  if ($type -ne "") { $conds += New-Object System.Windows.Automation.PropertyCondition(
      [System.Windows.Automation.AutomationElement]::ControlTypeProperty,
      [System.Windows.Automation.ControlType]::$type) }
  if ($conds.Count -eq 0) { return $null }
  $c = if ($conds.Count -eq 1) { $conds[0] } else { New-Object System.Windows.Automation.AndCondition($conds) }
  return $parent.FindFirst([System.Windows.Automation.TreeScope]::Descendants, $c)
}

switch ($Action) {
  "lister" {
    $walker = [System.Windows.Automation.TreeWalker]::ControlViewWalker
    function Marcher($el, $niv) {
      if ($niv -gt $Profondeur) { return }
      $e = $walker.GetFirstChild($el)
      while ($e -ne $null) {
        $c = $e.Current
        $r = $c.BoundingRectangle
        "{0}{1} | {2} | ({3},{4}) {5}x{6}" -f ('  ' * $niv), $c.ControlType.ProgrammaticName.Replace('ControlType.',''),
          $c.Name, [int]$r.X, [int]$r.Y, [int]$r.Width, [int]$r.Height
        Marcher $e ($niv + 1)
        $e = $walker.GetNextSibling($e)
      }
    }
    Marcher $win 0
  }
  "rect" {
    $el = if ($Name -ne "" -or $Type -ne "") { Trouver $win $Name $Type } else { $win }
    if (-not $el) { Write-Error "element introuvable"; exit 1 }
    $r = $el.Current.BoundingRectangle
    "{0} {1} {2} {3}" -f [int]$r.X, [int]$r.Y, [int]($r.X + $r.Width), [int]($r.Y + $r.Height)
  }
  "resize" {
    $p = $win.GetCurrentPattern([System.Windows.Automation.TransformPattern]::Pattern)
    if (-not $p) { Write-Error "fenetre non redimensionnable par UIA"; exit 1 }
    $p.Resize($W, $H)
    Start-Sleep -Milliseconds 300
    $r = $win.Current.BoundingRectangle
    "taille UIA : {0}x{1}" -f [int]$r.Width, [int]$r.Height
  }
  "poser" {
    # LibreOffice reimpose sa taille des qu'on passe par SetWindowPos : on ne le
    # deplace et on ne le redimensionne que par TransformPattern.
    $p = $win.GetCurrentPattern([System.Windows.Automation.TransformPattern]::Pattern)
    if (-not $p) { Write-Error "fenetre non transformable par UIA"; exit 1 }
    if ($W -gt 0 -and $H -gt 0) { $p.Resize($W, $H); Start-Sleep -Milliseconds 250 }
    $p.Move($X, $Y)
    Start-Sleep -Milliseconds 250
    $r = $win.Current.BoundingRectangle
    "pose : ({0},{1}) {2}x{3}" -f [int]$r.X, [int]$r.Y, [int]$r.Width, [int]$r.Height
  }
  "clic" {
    $el = Trouver $win $Name $Type
    if (-not $el) { Write-Error "element '$Name' introuvable"; exit 1 }
    try {
      $ip = $el.GetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern); $ip.Invoke()
      "invoque : $Name"
    } catch {
      $sp = $el.GetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern); $sp.Select()
      "selectionne : $Name"
    }
  }
  "cocher" {
    $el = Trouver $win $Name $Type
    if (-not $el) { Write-Error "element '$Name' introuvable"; exit 1 }
    $tp = $el.GetCurrentPattern([System.Windows.Automation.TogglePattern]::Pattern)
    "$Name : etat $($tp.Current.ToggleState)"
    if ($tp.Current.ToggleState -ne [System.Windows.Automation.ToggleState]::On) { $tp.Toggle() }
    "$Name : etat final $($tp.Current.ToggleState)"
  }
  "texte" {
    $el = Trouver $win $Name $Type
    if (-not $el) { Write-Error "element introuvable"; exit 1 }
    $el.Current.Name
  }
}
