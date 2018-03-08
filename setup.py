#!/usr/bin/env python

import sys, platform, os

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

__version__ = open(os.path.join('ficus', 'VERSION')).read().strip()

cmdclass = {}

def main():
    setup(  name = 'ficus',
            version = __version__,
            description = 'context managers for matplotlib',
            url = 'https://github.com/camillescott/ficus',
            author = 'Camille Scott',
            author_email = 'camille.scott.w@gmail.com',
            license = 'BSD',
            tests_require = ['pytest', 'pytest-runner'],
            packages = ['ficus'],
            setup_requires = ['pytest-runner', 'pytest'],
            install_requires = ['nose>=1.3.4',
                                'matplotlib>=1.4'],
            include_package_data = True,
            zip_safe = False,
            cmdclass = cmdclass  )
        
if __name__ == "__main__":
    main()
