# Envoie des touches SEULEMENT si la fenetre au premier plan est bien celle attendue.
# Une frappe egaree va dans le document (ou dans une autre application) et peut
# enregistrer, modifier ou fermer quelque chose : on verifie avant, jamais apres.
param([Parameter(Mandatory=$true)][string]$Attendu, [Parameter(Mandatory=$true)][string]$Keys)
Add-Type -AssemblyName System.Windows.Forms
Add-Type -TypeDefinition 'using System;using System.Runtime.InteropServices;using System.Text;public class Fg{[DllImport("user32.dll")]public static extern IntPtr GetForegroundWindow();[DllImport("user32.dll")]public static extern int GetWindowText(IntPtr h,StringBuilder s,int c);}'
$sb = New-Object System.Text.StringBuilder 512
[void][Fg]::GetWindowText([Fg]::GetForegroundWindow(), $sb, 512)
$titre = $sb.ToString()
if ($titre -notlike "*$Attendu*") {
  Write-Error "frappe annulee : au premier plan il y a '$titre', pas '$Attendu'"
  exit 1
}
[System.Windows.Forms.SendKeys]::SendWait($Keys)
"frappe '$Keys' envoyee a '$titre'"
