#!/usr/bin/env python

import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(HERE, 'README.md')).read()
CHANGES = open(os.path.join(HERE, 'CHANGES.md')).read()

test_requires = ['factory-boy']

setup(
    name='django-template-model',
    version=open(os.path.join(HERE, 'template_model', 'VERSION.md')).read().strip(),
    include_package_data=True,
    author="Makina Corpus",
    author_email="terralego-pypi@makina-corpus.com",
    description='Template model.',
    long_description=README + '\n\n' + CHANGES,
    description_content_type="text/markdown",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url='https://github.com/Terralego/django-template-model',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
    ],
    install_requires=[
        'Django>=2.2',
    ],
    test_requires=test_requires,
    extras_require={
        'dev': [
            'flake8',
            'coverage',
            'codecov',
        ] + test_requires
    },
)
