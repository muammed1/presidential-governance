# Download and install

This guide covers manual installation of **1.1.0-preview.4**, an experimental preview. See [validation limits](../VALIDATION.md) before relying on it. There is no package-manager dependency installation.

## Get the files

On the published repository page, select **Code → Download ZIP**. Alternatively, if a maintainer has attached a versioned skill ZIP to a GitHub release, download that asset. Extract it and locate the directory whose immediate child is `SKILL.md`.

Repository: [muammed1/presidential-governance](https://github.com/muammed1/presidential-governance). Versioned download: [1.1.0-preview.4 ZIP](https://github.com/muammed1/presidential-governance/releases/download/v1.1.0-preview.4/presidential-governance-1.1.0-preview.4.zip). The [release page](https://github.com/muammed1/presidential-governance/releases/tag/v1.1.0-preview.4) provides the manifest and SHA-256 file; compare the ZIP hash before installing when checking artifact integrity. [GitHub's source archive instructions](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives).

Install the entire skill directory, including `references`, `assets`, `scripts`, and `tests`. Copying `SKILL.md` alone breaks resource links. Do not copy a maintainer's development workspace, backups, chats or raw evaluation records.

## Codex: install for your user

Use the user skill directory `~/.agents/skills`. The final layout should be:

```text
~/.agents/skills/presidential-governance/
    SKILL.md
    README.md
    LICENSE
    references/
    assets/
    scripts/
    tests/
    docs/
```

These paths and invocation controls follow [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills). Other agent hosts may use different loading locations; consult their own documentation.

### Windows PowerShell

Replace the source path with your extracted folder. Run these commands yourself, or explicitly authorize your agent to perform this installation. They stop if the target already exists.

```powershell
$sourceFolder = 'D:\Downloads\presidential-governance-main'
$skillsRoot = Join-Path $env:USERPROFILE '.agents\skills'
$destination = Join-Path $skillsRoot 'presidential-governance'
if (-not (Test-Path -LiteralPath (Join-Path $sourceFolder 'SKILL.md') -PathType Leaf)) {
    throw 'Select the extracted folder containing SKILL.md.'
}
if (Test-Path -LiteralPath $destination) {
    throw 'Already installed. Review and back up the existing folder before replacing it.'
}
New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null
Copy-Item -LiteralPath $sourceFolder -Destination $destination -Recurse
```

### macOS / Linux

Replace the source path. This recipe has not been executed on macOS or Linux in the current validation.

```sh
source_dir="/path/to/extracted/presidential-governance-main"
destination="$HOME/.agents/skills/presidential-governance"
if [ ! -f "$source_dir/SKILL.md" ]; then
    printf '%s\n' 'Select the folder containing SKILL.md.' >&2
    exit 1
fi
if [ -e "$destination" ]; then
    printf '%s\n' 'Already installed. Review and back it up before replacing it.' >&2
    exit 1
fi
mkdir -p "$HOME/.agents/skills"
cp -R "$source_dir" "$destination"
```

### Project-only alternative

For repository-scoped Codex use, place the same folder at `.agents/skills/presidential-governance` inside the project instead of the user directory. Avoid installing duplicate copies in overlapping scopes unless you intend that behavior. A project-local install affects the files you may share with collaborators.

## Load and try

Codex detects skill changes automatically; restart it if the skill does not appear. Check that `SKILL.md` is directly inside the installed `presidential-governance` folder rather than an extra nested directory. Confirm the skill is available/enabled in your host.

Select it in the host's skill picker. In Codex CLI/IDE, an explicit example is:

```text
Use $presidential-governance in Professional mode.
Help me inspect this project and propose a small plan.
Discovery only; no edits or independent agents.
```

The [English usage guide](USAGE.en.md), [Arabic usage guide](USAGE.ar.md) and [README](../README.md) explain modes, approvals and review choices. Loading the skill grants no project execution or independent dispatch permission.

## Update, remove or recover

Before updating, record the installed version from `SKILL.md`, preserve the entire old folder outside any skill discovery directory, and review the new version's changes and validation limits. Resolve any folder collision before copying; the snippets above deliberately do not overwrite an existing installation. Do not merge an old folder with a new one, because removed files could remain.

For removal or recovery, close active use and manually move the installed skill outside discovery roots. Restore the preserved folder to the same original location if needed. Refresh/restart the host and verify the detected version. Installation removal does not undo changes in projects that previously used the skill. No automatic updater or rollback service is included.

## Optional local checks

If Python 3.10+ is already available, run the [README check commands](../README.md#local-checks) from the skill directory. They need only the standard library. These checks are optional for using the instructions; passing them does not authenticate approvals or validate independent review isolation.

The external official skill Metadata validator is a separate development tool. It passed in the 2026-11-08 follow-up using an already present PyYAML 6.0.3 tool directory after the default Python environment had failed to import YAML. No dependencies were installed or copied; the skill itself still has no YAML dependency. See [validation status](../VALIDATION.md).
