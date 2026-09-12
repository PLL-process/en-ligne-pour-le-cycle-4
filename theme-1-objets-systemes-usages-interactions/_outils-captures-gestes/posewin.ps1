# Pose une fenetre a une taille exacte, en pixels physiques, meme si elle est maximisee ou ancree.
# Passe par SetWindowPlacement : SetWindowPos seul est ignore sur une fenetre maximisee.
param(
  [string]$Classe = "",   # classe de fenetre exigee (CabinetWClass, SALFRAME, #32770...)
  [string]$Title = "",    # sous-chaine du titre ; vide = fenetre au premier plan
  [int]$X = 200, [int]$Y = 120, [int]$W = 2400, [int]$H = 1500)
Add-Type @"
using System; using System.Runtime.InteropServices; using System.Text;
public class W6 {
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
  [StructLayout(LayoutKind.Sequential)] public struct POINT { public int X, Y; }
  [StructLayout(LayoutKind.Sequential)] public struct WP {
    public int length, flags, showCmd; public POINT minPos, maxPos; public RECT normalPos; }
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr l);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern int GetClassName(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern bool GetWindowPlacement(IntPtr h, ref WP p);
  [DllImport("user32.dll")] public static extern bool SetWindowPlacement(IntPtr h, ref WP p);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int a, out RECT r, int s);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
}
"@
# Conscience DPI par moniteur v2 : sans elle, Windows virtualise les coordonnees
# des qu'une fenetre change d'ecran, et les tailles demandees sortent divisees.
try { [void][W6]::SetThreadDpiAwarenessContext([IntPtr](-4)) } catch { }
[void][W6]::SetProcessDPIAware()
$h=[IntPtr]::Zero
if ($Title -ne "") {
  $script:found=[IntPtr]::Zero
  $cb=[W6+EnumProc]{ param($hw,$l)
    if ([W6]::IsWindowVisible($hw)) { $sb=New-Object System.Text.StringBuilder 512; [void][W6]::GetWindowText($hw,$sb,512)
      if ($sb.ToString() -like "*$Title*") {
        $cn = New-Object System.Text.StringBuilder 256
        [void][W6]::GetClassName($hw, $cn, 256)
        if ($Classe -eq "" -or $cn.ToString() -eq $Classe) { $script:found=$hw; return $false } } }
    return $true }
  [void][W6]::EnumWindows($cb,[IntPtr]::Zero); $h=$script:found
} else { $h=[W6]::GetForegroundWindow() }
if ($h -eq [IntPtr]::Zero) { Write-Error "fenetre introuvable"; exit 1 }
# La bordure invisible : ecart entre le cadre DWM (ce que capwin capture) et le cadre fenetre.
$dwm=New-Object W6+RECT; [void][W6]::DwmGetWindowAttribute($h,9,[ref]$dwm,16)
$win=New-Object W6+RECT; [void][W6]::GetWindowRect($h,[ref]$win)
$padL=$dwm.L-$win.L; $padT=$dwm.T-$win.T
$padW=($win.R-$win.L)-($dwm.R-$dwm.L); $padH=($win.B-$win.T)-($dwm.B-$dwm.T)
$p=New-Object W6+WP; $p.length=[Runtime.InteropServices.Marshal]::SizeOf($p)
[void][W6]::GetWindowPlacement($h,[ref]$p)
$p.showCmd=1   # SW_SHOWNORMAL : defait maximise et ancrage
$r=New-Object W6+RECT
$r.L=$X-$padL; $r.T=$Y-$padT; $r.R=$X-$padL+$W+$padW; $r.B=$Y-$padT+$H+$padH
$p.normalPos=$r
[void][W6]::SetWindowPlacement($h,[ref]$p)
[void][W6]::SetForegroundWindow($h)
Start-Sleep -Milliseconds 350
[void][W6]::DwmGetWindowAttribute($h,9,[ref]$dwm,16)
"cadre visible : $($dwm.L) $($dwm.T) $($dwm.R) $($dwm.B)  ->  $($dwm.R-$dwm.L) x $($dwm.B-$dwm.T)"
