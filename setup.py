from distutils.core import setup, Extension

setup(
    name         = 'capture',
    version      = '0.1',
    author       = 'Gabor Szabo',
    author_email = 'gabor@szabgab.com',
    description  = 'Capture stdout and/or stderr',
    license      = 'MIT',
    keywords     = 'capture stdout stderr write read',
    packages     = [
        'capture',
    ],
)


