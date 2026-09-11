param(
  [string]$Classe = "",   # classe de fenetre exigee (CabinetWClass, SALFRAME, #32770...)
  [Parameter(Mandatory=$true)][string]$Out,
  [string]$Title = "",        # sous-chaine du titre ; vide = fenetre au premier plan
  [int]$Delay = 400
)
Add-Type -AssemblyName System.Drawing
Add-Type @"
using System;
using System.Runtime.InteropServices;
using System.Text;
public class W2 {
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr l);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern int GetClassName(IntPtr h, StringBuilder s, int c);
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int a, out RECT r, int s);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
}
"@
# Conscience DPI par moniteur v2 : sans elle, Windows virtualise les coordonnees
# des qu'une fenetre change d'ecran, et les tailles demandees sortent divisees.
try { [void][W2]::SetThreadDpiAwarenessContext([IntPtr](-4)) } catch { }
[void][W2]::SetProcessDPIAware()   # sinon CopyFromScreen travaille en pixels virtualises
Start-Sleep -Milliseconds $Delay
$h = [IntPtr]::Zero
if ($Title -ne "") {
  $script:found = [IntPtr]::Zero
  $cb = [W2+EnumProc]{
    param($hw, $l)
    if ([W2]::IsWindowVisible($hw)) {
      $sb = New-Object System.Text.StringBuilder 512
      [void][W2]::GetWindowText($hw, $sb, 512)
      if ($sb.ToString() -like "*$Title*") {
        $cn = New-Object System.Text.StringBuilder 256
        [void][W2]::GetClassName($hw, $cn, 256)
        if ($Classe -eq "" -or $cn.ToString() -eq $Classe) { $script:found = $hw; return $false } }
    }
    return $true
  }
  [void][W2]::EnumWindows($cb, [IntPtr]::Zero)
  $h = $script:found
} else { $h = [W2]::GetForegroundWindow() }
if ($h -eq [IntPtr]::Zero) { Write-Error "fenetre introuvable"; exit 1 }
$r = New-Object W2+RECT
if ([W2]::DwmGetWindowAttribute($h, 9, [ref]$r, 16) -ne 0) { [void][W2]::GetWindowRect($h, [ref]$r) }
$w = $r.R - $r.L; $hh = $r.B - $r.T
$bmp = New-Object System.Drawing.Bitmap($w, $hh)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen($r.L, $r.T, 0, 0, (New-Object System.Drawing.Size($w, $hh)))
$g.Dispose()
$bmp.Save($Out, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
$sb = New-Object System.Text.StringBuilder 512
[void][W2]::GetWindowText($h, $sb, 512)
Write-Output "$Out  ($w x $hh)  titre='$($sb.ToString())'"
