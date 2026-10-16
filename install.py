"""Install the verified Stake Engine docs as a project-local skill. Python 3.9+."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import os
import stat
import tempfile
import urllib.request
import zipfile

ARCHIVE_SHA256 = '0f74779f8927dcd3b290c1d1cbdb53a9c4991b9401ec9be62936d52ba25500ef'
DOWNLOAD_URL = 'https://github.com/jordanschock632-spec/stake-engine-docs/releases/download/docs-2026-10-15-checklist/stake-engine-docs.zip'
PREFIX = 'stake-engine-docs/'


def digest_file(path):
    digest = hashlib.sha256()
    with path.open('rb') as incoming:
        for chunk in iter(lambda: incoming.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def install(archive, project):
    archive = archive.expanduser().resolve()
    project = project.expanduser().resolve()
    if not project.is_dir():
        raise ValueError('Choose an existing game project directory.')
    destination = project / '.agents' / 'skills' / 'stake-engine-docs'
    if destination.exists():
        raise FileExistsError('Skill already exists; no files overwritten: ' + str(destination))
    if digest_file(archive) != ARCHIVE_SHA256:
        raise ValueError('Archive SHA-256 differs from the pinned verified release.')
    with zipfile.ZipFile(archive) as source:
        if source.testzip() is not None:
            raise ValueError('Archive CRC validation failed.')
        members = source.infolist()
        names = [member.filename for member in members]
        if len(names) != len(set(names)):
            raise ValueError('Duplicate archive paths.')
        for member in members:
            path = PurePosixPath(member.filename)
            if (not member.filename.startswith(PREFIX) or path.is_absolute()
                    or '..' in path.parts or '\\' in member.filename
                    or stat.S_ISLNK(member.external_attr >> 16)):
                raise ValueError('Unsafe ZIP path: ' + member.filename)
        expected = {}
        for line in source.read(PREFIX + 'metadata/checksums.sha256').decode('utf-8').splitlines():
            checksum, relative = line.split('  ', 1)
            expected[relative] = checksum
        payload = {name[len(PREFIX):] for name in names
                   if not name.endswith('/') and name != PREFIX + 'metadata/checksums.sha256'}
        if set(expected) != payload:
            raise ValueError('Checksum inventory does not match archive contents.')
        for relative, checksum in expected.items():
            if hashlib.sha256(source.read(PREFIX + relative)).hexdigest() != checksum:
                raise ValueError('File checksum failed: ' + relative)
        parent = destination.parent
        parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='.stake-engine-docs-install-', dir=parent) as temporary:
            staging = Path(temporary).resolve()
            if staging.parent != parent.resolve():
                raise ValueError('Unexpected staging location.')
            source.extractall(staging)
            skill = staging / 'stake-engine-docs'
            if not (skill / 'SKILL.md').is_file():
                raise ValueError('SKILL.md missing.')
            for relative, checksum in expected.items():
                if digest_file(skill / relative) != checksum:
                    raise ValueError('Extracted file mismatch: ' + relative)
            os.rename(skill, destination)
    return {'installed_to': str(destination), 'verified_files': len(expected),
            'scope': 'project-local', 'archive_sha256': ARCHIVE_SHA256,
            'next': 'Read SKILL.md and index.md, then invoke $stake-engine-docs.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, required=True, help='Existing game project directory')
    parser.add_argument('--archive', type=Path, help='Optional already-downloaded stake-engine-docs.zip')
    args = parser.parse_args()
    if not args.project.expanduser().is_dir():
        parser.error('--project must name an existing directory')
    if args.archive:
        result = install(args.archive, args.project)
    else:
        with tempfile.TemporaryDirectory(prefix='stake-engine-docs-download-') as temporary:
            archive = Path(temporary) / 'stake-engine-docs.zip'
            request = urllib.request.Request(DOWNLOAD_URL, headers={'User-Agent': 'Stake-Engine-Docs-Installer'})
            print('Downloading the verified documentation archive...', flush=True)
            with urllib.request.urlopen(request, timeout=60) as incoming, archive.open('wb') as output:
                for chunk in iter(lambda: incoming.read(1024 * 1024), b''):
                    output.write(chunk)
            result = install(archive, args.project)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
