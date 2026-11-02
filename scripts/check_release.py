"""Validate the public, metadata-only Home Assistant repository."""
from pathlib import Path
import os
import re
import zipfile

root = Path(__file__).resolve().parents[1]
app = root / "remote_home_assistant"
allowed = {
    ".gitignore", ".github/workflows/verify.yaml", "scripts/check_release.py",
    "README.md", "SECURITY.md", "LICENSE-FRP", "THIRD-PARTY-NOTICES.md",
    "repository.yaml", "remote_home_assistant/config.yaml",
    "remote_home_assistant/CHANGELOG.md", "remote_home_assistant/README.md",
    "remote_home_assistant/DOCS.md",
    *(f"remote_home_assistant/translations/{language}.yaml"
      for language in ("en", "pl", "de", "nl", "fr", "sv")),
}
files = {
    path.relative_to(root).as_posix(): path
    for path in root.rglob("*")
    if path.is_file()
    and not {".git", ".cache"}.intersection(path.relative_to(root).parts)
}
if set(files) != allowed:
    raise SystemExit(f"Unexpected or missing public files: {set(files) ^ allowed}")
configuration = (app / "config.yaml").read_text()
match = re.search(r'^version: "(\d+\.\d+\.\d+)"$', configuration, re.M)
if match is None:
    raise SystemExit("Missing app version")
version = match[1]
if not re.search(r'^image: ghcr\.io/remote-ha/homeassistant-addon/agent$', configuration, re.M):
    raise SystemExit("App must use the published multi-architecture image")
if configuration.split("options:\n", 1)[1].split("schema:\n", 1)[0].strip() != 'pairing_token: ""':
    raise SystemExit("Only the pairing token may be configured")
if configuration.split("schema:\n", 1)[1].strip() != "pairing_token: password":
    raise SystemExit("Unexpected app schema")
if not (app / "CHANGELOG.md").read_text().startswith(f"# {version}\n"):
    raise SystemExit("Changelog version differs from app version")
if os.getenv("GITHUB_REF_TYPE") == "tag" and os.environ["GITHUB_REF_NAME"] != "v" + version:
    raise SystemExit("Release tag differs from app version")
for name, path in files.items():
    data = path.read_text()
    if re.search(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", data):
        raise SystemExit(f"Private key in public file: {name}")
output = root / ".cache" / f"remote-ha-app-{version}.zip"
output.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    for name, path in sorted(files.items()):
        archive.write(path, name)
print(f"Validated metadata-only app {version}; archive: {output}")
