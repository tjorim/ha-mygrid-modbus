# Protocol reference

The authoritative [ModuleTwo register reference](https://github.com/tjorim/python-mygrid-modbus/blob/main/docs/protocol.md)
is maintained with the Python library. It covers register addresses, scaling,
signed values, word order, status handling and command semantics. Update that
source when protocol behavior changes; do not maintain another register table
in this integration.

The website also publishes the [protocol reference](https://tjorim.github.io/custom-mygrid/docs/moduletwo-protocol/)
from a reviewed library revision.

## Faults

Use the library's [fault-bit reference](https://github.com/tjorim/python-mygrid-modbus/blob/main/docs/protocol.md#faults).
Integration-specific entity behavior remains in the [setup guide](../README.md#entities).
