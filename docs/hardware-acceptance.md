# ModuleTwo hardware acceptance record

Status: **partial physical acceptance — setup, polling and diagnostics verified on 2026-11-09; remaining checks pending**.

Tracking: [ha-mygrid-modbus #4](https://github.com/tjorim/ha-mygrid-modbus/issues/4).
Follow the [acceptance checklist](hardware-testing.md). Record observations, timestamps and failures below; a blank or pending result is not a pass.

## Confirmed prerequisite — 2026-11-09

The [library validation issue](https://github.com/tjorim/python-mygrid-modbus/issues/5) is resolved. The [library validation record](https://github.com/tjorim/python-mygrid-modbus/pull/22) documents read-only testing on the replacement battery:

- The owner reports that account linking started battery updates, and selecting Home Assistant control again made Modbus TCP available.
- Software **31.6** is owner-reported. The standard device-identification request returned Illegal Function, so this version was not read over Modbus.
- Register 0 reports map version **2**.
- Both read-only library smoke tests passed; the read-only CLI returned a valid snapshot and raw-register dump. No protocol correction was needed.
- No power or restart commands were sent. Activation persistence and operation without cloud access remain unverified.

These results validate the library prerequisite only.

## Integration test environment

| Field | Value |
| --- | --- |
| Test date/time and timezone | 2026-11-09, 20:21–20:23 UTC (21:21–21:23 Europe/Brussels) |
| Tester | Codex via authenticated Home Assistant REST/WebSocket APIs, owner-provided endpoint |
| Installed integration version and commit | Manifest 0.1.0; HACS update entity reports installed revision `6e4ce48` (not independently verified against installed files) |
| Installed library version | Manifest requirement `mygrid-modbus==0.1.1`; runtime package not independently inspected |
| Home Assistant version | 2026.11.0, Home Assistant OS 18.5, Python 3.14.10, aarch64 |
| Battery software/firmware and source | Pending reconfirmation (owner-reported baseline: Software 31.6) |
| Observed register-map version | 2, reconfirmed in integration diagnostics/register 0 |
| Standalone/cluster and leader role | Pending |
| Control source and competing controllers disconnected | Pending |

Keep network addresses, credentials and unreviewed diagnostics out of published results.

## Integration observations

| Checklist steps | Check | Result and evidence |
| --- | --- | --- |
| 1–2 | Setup, one device, initial setpoint unchanged | Setup loaded successfully; one device, 38 registered entities, 13 enabled. First and subsequent setpoint readings were 0 W. No command actions invoked; no pre-setup setpoint capture, so unchanged initial setpoint is not independently established. |
| 2–3 | SOC, power/sign, limits, stored energy, capacity and lifetime counters compared with app | Live telemetry available: SOC 49%, power 0 W, limits +1200/−800 W, stored energy 2000 Wh, capacity 3978 Wh, lifetime charged/discharged 1446/111 Wh. Status normal, Problem off. App comparison and nonzero power sign remain pending. |
| Connection visibility | Shared Modbus connection | `modbus/connections/list` reports a connected TCP endpoint held by this config entry on unit 1. Owner confirmed it is visible on the Modbus configuration page after refresh. |
| 3 | Cluster energy aggregation scope, if applicable | Pending |
| 4–5 | Explicitly supervised allowed setpoints, readback, measured response and explicit zero | Not performed; requires authorization and supervision |
| 6 | Connectivity loss, unavailable state, polling recovery and no command replay | Pending |
| 7 | Reconfiguration preserves entity IDs/history and permits connection | Pending |
| 8 | Energy dashboard selection and generated statistics | Both lifetime counters expose energy/Wh/total_increasing; recorder lists both IDs with has_sum=true. Actual statistic samples, dashboard selection and behavior remain pending. |
| 9 | Polling changes, reload/unload do not write power; last-consumer connection release | Pending |
| 10 | Optional supervised restart, single command and eventual read recovery | Not performed; requires separate authorization and maintenance window |
| Diagnostics | Download works, decoded telemetry/raw dump agree, identifying fields omitted | HTTP 200; last_update_success=true, battery updated, no failed components/faults, all 18 holding registers returned and consistent with decoded values/scales. Integration payload omits network addresses and entry identity. HA diagnostic wrapper includes other integrations and setup-time entry IDs; do not publish the complete download without review. |

For any control test, record authorization, requested value, fresh limits, readback, measured response, time and final state. Record uncertain command outcomes explicitly; do not automatically retry. Do not induce faults to test diagnostics.

## Discrepancies and completion

Setup, repeated polling and diagnostics succeeded; no discrepancy requiring a code fix was observed in this limited scope. Restart remains disabled by the integration. No power or restart action was invoked. The existing Home Assistant instance retains the configured entry and continues polling; no local HA instance was started. Availability/recovery, reconfiguration, options/unload, physical app comparison and dashboard acceptance remain pending. Optional restart may remain untested if explicitly recorded as such.

After reviewing the physical test evidence, update the README and the [documentation hub](https://github.com/tjorim/custom-mygrid#readme) with the tested versions, scope and remaining limitations. Library reads, simulator tests, hassfest and HACS validation alone do not establish physical-device acceptance.
