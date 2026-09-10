param([string]$Title)
Add-Type @"
using System; using System.Runtime.InteropServices; using System.Text;
public class W4 {
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr l);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int c);
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int a, out RECT r, int s);
}
"@
[void][W4]::SetProcessDPIAware()
$script:found=[IntPtr]::Zero
$cb=[W4+EnumProc]{ param($hw,$l)
  if ([W4]::IsWindowVisible($hw)) { $sb=New-Object System.Text.StringBuilder 512; [void][W4]::GetWindowText($hw,$sb,512)
    if ($sb.ToString() -like "*$Title*") { $script:found=$hw; return $false } }
  return $true }
[void][W4]::EnumWindows($cb,[IntPtr]::Zero)
$r=New-Object W4+RECT; [void][W4]::DwmGetWindowAttribute($script:found,9,[ref]$r,16)
"$($r.L) $($r.T) $($r.R) $($r.B)"
