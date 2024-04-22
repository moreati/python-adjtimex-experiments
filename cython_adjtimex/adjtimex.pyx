
from cpython.exc cimport PyErr_SetFromErrno
from posix.time cimport timeval


cdef extern from "<sys/timex.h>":
    const int ADJ_OFFSET
    const int ADJ_FREQUENCY
    const int ADJ_MAXERROR
    const int ADJ_ESTERROR
    const int ADJ_STATUS
    const int ADJ_TIMECONST
    const int ADJ_SETOFFSET
    const int ADJ_MICRO
    const int ADJ_NANO
    const int ADJ_TAI
    const int ADJ_TICK
    const int ADJ_OFFSET_SINGLESHOT
    const int ADJ_OFFSET_SS_READ
    const int ADJ_OFFSET_SS_READ

    const int STA_PLL
    const int STA_PPSFREQ
    const int STA_PPSTIME
    const int STA_FLL
    const int STA_INS
    const int STA_DEL
    const int STA_UNSYNC
    const int STA_FREQHOLD
    const int STA_PPSSIGNAL
    const int STA_PPSJITTER
    const int STA_PPSWANDER
    const int STA_PPSERROR
    const int STA_CLOCKERR
    const int STA_NANO
    const int STA_MODE
    const int STA_CLK

    const int TIME_OK
    const int TIME_INS
    const int TIME_DEL
    const int TIME_OOP
    const int TIME_WAIT
    const int TIME_ERROR

    struct timex:
        int     modes;
        long    offset;
        long    freq;
        long    maxerror;
        long    esterror;
        int     status;
        long    constant;
        long    precision;
        long    tolerance;
        timeval time;
        long    tick;
        long    ppsfreq;
        long    jitter;
        int     shift;
        long    stabil;
        long    jitcnt;
        long    calcnt;
        long    errcnt;
        long    stbcnt;
        int     tai;

    int adjtimex(timex *);
    int ntp_adjtime(timex *);


def tai_offset():
    cdef timex buf = timex(
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        timeval(0, 0),
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    )
    cdef int status = adjtimex(&buf)
    if status < 0:
        PyErr_SetFromErrno(OSError)
    return status, buf.tai
