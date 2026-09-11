param(
  # Classe de fenetre exigee : CabinetWClass = Explorateur, SALFRAME = LibreOffice,
  # #32770 = boite de dialogue Windows. Vide = on ne filtre que sur le titre.
  [string]$Classe = "",
  [string]$Title)
Add-Type @"
using System; using System.Runtime.InteropServices; using System.Text;
public class W5 {
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr l);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern int GetClassName(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int c);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
}
"@
# Conscience DPI par moniteur v2 : sans elle, Windows virtualise les coordonnees
# des qu'une fenetre change d'ecran, et les tailles demandees sortent divisees.
try { [void][W5]::SetThreadDpiAwarenessContext([IntPtr](-4)) } catch { }
[void][W5]::SetProcessDPIAware()
$script:found=[IntPtr]::Zero
$cb=[W5+EnumProc]{ param($hw,$l)
  if ([W5]::IsWindowVisible($hw)) { $sb=New-Object System.Text.StringBuilder 512; [void][W5]::GetWindowText($hw,$sb,512)
    if ($sb.ToString() -like "*$Title*") {
        $cn = New-Object System.Text.StringBuilder 256
        [void][W5]::GetClassName($hw, $cn, 256)
        if ($Classe -eq "" -or $cn.ToString() -eq $Classe) { $script:found=$hw; return $false } } }
  return $true }
[void][W5]::EnumWindows($cb,[IntPtr]::Zero)
if ($script:found -eq [IntPtr]::Zero) { Write-Error "introuvable"; exit 1 }
[void][W5]::ShowWindow($script:found, 9)   # SW_RESTORE
[void][W5]::SetForegroundWindow($script:found)
"restauree"
