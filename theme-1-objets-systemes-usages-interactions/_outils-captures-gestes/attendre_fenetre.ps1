# Attend qu'une fenetre dont le titre contient $Titre soit au premier plan,
# en la ramenant devant si besoin. Rend la main des qu'elle y est, ou echoue.
param([Parameter(Mandatory=$true)][string]$Titre, [int]$Secondes = 20)
Add-Type -TypeDefinition @"
using System; using System.Runtime.InteropServices; using System.Text;
public class Wt {
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr l);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int c);
  [DllImport("user32.dll")] public static extern void keybd_event(byte k, byte s, uint f, UIntPtr e);
}
"@
function Chercher($t) {
  $script:trouve = [IntPtr]::Zero
  $cb = [Wt+EnumProc]{ param($hw, $l)
    if ([Wt]::IsWindowVisible($hw)) {
      $sb = New-Object System.Text.StringBuilder 512
      [void][Wt]::GetWindowText($hw, $sb, 512)
      if ($sb.ToString() -like "*$t*") { $script:trouve = $hw; return $false } }
    return $true }
  [void][Wt]::EnumWindows($cb, [IntPtr]::Zero)
  return $script:trouve
}
for ($i = 0; $i -lt $Secondes; $i++) {
  $h = Chercher $Titre
  if ($h -ne [IntPtr]::Zero) {
    if ([Wt]::GetForegroundWindow() -ne $h) {
      # Windows refuse le vol de focus tant qu'aucune touche n'a ete pressee :
      # un appui/relachement d'Alt debloque SetForegroundWindow.
      [Wt]::keybd_event(0x12, 0, 0, [UIntPtr]::Zero)
      [Wt]::keybd_event(0x12, 0, 2, [UIntPtr]::Zero)
      [void][Wt]::ShowWindow($h, 9)
      [void][Wt]::SetForegroundWindow($h)
      Start-Sleep -Milliseconds 500
    }
    if ([Wt]::GetForegroundWindow() -eq $h) { "au premier plan : $Titre"; exit 0 }
  }
  Start-Sleep -Seconds 1
}
Write-Error "'$Titre' n'est pas venue au premier plan en $Secondes s"
exit 1
