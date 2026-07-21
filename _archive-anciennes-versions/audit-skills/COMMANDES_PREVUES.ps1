#requires -Version 7.0
<#
Journal des commandes prévues — audit du 15 juillet 2026.
Par défaut, ce fichier n'exécute rien. Les candidats B restent volontairement
désactivés jusqu'à validation humaine explicite.

Exécution A réussie le 15 juillet 2026.
Sauvegarde créée : C:\\Users\\PhaseLockedLoop\\.codex\\backups\\skills\\find-skills-20260715-070643
#>
param(
    [switch]$MettreAJourFindSkills
)

$ErrorActionPreference = 'Stop'
$CommitFindSkills = '5527c09adc367612b0bffd9c80e3bc28a6b01b6d'
$Python = 'C:\Users\PhaseLockedLoop\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$Installer = Join-Path $HOME '.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py'
$SkillsRoot = [IO.Path]::GetFullPath((Join-Path $HOME '.agents\skills'))
$Source = [IO.Path]::GetFullPath((Join-Path $SkillsRoot 'find-skills'))
$BackupRoot = [IO.Path]::GetFullPath((Join-Path $HOME '.codex\backups\skills'))

if ($MettreAJourFindSkills) {
    if (-not $Source.StartsWith($SkillsRoot, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Chemin source inattendu : $Source"
    }
    if (-not $BackupRoot.StartsWith([IO.Path]::GetFullPath((Join-Path $HOME '.codex')), [StringComparison]::OrdinalIgnoreCase)) {
        throw "Chemin de sauvegarde inattendu : $BackupRoot"
    }
    if (-not (Test-Path -LiteralPath $Source)) {
        throw "Skill existant introuvable : $Source"
    }

    New-Item -ItemType Directory -Path $BackupRoot -Force | Out-Null
    $Backup = Join-Path $BackupRoot ('find-skills-' + (Get-Date -Format 'yyyyMMdd-HHmmss'))
    Move-Item -LiteralPath $Source -Destination $Backup

    try {
        & $Python $Installer --repo vercel-labs/skills --path skills/find-skills --ref $CommitFindSkills --dest $SkillsRoot
        if ($LASTEXITCODE -ne 0) { throw "Échec de l'installateur officiel (code $LASTEXITCODE)" }
    }
    catch {
        if (-not (Test-Path -LiteralPath $Source) -and (Test-Path -LiteralPath $Backup)) {
            Move-Item -LiteralPath $Backup -Destination $Source
        }
        throw
    }
}

# B — ne pas exécuter sans validation :
# codex plugin add hugging-face@openai-curated
# codex plugin marketplace add wshobson/agents --ref b6af3711058190e4b5c5274b9758498fe626ec5a --sparse .agents/plugins --sparse plugins/accessibility-compliance
# codex plugin add accessibility-compliance@claude-code-workflows

# Rollbacks manuels B :
# codex plugin remove hugging-face@openai-curated
# codex plugin remove accessibility-compliance@claude-code-workflows
# codex plugin marketplace remove claude-code-workflows
