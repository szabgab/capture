from distutils.core import setup, Extension

setup(
    name         = 'capture-cli',
    version      = '0.01',
    author       = 'Gabor Szabo',
    author_email = 'gabor@szabgab.com',
    description  = 'Capture stdout and/or stderr',
    license      = 'MIT',
    keywords     = 'capture stdout stderr write read',
    packages     = [
        'capturecli',
    ],
)


