I've been trying to debug a C extension that should be using OpenMP
but doesn't seem to be doing so. So I put this together as a
simple test of whether OpenMP is supported and used on a given system.

To use, make sure you have Python 2 and [pytest](http://pytest.org)
installed, then try running `python setup.py test`.
If OpenMP is working you should see output like:

```
============================ test session starts ============================
platform darwin -- Python 2.7.8 -- py-1.4.22 -- pytest-2.6.0
collected 1 items

test/test_omp.py Hello World from thread 1
Hello World from thread 3
Hello World from thread 0
Hello World from thread 2
There are 4 threads
.

========================= 1 passed in 0.06 seconds ==========================
```

Mac Note: The default `gcc` compiler on Macs is actually Apple's `clang`
compiler, which does not support OpenMP. For this to work on a Mac you'll
need to install GNU's `gcc` (e.g. with Homebrew) and set the `CC`
environment variable to point to it.
For my computer I do `CC=gcc-4.9`.
