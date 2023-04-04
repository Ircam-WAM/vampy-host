import os
from setuptools import setup, find_packages, Extension

sdkdir = 'vamp-plugin-sdk/src/vamp-hostsdk/'
vpydir = 'native/'

sdkfiles = [ 'Files', 'PluginBufferingAdapter', 'PluginChannelAdapter',
             'PluginHostAdapter', 'PluginInputDomainAdapter', 'PluginLoader',
             'PluginSummarisingAdapter', 'PluginWrapper', 'RealTime' ]
vpyfiles = [ 'PyPluginObject', 'PyRealTime', 'VectorConversion', 'vampyhost' ]

srcfiles = [
    sdkdir + f + '.cpp' for f in sdkfiles
] + [
    vpydir + f + '.cpp' for f in vpyfiles
]

def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

class get_numpy_include(object):
    """Defer numpy.get_include() until after numpy is installed."""

    def __str__(self):
        import numpy
        return numpy.get_include()

def get_extension():
    vampyhost = Extension('vampyhost',
                      sources = srcfiles,
                      define_macros = [ ('_USE_MATH_DEFINES', 1) ],
                      include_dirs = [ 'vamp-plugin-sdk', get_numpy_include() ])
    return vampyhost

setup (name = 'vamp',
       version = '1.1.0',
       url = 'https://code.soundsoftware.ac.uk/projects/vampy-host',
       description = 'Use Vamp plugins for audio feature analysis.',
       long_description = ( read('README.rst') + '\n\n' + read('COPYING.rst') ),
       license = 'MIT',
       packages = find_packages(exclude = [ '*test*' ]),
       ext_modules = [get_extension() ],
       requires = [ 'numpy' ],
       setup_requires=["numpy"],  # Just numpy here
       install_requires=["numpy"],  # Add any of your other dependencies here
       author = 'Chris Cannam, George Fazekas',
       author_email = 'cannam@all-day-breakfast.com',
       classifiers = [
           'Development Status :: 4 - Beta',
           'Intended Audience :: Science/Research',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: MIT License',
           'Operating System :: MacOS :: MacOS X',
           'Operating System :: Microsoft :: Windows',
           'Operating System :: POSIX',
           'Programming Language :: Python',
           'Programming Language :: Python :: 2',
           'Programming Language :: Python :: 3',
           'Topic :: Multimedia :: Sound/Audio :: Analysis'
           ]
       )
