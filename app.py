#!/usr/bin/env python3
# Packed application loader; source compression is reversible and is NOT cryptographic protection.
import base64 as _packed_b64, zlib as _packed_zlib
from pathlib import Path as _packed_Path
_payload = (_packed_Path(__file__).resolve().parent / "core.pkg").read_bytes()
exec(compile(_packed_zlib.decompress(_packed_b64.b85decode(_payload)), __file__, "exec"), globals())
