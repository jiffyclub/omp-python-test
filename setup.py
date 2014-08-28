import sys

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args or '-s')
        sys.exit(errno)


setup(
    name='omp',
    version='0.1dev',
    packages=find_packages(),
    ext_modules=[
        Extension(
            'omp._omp',
            sources=['src/openmptest.c'],
            extra_compile_args=['-fopenmp'],
            extra_link_args=['-lgomp'])],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
