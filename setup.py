# -*- coding: utf-8 -*-

"""PathMe Viewer setup.py."""

import codecs
import os
import re

import setuptools

MODULE = 'pathme_viewer'
PACKAGES = setuptools.find_packages(where='src')
META_PATH = os.path.join('src', MODULE, '__init__.py')
KEYWORDS = ['Pathways', 'Systems Biology', 'Networks Biology', 'Visualization']
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Scientific/Engineering :: Bio-Informatics'
]
INSTALL_REQUIRES = [
    'pandas',
    'tqdm',
    'numpy',
    'compath',
    'rdflib',
    'rdflib-jsonld',
    'requests',
    'bio2bel',
    'bio2bel_chebi',
    'bio2bel_hgnc',
    'pybel',
    'pybel_tools',
    'pathme',
]
EXTRAS_REQUIRE = {
    'web': [
        'flask',
        'flask_admin',
    ],
    'docs': [
        'sphinx',
        'sphinx-rtd-theme',
        'sphinx-click',
    ],
}

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """Build an absolute path from *parts* and return the contents of the resulting file. Assume UTF-8 encoding."""
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """Extract __*meta*__ from META_FILE."""
    meta_match = re.search(
        r'^__{meta}__ = ["\']([^"\']*)["\']'.format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError('Unable to find __{meta}__ string'.format(meta=meta))


def get_long_description():
    """Get the long_description from the README.rst file. Assume UTF-8 encoding."""
    with codecs.open(os.path.join(HERE, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


if __name__ == '__main__':
    setuptools.setup(
        name=find_meta('title'),
        version=find_meta('version'),
        description=find_meta('description'),
        long_description=get_long_description(),
        url=find_meta('url'),
        author=find_meta('author'),
        author_email=find_meta('email'),
        maintainer=find_meta('author'),
        maintainer_email=find_meta('email'),
        license=find_meta('license'),
        classifiers=CLASSIFIERS,
        keywords=KEYWORDS,
        packages=PACKAGES,
        package_dir={'': 'src'},
        include_package_data=True,
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE
    )
