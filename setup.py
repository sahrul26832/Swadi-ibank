import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    
    name='swasdi',
    version='22.6.3',
    description='AsiaCI corntibute Service',
    author='Jirapong Choochua',
    author_email='khoonjc@gmail.com',
    url='https://asiaci.co.th',
    packages=find_packages(exclude=['venv']),
    # package_dir={'bMisc': 'bSpace'},
    install_requires = [
        'mysqlclient',
        'passlib',
        'python-dateutil'
    ],
    include_package_data=True,
    zip_safe=True,
    long_description=read('README.md'),
    license='ACI',
    keywords='kaen',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ACI License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)