# Stake Engine documentation for our team

Verified documentation snapshot captured **2026-10-15 UTC**, covering **67 documentation routes** and **51 approval-checklist items supplied through screenshots**. Includes searchable Markdown, original assets, HTML/DOM captures, screenshots, provenance, and agent guidance.

## Download the complete ZIP

**[Download stake-engine-docs.zip](https://github.com/jordanschock632-spec/stake-engine-docs/releases/download/docs-2026-10-15-checklist/stake-engine-docs.zip)**

The original ZIP is 137,818,122 bytes, above GitHub's normal 100 MiB Git-file limit, so the complete file is attached to this repository's [release](https://github.com/jordanschock632-spec/stake-engine-docs/releases/tag/docs-2026-10-15-checklist). Choose `stake-engine-docs.zip` under Assets. GitHub's automatically generated source-code ZIP contains the installer and this README; it is not the full documentation archive.

The repository and release are public. No invitation or GitHub sign-in is needed to download them.

## Install into a game project

Use Python 3.9+ and an existing game project folder. Inspect [install.py](install.py), then:

```text
git clone https://github.com/jordanschock632-spec/stake-engine-docs.git
cd stake-engine-docs
python install.py --project /path/to/your/game-project
```

On Windows, quote the project path, for example `--project "C:\Projects\our-game"`.

The installer downloads the full ZIP automatically. No GitHub CLI, Git LFS, or additional Python packages are required. You can also download the ZIP manually and use:

```text
python install.py --archive /path/to/stake-engine-docs.zip --project /path/to/your/game-project
```

The installer verifies the original ZIP SHA-256, ZIP integrity, safe paths, and all 1,232 payload checksums. It installs the complete archive to `<project>/.agents/skills/stake-engine-docs/` and refuses to overwrite an existing skill. It does not change global configuration, install game dependencies, or run documentation examples.

## Prompt for your Codex worker

Copy the block in [COFOUNDER_PROMPT.md](COFOUNDER_PROMPT.md).

Project-local skill discovery uses `.agents/skills/`; see the [official skill documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills). If the installed skill does not appear, restart Codex. The worker can also read the installed `SKILL.md` explicitly.

## Integrity and scope

```text
stake-engine-docs.zip
SHA-256: 0f74779f8927dcd3b290c1d1cbdb53a9c4991b9401ec9be62936d52ba25500ef
```

The archive contains its complete checksum inventory, coverage and verification reports, and source records. It is a dated reference snapshot, not an official approval or a guarantee that future requirements remain unchanged. The formerly restricted checklist comes from three user-supplied screenshots; provenance and limitations are documented separately in the archive.

Documentation and artwork remain the property of their original authors. No license to the copied documentation is implied by this repository.
