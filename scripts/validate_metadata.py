"""Validate the HACS package metadata and its dependency pins."""

import ast
import json
import tomllib
from importlib.metadata import distribution
from pathlib import Path

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = ROOT / "custom_components/mygrid_modbus"


def validate_transport_pins(dev: list[str], upstream: list[str]) -> None:
    """Require the test transport pins to match Home Assistant exactly."""
    local = {canonicalize_name(req.name): req for req in map(Requirement, dev)}
    core = {canonicalize_name(req.name): req for req in map(Requirement, upstream)}
    for name in ("modbus-connection", "tmodbus", "pymodbus"):
        if name not in core or name not in local:
            msg = f"Missing shared transport requirement: {name}"
            raise ValueError(msg)
        if (
            local[name].specifier != core[name].specifier
            or local[name].extras != core[name].extras
        ):
            msg = f"Transport pin differs from installed Home Assistant: {local[name]} != {core[name]}"
            raise ValueError(msg)


def main() -> None:
    """Validate the package metadata, library pin and import boundaries."""
    core_manifest = distribution("homeassistant").locate_file(
        "homeassistant/components/modbus/manifest.json"
    )
    upstream = json.loads(core_manifest.read_text())["requirements"]
    manifest = json.loads((COMPONENT / "manifest.json").read_text())
    project = tomllib.loads((ROOT / "pyproject.toml").read_text())
    validate_transport_pins(project["dependency-groups"]["dev"], upstream)
    assert list(manifest) == [
        "domain",
        "name",
        *sorted(set(manifest) - {"domain", "name"}),
    ]
    assert manifest["domain"] == "mygrid_modbus"
    assert manifest["version"] == project["project"]["version"] == "0.1.0"
    assert manifest["requirements"] == ["mygrid-modbus==0.1.1"]
    assert manifest["requirements"][0] in project["dependency-groups"]["dev"]
    assert manifest["dependencies"] == ["modbus"]
    assert manifest["config_flow"]
    assert manifest["iot_class"] == "local_polling"
    assert "quality_scale" not in manifest
    assert json.loads((COMPONENT / "strings.json").read_text()) == json.loads(
        (COMPONENT / "translations/en.json").read_text()
    )
    for path in COMPONENT.glob("*.py"):
        for node in ast.walk(ast.parse(path.read_text())):
            if isinstance(node, ast.ImportFrom):
                module = node.module or ""
                assert not module.startswith(
                    (
                        "pymodbus",
                        "tmodbus",
                        "modbus_connection.tmodbus",
                        "modbus_connection.pymodbus",
                    )
                ), path
    print("HACS metadata, library pin, and transport import boundaries validated.")


if __name__ == "__main__":
    main()
