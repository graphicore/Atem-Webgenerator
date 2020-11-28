import os
from setuptools import setup

# Read the contents of the README file
with open('README.md') as f:
    long_description = f.read()

setup(
    name="Atem-Webgenerator",
    use_scm_version={"write_to": "Lib/webgenerator/_version.py"},
    url='https://github.com/graphicore/atem-webgenerator',
    description='Atem Project: static site generator written in Python based on Frozen-Flask.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=('Lasse Fister',),
    author_email='commander@graphicore.com',
    package_dir={'': 'Lib'},
    packages=['webgenerator'],
    package_data={
                  'webgenerator': [
                      'templates/*',
                  ]
                 },
    entry_points={
        'console_scripts': ['webgenerator=webgenerator.cli:main'],
    },
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    setup_requires=['setuptools_scm'],
    # Dependencies needed for gftools qa.
    install_requires=[
        'setuptools',
        'Flask',
        'Frozen-Flask',
        'houdini.py',
        'misaka',
        'Pygments',
        'PyYAML',
        'pytz',
        ]
    )
