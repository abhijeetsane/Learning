from distutils.core import setup
from distutils.extension import Extension

setup(name="PackageName",
    ext_modules=[
        Extension("hello", ["hellomodule.cpp"],
        include_dirs=['/usr/local/include'],
        libraries = ["boost_python37"])
    ])
