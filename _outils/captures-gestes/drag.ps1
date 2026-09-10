param([int]$X1,[int]$Y1,[int]$X2,[int]$Y2)
$sig=@'
[DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
[DllImport("user32.dll")] public static extern bool SetCursorPos(int x,int y);
[DllImport("user32.dll")] public static extern void mouse_event(uint f,uint dx,uint dy,uint d,UIntPtr e);
'@
Add-Type -Namespace N -Name Mo -MemberDefinition $sig
[void][N.Mo]::SetProcessDPIAware()
[void][N.Mo]::SetCursorPos($X1,$Y1); Start-Sleep -m 200
[N.Mo]::mouse_event(2,0,0,0,[UIntPtr]::Zero); Start-Sleep -m 200
$steps=20
for($i=1;$i -le $steps;$i++){ [void][N.Mo]::SetCursorPos($X1+($X2-$X1)*$i/$steps,$Y1+($Y2-$Y1)*$i/$steps); Start-Sleep -m 25 }
Start-Sleep -m 200
[N.Mo]::mouse_event(4,0,0,0,[UIntPtr]::Zero)
"drag ($X1,$Y1)->($X2,$Y2)"
