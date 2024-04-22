from __future__ import annotations

import os

import _adjtimex


def tai_offset() -> tuple[int, int]:
    with _adjtimex.ffi.new('struct timex *buf') as buf:
        status = _adjtimex.lib.adjtimex(buf)
        if status < 0:
            OSError(_adjtimex.ffi.errno, os.strerror(_adjtimex.ffi.errno))
        return status, buf.tai


__all__ = [
    tai_offset.__name__,
]