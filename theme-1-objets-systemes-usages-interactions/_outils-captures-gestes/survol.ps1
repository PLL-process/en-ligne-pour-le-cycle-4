# Pose le curseur sur un point (sans cliquer) pour obtenir l'etat survole d'un bouton.
# Rappel : sous curseur simule, Windows n'affiche pas l'infobulle — on capture le bouton surligne.
param([int]$X, [int]$Y)
$sig = @'
[DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
[DllImport("user32.dll")] public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);
[DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
'@
Add-Type -Namespace N -Name Sv -MemberDefinition $sig
try { [void][N.Sv]::SetThreadDpiAwarenessContext([IntPtr](-4)) } catch { }
[void][N.Sv]::SetProcessDPIAware()
[void][N.Sv]::SetCursorPos($X - 40, $Y)
Start-Sleep -Milliseconds 150
[void][N.Sv]::SetCursorPos($X, $Y)
Start-Sleep -Milliseconds 500
"survol en ($X,$Y)"
