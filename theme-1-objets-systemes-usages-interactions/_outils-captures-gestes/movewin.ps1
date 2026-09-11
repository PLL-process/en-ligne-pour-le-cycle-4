param([string]$Title="", [int]$X=60, [int]$Y=60, [int]$W=0, [int]$H=0)
Add-Type @"
using System; using System.Runtime.InteropServices; using System.Text;
public class W3 {
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr l);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr h, IntPtr a, int x, int y, int cx, int cy, uint f);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
}
"@
[void][W3]::SetProcessDPIAware()
$h=[IntPtr]::Zero
if ($Title -ne "") {
  $script:found=[IntPtr]::Zero
  $cb=[W3+EnumProc]{ param($hw,$l)
    if ([W3]::IsWindowVisible($hw)) { $sb=New-Object System.Text.StringBuilder 512; [void][W3]::GetWindowText($hw,$sb,512)
      if ($sb.ToString() -like "*$Title*") { $script:found=$hw; return $false } }
    return $true }
  [void][W3]::EnumWindows($cb,[IntPtr]::Zero); $h=$script:found
} else { $h=[W3]::GetForegroundWindow() }
if ($h -eq [IntPtr]::Zero) { Write-Error "introuvable"; exit 1 }
$r=New-Object W3+RECT; [void][W3]::GetWindowRect($h,[ref]$r)
if ($W -eq 0) { $W=$r.R-$r.L }; if ($H -eq 0) { $H=$r.B-$r.T }
[void][W3]::SetWindowPos($h,[IntPtr]::Zero,$X,$Y,$W,$H,0x0004)   # SWP_NOZORDER
[void][W3]::GetWindowRect($h,[ref]$r)
"deplacee: L=$($r.L) T=$($r.T) R=$($r.R) B=$($r.B)"
