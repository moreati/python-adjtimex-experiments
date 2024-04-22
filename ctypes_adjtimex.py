import ctypes

try:
    from ctypes import c_time_t
except ImportError:
    if ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_int64):
        c_time_t = ctypes.c_int64
    else:
        ctypes.c_int32

class timeval(ctypes.Structure):
    _fields_ = [
        ('tv_sec',      c_time_t),  # ctypes.c_time_t in Python >= 3.12
        ('tv_usec',     ctypes.c_long),
    ]


class timex(ctypes.Structure):
    _fields_ = [
        ('modes',       ctypes.c_int),
        ('offset',      ctypes.c_long),
        ('freq',        ctypes.c_long),
        ('maxerror',    ctypes.c_long),
        ('esterror',    ctypes.c_long),
        ('status',      ctypes.c_int),
        ('constant',    ctypes.c_long),
        ('precision',   ctypes.c_long),
        ('tolerance',   ctypes.c_long),
        ('time',        timeval),
        ('tick',        ctypes.c_long),
        ('ppsfreq',     ctypes.c_long),
        ('jitter',      ctypes.c_long),
        ('shift',       ctypes.c_int),
        ('stabil',      ctypes.c_long),
        ('jitcnt',      ctypes.c_long),
        ('calcnt',      ctypes.c_long),
        ('errcnt',      ctypes.c_long),
        ('stbcnt',      ctypes.c_long),
        ('tai',         ctypes.c_int),
    ]

libc = ctypes.CDLL('libc.so.6')
t = timex()
state = libc.adjtimex(ctypes.byref(t))
print(state)
print(f'{t.freq=} {t.tai=}')
