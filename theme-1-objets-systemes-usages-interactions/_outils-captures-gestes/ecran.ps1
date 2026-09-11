# Capture une zone de l'ecran en pixels physiques (pour voir menus et infobulles,
# qui ne font pas partie de la fenetre et echappent a capwin.ps1).
param([int]$X, [int]$Y, [int]$W, [int]$H, [string]$Out)
Add-Type -AssemblyName System.Drawing
Add-Type -TypeDefinition 'using System;using System.Runtime.InteropServices;public class Sc{[DllImport("user32.dll")]public static extern bool SetProcessDPIAware();[DllImport("user32.dll")]public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);}'
try { [void][Sc]::SetThreadDpiAwarenessContext([IntPtr](-4)) } catch { }
[void][Sc]::SetProcessDPIAware()
$b = New-Object System.Drawing.Bitmap($W, $H)
$g = [System.Drawing.Graphics]::FromImage($b)
$g.CopyFromScreen($X, $Y, 0, 0, (New-Object System.Drawing.Size($W, $H)))
$g.Dispose()
$b.Save($Out, [System.Drawing.Imaging.ImageFormat]::Png)
$b.Dispose()
"$Out ($W x $H)"
