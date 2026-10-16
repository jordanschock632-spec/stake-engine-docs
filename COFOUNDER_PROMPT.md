# Send this to your Codex worker

```text
Install our verified Stake Engine documentation skill into this game project.

Repository: https://github.com/jordanschock632-spec/stake-engine-docs
Complete documentation ZIP: https://github.com/jordanschock632-spec/stake-engine-docs/releases/download/docs-2026-10-15-checklist/stake-engine-docs.zip
Expected ZIP SHA-256: 0f74779f8927dcd3b290c1d1cbdb53a9c4991b9401ec9be62936d52ba25500ef

Clone the repository into a temporary working directory outside the game project. Inspect install.py, then run `python install.py --project <absolute-path-to-this-game-project>`. The installer downloads the complete ZIP from the public release. No GitHub account, GitHub CLI, Git LFS, or extra Python packages are required. Alternatively, download stake-engine-docs.zip manually and supply --archive <absolute-path-to-ZIP>. GitHub's automatically generated source-code ZIP is not the full documentation archive.

Install the complete archive under .agents/skills/stake-engine-docs/ so all relative references and assets remain intact. Verify the pinned ZIP hash and all 1,232 payload checksums. Do not overwrite an existing skill or change global Codex configuration. No game dependencies are needed. Do not run the archive's capture scripts or documentation examples for installation.

After installation, read SKILL.md, AGENTS.md, index.md, and metadata/user-supplied-checklist-notes.md. Confirm 67 page records and 51 supplied approval-checklist items. Load relevant reference pages when building or reviewing our game, cite local file paths and headings, and distinguish requirements from examples. The archive is a 2026-10-15 snapshot; the formerly restricted checklist was transcribed from three supplied screenshots, with provenance preserved.

Report the installed path, checksum results, and how to invoke $stake-engine-docs. Stop after installation and validation; do not modify game implementation or execute documentation examples.
```
