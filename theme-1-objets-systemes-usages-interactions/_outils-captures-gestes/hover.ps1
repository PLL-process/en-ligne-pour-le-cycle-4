param([int]$X,[int]$Y,[int]$Ms=1800)
$sig='[DllImport("user32.dll")] public static extern bool SetCursorPos(int x,int y);'
Add-Type -Namespace N -Name M -MemberDefinition $sig
[void][N.M]::SetCursorPos($X-12,$Y+8); Start-Sleep -m 150
[void][N.M]::SetCursorPos($X-5,$Y+3);  Start-Sleep -m 150
[void][N.M]::SetCursorPos($X,$Y);      Start-Sleep -m $Ms
