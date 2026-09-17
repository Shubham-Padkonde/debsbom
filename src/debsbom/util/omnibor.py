# Copyright (C) 2026 Siemens
#
# SPDX-License-Identifier: MIT

from pathlib import Path

from .gitoid import gitoid_hash


def omnibor_artifact_id(artifact: Path) -> str:
    """
    Calculate the omnibor artifact ID for the given artifact.

    The artifact should be in uncompressed form as otherwise we depend
    on the compression algorithms reproducability guarantees.
    """
    digest = gitoid_hash(artifact)
    return f"gitoid:blob:sha256:{digest}"
