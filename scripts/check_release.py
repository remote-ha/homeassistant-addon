"""Validate the public, metadata-only Home Assistant repository."""
from pathlib import Path
import os
import re
import struct
import zipfile

root = Path(__file__).resolve().parents[1]
app = root / "remote_home_assistant"
allowed = {
    ".gitignore", ".github/workflows/verify.yaml", "scripts/check_release.py",
    "README.md", "INSTALL_WITH_AI.md", "SECURITY.md", "LICENSE", "THIRD-PARTY-NOTICES.md",
    "third_party/licenses/FRP-Apache-2.0.txt", "third_party/licenses/Go-BSD-3-Clause.txt",
    "repository.yaml", "remote_home_assistant/config.yaml",
    "remote_home_assistant/CHANGELOG.md", "remote_home_assistant/README.md",
    "remote_home_assistant/DOCS.md", "remote_home_assistant/icon.png",
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
for document in (root / "README.md", app / "README.md", app / "DOCS.md"):
    if document.read_text().splitlines()[0] != f"# Remote Home Assistant {version}":
        raise SystemExit(f"Documentation version differs: {document.name}")
if re.findall(r"^# (\d+\.\d+\.\d+)$", (app / "CHANGELOG.md").read_text(), re.M) != [version]:
    raise SystemExit("Changelog must describe only the current release")
if "Proprietary Software" not in (root / "LICENSE").read_text():
    raise SystemExit("Missing product ownership notice")
for name, path in files.items():
    data = path.read_bytes()
    if name == "remote_home_assistant/icon.png":
        if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR" or len(data) < 33:
            raise SystemExit("App icon must be a PNG image")
        width, height = struct.unpack(">II", data[16:24])
        if width != height or width < 128:
            raise SystemExit("App icon must be square and at least 128px")
    if re.search(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", data):
        raise SystemExit(f"Private key in public file: {name}")
output = root / ".cache" / f"remote-ha-app-{version}.zip"
output.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    for name, path in sorted(files.items()):
        archive.write(path, name)
print(f"Validated metadata-only app {version}; archive: {output}")
