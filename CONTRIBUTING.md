# Contributing

Change integration behavior and tests here. Change protocol or device behavior in `python-mygrid-modbus`, release it to PyPI, then bump the `mygrid-modbus` pin in `manifest.json` and `pyproject.toml`.

Run the README validation commands before proposing a change. Include a redacted raw-register dump and firmware/map version for decoding issues. Never publish the battery's local address or entry identifiers. The simulator can verify most changes without hardware; clearly distinguish simulation from physical acceptance results.

Use the local manual-install ZIP or publish a HACS custom-repository release for community testing.

## Documentation ownership

Update documentation alongside behavior changes. Keep Python examples, protocol
references, device prerequisites and library validation in the Python library;
keep HA setup, configuration, entities, Energy dashboard instructions, automation
examples and integration acceptance in the HA integration. Cross-device
introductions and website navigation belong in `custom-mygrid`.

The documentation website imports authoritative Markdown at pinned commits.
Edit the original source, not a website snapshot. Preserve existing headings
where possible because published pages may link to their anchors. Use relative
Markdown links for files in this repository. Link to another repository's source
rather than copying its detailed instructions.

After a documentation change merges, the hub's scheduled update workflow proposes
a snapshot refresh. To publish sooner, run that workflow manually or update the
pins with `pnpm docs:update` in `custom-mygrid`. The website changes only after
the snapshot-update PR is reviewed and merged. See the
[website publishing guide](https://tjorim.github.io/custom-mygrid/docs/website/#upstream-documentation-ownership).

## Marketplace presentation

Keep prerequisites, configuration, entities, examples, limitations and
troubleshooting in README.md: Marketplace displays that README directly.
Use `ha-marketplace:exclude-start` / `ha-marketplace:exclude-end` HTML comments
only around repository installation instructions or contributor/development
material. Do not exclude device activation or post-install setup. The website
renders the full README, including sections Marketplace omits.
