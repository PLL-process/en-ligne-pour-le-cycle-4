param(
  # Classe de fenetre exigee : CabinetWClass = Explorateur, SALFRAME = LibreOffice,
  # #32770 = boite de dialogue Windows. Vide = on ne filtre que sur le titre.
  [string]$Classe = "",
  [string]$Title)
Add-Type @"
using System; using System.Runtime.InteropServices; using System.Text;
public class W4 {
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr l);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern int GetClassName(IntPtr h, StringBuilder s, int c);
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int a, out RECT r, int s);
}
"@
# Conscience DPI par moniteur v2 : sans elle, Windows virtualise les coordonnees
# des qu'une fenetre change d'ecran, et les tailles demandees sortent divisees.
try { [void][W4]::SetThreadDpiAwarenessContext([IntPtr](-4)) } catch { }
[void][W4]::SetProcessDPIAware()
$script:found=[IntPtr]::Zero
$cb=[W4+EnumProc]{ param($hw,$l)
  if ([W4]::IsWindowVisible($hw)) { $sb=New-Object System.Text.StringBuilder 512; [void][W4]::GetWindowText($hw,$sb,512)
    if ($sb.ToString() -like "*$Title*") {
        $cn = New-Object System.Text.StringBuilder 256
        [void][W4]::GetClassName($hw, $cn, 256)
        if ($Classe -eq "" -or $cn.ToString() -eq $Classe) { $script:found=$hw; return $false } } }
  return $true }
[void][W4]::EnumWindows($cb,[IntPtr]::Zero)
$r=New-Object W4+RECT; [void][W4]::DwmGetWindowAttribute($script:found,9,[ref]$r,16)
"$($r.L) $($r.T) $($r.R) $($r.B)"
