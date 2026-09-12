# PIEGE : en PowerShell les variables ne distinguent pas la casse. La poignee de
# fenetre s'appelait $h, et ecrasait donc le parametre $H — la hauteur demandee
# devenait le numero de la poignee, que Windows rabotait a la hauteur de l'ecran.
# Mesure le 12/09/2026 : 660 px demandes, 2178 obtenus, sur trois classes de
# fenetres. La poignee s'appelle $hFen depuis.
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
$hFen=[IntPtr]::Zero
if ($Title -ne "") {
  $script:found=[IntPtr]::Zero
  $cb=[W3+EnumProc]{ param($hw,$l)
    if ([W3]::IsWindowVisible($hw)) { $sb=New-Object System.Text.StringBuilder 512; [void][W3]::GetWindowText($hw,$sb,512)
      if ($sb.ToString() -like "*$Title*") { $script:found=$hw; return $false } }
    return $true }
  [void][W3]::EnumWindows($cb,[IntPtr]::Zero); $hFen=$script:found
} else { $hFen=[W3]::GetForegroundWindow() }
if ($hFen -eq [IntPtr]::Zero) { Write-Error "introuvable"; exit 1 }
$r=New-Object W3+RECT; [void][W3]::GetWindowRect($hFen,[ref]$r)
if ($W -eq 0) { $W=$r.R-$r.L }; if ($H -eq 0) { $H=$r.B-$r.T }
[void][W3]::SetWindowPos($hFen,[IntPtr]::Zero,$X,$Y,$W,$H,0x0004)   # SWP_NOZORDER
[void][W3]::GetWindowRect($hFen,[ref]$r)
"deplacee: L=$($r.L) T=$($r.T) R=$($r.R) B=$($r.B)"
