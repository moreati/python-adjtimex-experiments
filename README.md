# Experimental Python wrappers of POSIX adjtimex(2)

[adjtimex(2)] is a Linux specific libc function that gets and sets clock
statuses, offsets, measurements, statuses, etc. These include the [TAI]
leap second offset known to that host.

The function takes a `struct timex *` which it both reads and populates.

This repositry contains Python wrappers of adjtimex(2), implemented with
different FFI frameworks. So far there is

|  Framework  | Language |      Implementation      |
| ----------- | -------- | ------------------------ |
| [ctypes]    |          | [ctypes_adjtimex.py]     |
| [CFFI]      |          | [cffi_adjtimex/]         |
| [Cython]    |          | [cython_adjtimex/]       |
| [PyO3]      | Rust     | [pyo3_adjtimex/]         |

Each implementation contains a single module, exposing a single function

```pycon
>>> import adjtimex
>>> adjtimex.tai_offset()
(0, 37)
```

`0` is returned by `adjtime(2)`, the clock is synchronised and no leap
seconds are pending.

`37` is read from `timex.tai`, the host knows that [TAI] is 37 seconds
ahead of [UTC].


## TODO

- Add Zig?
- CFFI built by Maturin?
- Port from setuptools -> pyproject.toml?
- Port to BSD? macOS? Windows?
- More in depth writeup
- CPython restricted API?
- PyPy3?
- WASM?


## See also

- https://github.com/moreati/scanwalk different implementations in branches


[adjtimex(2)]: https://www.man7.org/linux/man-pages/man2/adjtimex.2.html
[cffi_adjtimex/]: https://github.com/moreati/python-adjtimex-experiments/tree/main/cffi_adjtimex
[CFFI]: https://cffi.readthedocs.io/en/stable/
[ctypes_adjtimex.py]: https://github.com/moreati/python-adjtimex-experiments/blob/main/ctypes_adjtimex.py
[ctypes]: https://docs.python.org/3/library/ctypes.html
[cython_adjtimex/]: https://github.com/moreati/python-adjtimex-experiments/tree/main/cython_adjtimex
[Cython]: https://cython.readthedocs.io/en/stable/index.html
[pyo3_adjtimex/]: https://github.com/moreati/python-adjtimex-experiments/tree/main/pyo3_adjtimex
[PyO3]: https://pyo3.rs/
[TAI]: https://en.wikipedia.org/wiki/International_Atomic_Time
[UTC]: https://en.wikipedia.org/wiki/Coordinated_Universal_Time
