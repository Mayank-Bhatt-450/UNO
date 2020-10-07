from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    console=['test.py'],
    options = {"build_exe": {
            "icon": ""
        },
               'py2exe': {'bundle_files': 1, 'compressed': True}},
    
    zipfile = None,
)
