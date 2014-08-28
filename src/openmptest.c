#include <Python.h>
#include <stdio.h>
#ifdef _OPENMP
#include <omp.h>
#endif

static PyObject *
omp_test(PyObject *self, PyObject *args)
{
    int th_id, nthreads;
    #pragma omp parallel private(th_id)
    {
    th_id = omp_get_thread_num();
    printf("Hello World from thread %d\n", th_id);
    #pragma omp barrier
    if ( th_id == 0 ) {
        nthreads = omp_get_num_threads();
        printf("There are %d threads\n", nthreads);
    }
    }

    Py_RETURN_NONE;
}

static PyMethodDef OMPTestMethods[] = {
    {"test",  omp_test, METH_VARARGS,
     "Testing printing stuff and OpenMP."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
init_omp(void)
{
    (void) Py_InitModule("_omp", OMPTestMethods);
}
