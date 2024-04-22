use errno;
use libc;
use pyo3::prelude::*;

#[pyfunction]
fn tai_offset() -> PyResult<(i32, i32)> {
    let mut buf: libc::timex = libc::timex{
        modes:0, offset:0, freq:0, maxerror:0, esterror:0,
        status:0, constant:0, precision:0, tolerance:0, 
        time:libc::timeval{tv_sec:0,tv_usec:0},
        tick:0, ppsfreq:0, jitter:0, shift:0, stabil:0,
        jitcnt:0, calcnt:0, errcnt:0, stbcnt:0, tai:0,
        __unused1:0, __unused2:0, __unused3:0, __unused4:0, __unused5:0,
        __unused6:0, __unused7:0, __unused8:0, __unused9:0, __unused10:0,
        __unused11:0,
    };
    let buf_ptr: *mut libc::timex = &mut buf;
    let status = unsafe { libc::adjtimex(buf_ptr) };
    errno::set_errno(errno::Errno(0));
    if status < 0 {
        panic!("Error: status={} errno={}", status, errno::errno());
    };
    Ok((status, buf.tai))
}

/// A Python module implemented in Rust.
#[pymodule]
fn adjtimex(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(tai_offset, m)?)?;
    Ok(())
}
