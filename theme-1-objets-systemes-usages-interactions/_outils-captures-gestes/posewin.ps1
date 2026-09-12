# Pose une fenetre a une taille exacte, en pixels physiques, meme si elle est maximisee ou ancree.
# On DEFAIT d'abord l'etat maximise (SW_RESTORE) — c'est lui, et lui seul, qui faisait
# ignorer SetWindowPos — puis on pose la fenetre par SetWindowPos, et on RELIT le cadre.
# SetWindowPlacement, employe ici jusqu'au 12/09/2026, posait bien la largeur et jamais
# la hauteur : mesure ce jour-la sur trois classes de fenetres (SALSUBFRAME, SALFRAME,
# CabinetWClass), 660 px demandes, 2178 obtenus a chaque fois. Les quatre premiers lots de
# la vague « tableur » ont ete recadres a la main faute de l'avoir vu.
# PIEGE : en PowerShell les variables ne distinguent pas la casse. La poignee de
# fenetre s'appelait $h, et ecrasait donc le parametre $H — la hauteur demandee
# devenait le numero de la poignee, que Windows rabotait a la hauteur de l'ecran.
# Mesure le 12/09/2026 : 660 px demandes, 2178 obtenus, sur trois classes de
# fenetres. La poignee s'appelle $hFen depuis.
param(
  [string]$Classe = "",   # classe de fenetre exigee (CabinetWClass, SALFRAME, #32770...)
  [string]$Title = "",    # sous-chaine du titre ; vide = fenetre au premier plan
  [int]$X = 200, [int]$Y = 120, [int]$W = 2400, [int]$H = 1500)
Add-Type @"
using System; using System.Runtime.InteropServices; using System.Text;
public class W6 {
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
  [StructLayout(LayoutKind.Sequential)] public struct POINT { public int X, Y; }
  [StructLayout(LayoutKind.Sequential)] public struct WP {
    public int length, flags, showCmd; public POINT minPos, maxPos; public RECT normalPos; }
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern IntPtr SetThreadDpiAwarenessContext(IntPtr c);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr l);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern int GetClassName(IntPtr h, StringBuilder s, int c);
  [DllImport("user32.dll")] public static extern bool GetWindowPlacement(IntPtr h, ref WP p);
  [DllImport("user32.dll")] public static extern bool SetWindowPlacement(IntPtr h, ref WP p);
  [DllImport("user32.dll")] public static extern bool SetWindowPos(IntPtr h, IntPtr a, int x, int y, int cx, int cy, uint f);
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int c);
  [DllImport("user32.dll")] public static extern bool IsZoomed(IntPtr h);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int a, out RECT r, int s);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
}
"@
# Conscience DPI par moniteur v2 : sans elle, Windows virtualise les coordonnees
# des qu'une fenetre change d'ecran, et les tailles demandees sortent divisees.
try { [void][W6]::SetThreadDpiAwarenessContext([IntPtr](-4)) } catch { }
[void][W6]::SetProcessDPIAware()
$hFen=[IntPtr]::Zero
if ($Title -ne "") {
  $script:found=[IntPtr]::Zero
  $cb=[W6+EnumProc]{ param($hw,$l)
    if ([W6]::IsWindowVisible($hw)) { $sb=New-Object System.Text.StringBuilder 512; [void][W6]::GetWindowText($hw,$sb,512)
      if ($sb.ToString() -like "*$Title*") {
        $cn = New-Object System.Text.StringBuilder 256
        [void][W6]::GetClassName($hw, $cn, 256)
        if ($Classe -eq "" -or $cn.ToString() -eq $Classe) { $script:found=$hw; return $false } } }
    return $true }
  [void][W6]::EnumWindows($cb,[IntPtr]::Zero); $hFen=$script:found
} else { $hFen=[W6]::GetForegroundWindow() }
if ($hFen -eq [IntPtr]::Zero) { Write-Error "fenetre introuvable"; exit 1 }
# La bordure invisible : ecart entre le cadre DWM (ce que capwin capture) et le cadre fenetre.
$dwm=New-Object W6+RECT; [void][W6]::DwmGetWindowAttribute($hFen,9,[ref]$dwm,16)
$win=New-Object W6+RECT; [void][W6]::GetWindowRect($hFen,[ref]$win)
$padL=$dwm.L-$win.L; $padT=$dwm.T-$win.T
$padW=($win.R-$win.L)-($dwm.R-$dwm.L); $padH=($win.B-$win.T)-($dwm.B-$dwm.T)
if ([W6]::IsZoomed($hFen)) { [void][W6]::ShowWindow($hFen, 9); Start-Sleep -Milliseconds 400 }  # SW_RESTORE
# On vise le cadre VISIBLE : on ajoute la bordure invisible pour que capwin, qui capture
# ce cadre-la, recoive exactement les $W x $H demandes.
[void][W6]::SetWindowPos($hFen, [IntPtr]::Zero, $X-$padL, $Y-$padT, $W+$padW, $H+$padH, 0x0004)  # SWP_NOZORDER
[void][W6]::SetForegroundWindow($hFen)
Start-Sleep -Milliseconds 350
[void][W6]::DwmGetWindowAttribute($hFen,9,[ref]$dwm,16)
$vw=$dwm.R-$dwm.L; $vh=$dwm.B-$dwm.T
"cadre visible : $($dwm.L) $($dwm.T) $($dwm.R) $($dwm.B)  ->  $vw x $vh"
# Une fenetre peut refuser une taille (taille minimale de l'application) : on le DIT,
# plutot que de laisser la capture suivante sortir a une taille qu'on n'a pas voulue.
if ($vw -ne $W -or $vh -ne $H) { Write-Warning "taille refusee : $W x $H demandes, $vw x $vh obtenus" }
