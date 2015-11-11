#!/usr/bin/env python

import sys, platform

try:
    from setuptools import *
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
finally:
    from setuptools import *

from glob import glob

if sys.version_info < (2, 6):
    print >> sys.stderr, "ERROR: ficus requires python 2.6 or greater"
    sys.exit()

import ficus

cmdclass = {}

def main():
    setup(  name = 'ficus',
            version = ficus.__version__,
            description = 'context managers for matplotlib',
            url = 'https://github.com/camillescott/ficus',
            author = 'Camille Scott',
            author_email = 'camille.scott.w@gmail.com',
            license = 'BSD',
            test_suite = 'nose.collector',
            tests_require = ['nose'],
            packages = ['ficus'],
            install_requires = ['nose',
                                #'sphinxcontrib-napoleon',
                                #'Sphinx',
                                'matplotlib',
                                'nose-capturestderr'],
            include_package_data = True,
            zip_safe = False,
            cmdclass = cmdclass  )
        
if __name__ == "__main__":
    main()
