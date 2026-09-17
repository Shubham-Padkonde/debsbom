# Copyright (C) 2026 Siemens
#
# SPDX-License-Identifier: MIT

from hashlib import sha256
import os
from pathlib import Path


def omnibor_artifact_id(artifact: Path) -> str:
    """
    Calculate the omnibor artifact ID for the given artifact.

    The artifact should be in uncompressed form as otherwise we depend
    on the compression algorithms reproducability guarantees.
    """

    hasher = sha256()
    with open(artifact, "rb") as f:
        size = os.fstat(f.fileno()).st_size

        hasher.update(f"blob {size}\0".encode("ascii"))
        while True:
            data = f.read()
            if not data:
                break
            hasher.update(data)

    digest = hasher.hexdigest()
    return f"gitoid:blob:sha256:{digest}"
