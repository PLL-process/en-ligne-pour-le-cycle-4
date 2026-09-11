# Clic (ou double-clic, ou clic droit) a une position ecran en pixels physiques.
param([int]$X, [int]$Y, [string]$Bouton = "gauche", [int]$Nb = 1)
$sig = @'
[DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
[DllImport("user32.dll")] public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);
[DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
[DllImport("user32.dll")] public static extern bool GetCursorPos(out POINT p);
[DllImport("user32.dll")] public static extern void mouse_event(uint f, uint dx, uint dy, uint d, UIntPtr e);
[StructLayout(LayoutKind.Sequential)] public struct POINT { public int X, Y; }
'@
Add-Type -Namespace N -Name Cl -MemberDefinition $sig
try { [void][N.Cl]::SetThreadDpiAwarenessContext([IntPtr](-4)) } catch { }
[void][N.Cl]::SetProcessDPIAware()
[void][N.Cl]::SetCursorPos($X, $Y)
Start-Sleep -Milliseconds 250
$p = New-Object N.Cl+POINT
[void][N.Cl]::GetCursorPos([ref]$p)
if ([math]::Abs($p.X - $X) -gt 2 -or [math]::Abs($p.Y - $Y) -gt 2) {
  Write-Error "curseur pose en ($($p.X),$($p.Y)) au lieu de ($X,$Y) : mise a l'echelle non neutralisee"
  exit 1
}
$bas = if ($Bouton -eq "droit") { 8 } else { 2 }
$haut = if ($Bouton -eq "droit") { 16 } else { 4 }
for ($i = 0; $i -lt $Nb; $i++) {
  [N.Cl]::mouse_event($bas, 0, 0, 0, [UIntPtr]::Zero)
  Start-Sleep -Milliseconds 60
  [N.Cl]::mouse_event($haut, 0, 0, 0, [UIntPtr]::Zero)
  if ($Nb -gt 1) { Start-Sleep -Milliseconds 90 }
}
"clic $Bouton x$Nb en ($X,$Y)"
