# Enchaine des frappes dans UNE fenetre, en reverifiant le focus avant chacune.
# Regrouper les etapes dans un seul processus evite que le focus derive entre
# deux appels : une frappe egaree ouvre le menu Demarrer ou modifie le document.
param(
  [Parameter(Mandatory=$true)][string]$Titre,
  # Les frappes arrivent en UNE chaine separee par § : powershell -File ne sait
  # pas recevoir un tableau, il collerait tout en un seul element.
  [Parameter(Mandatory=$true)][string]$Frappes,
  [int]$PauseMs = 500,
  # La classe verrouille la cible : sans elle, un titre peut designer une autre
  # application (la fenetre de Claude porte le texte de la conversation).
  [string]$Classe = ""
)
Add-Type -AssemblyName System.Windows.Forms
Add-Type -TypeDefinition @"
using System; using System.Runtime.InteropServices; using System.Text;
public class Sf {
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr l);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern int GetClassName(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
  [DllImport("user32.dll")] public static extern void mouse_event(uint f, uint dx, uint dy, uint d, UIntPtr e);
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int a, out RECT r, int s);
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
}
"@
try { [void][Sf]::SetThreadDpiAwarenessContext([IntPtr](-4)) } catch { }
[void][Sf]::SetProcessDPIAware()

function Poignee($t) {
  $script:h = [IntPtr]::Zero
  $cb = [Sf+EnumProc]{ param($hw, $l)
    if ([Sf]::IsWindowVisible($hw)) {
      $sb = New-Object System.Text.StringBuilder 512
      [void][Sf]::GetWindowText($hw, $sb, 512)
      if ($sb.ToString() -like "*$t*") {
        $cn = New-Object System.Text.StringBuilder 256
        [void][Sf]::GetClassName($hw, $cn, 256)
        if ($Classe -eq "" -or $cn.ToString() -eq $Classe) { $script:h = $hw; return $false } } }
    return $true }
  [void][Sf]::EnumWindows($cb, [IntPtr]::Zero)
  return $script:h
}
function Devant($t) {
  $h = Poignee $t
  if ($h -eq [IntPtr]::Zero) { return $false }
  if ([Sf]::GetForegroundWindow() -eq $h) { return $true }
  # On clique la barre de titre : c'est le seul moyen fiable de reprendre le
  # focus quand une autre application l'a pris (SetForegroundWindow est bride).
  $r = New-Object Sf+RECT
  [void][Sf]::DwmGetWindowAttribute($h, 9, [ref]$r, 16)
  [void][Sf]::SetCursorPos([int](($r.L + $r.R) / 2), $r.T + 35)
  Start-Sleep -Milliseconds 200
  [Sf]::mouse_event(2, 0, 0, 0, [UIntPtr]::Zero)
  [Sf]::mouse_event(4, 0, 0, 0, [UIntPtr]::Zero)
  Start-Sleep -Milliseconds 400
  [void][Sf]::SetForegroundWindow($h)
  Start-Sleep -Milliseconds 300
  return ([Sf]::GetForegroundWindow() -eq $h)
}
$liste = $Frappes -split "§"
foreach ($f in $liste) {
  if (-not (Devant $Titre)) { Write-Error "'$Titre' n'a pas le focus : serie interrompue avant '$f'"; exit 1 }
  [System.Windows.Forms.SendKeys]::SendWait($f)
  Start-Sleep -Milliseconds $PauseMs
}
"serie de $($liste.Count) frappe(s) envoyee a '$Titre'"
