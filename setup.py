# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='clg',
    version='0.3',
    author='François Ménabé',
    author_email='francois.menabe@gmail.com',
    url='https://clg.readthedocs.org/en/latest/',
    download_url='https://github.com/fmenabe/python-clg',
    license=open('LICENSE').read(),
    description='Command-line generator from a dictionary.',
    long_description=open('README').read(),
    classifiers=[
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ],
    py_modules=['clg'],
    install_requires=['argparse',]
)
