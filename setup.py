#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from itertools import chain
from setuptools import setup, find_packages
import pathlib

prj_root = pathlib.Path(__file__).parent

def file_contents(relpath):
  src_path = prj_root/relpath
  if src_path.exists():
    with src_path.open('r') as in_stream:
      return in_stream.read()
  else:
    return ''

def file_populated_lines(relpath):
  return [line for line in map(str.strip, file_contents(relpath).splitlines()) if line]

  requirements_lines = {k: file_populated_lines(relpath)
                            for k, relpath in [('install', 'requirements.txt'), 
                                               ('dev', 'requirements_dev.txt')]}
  
  requirements = {k: [l for l in lines if ('git+' not in l) and \
                      not any(l.startswith(prefix) for prefix in ['http://', 'https://'])]
                  for k, lines in requirements_lines.items()}
  
  dependency_links = sorted({l.strip().replace('git+', '')
                             for l in chain.from_iterable(requirements_lines.values())
                             if l.startswith('git+')})
  
  setup(
    author="Claudia Wallis",
    author_email='<built-in method replace of str object at 0x7fa9b272fb28>',
    classifiers=[
      'Development Status :: 2 - Pre-Alpha',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
    ],
    description='Functions for everyday use in ml projects',
    install_requires=requirements['install'],
    long_description=file_contents('README.rst') + '\n\n' + file_contents('HISTORY.rst'),
    include_package_data=True,
    keywords='ml_helpers',
    name='ml_helpers',
    packages=find_packages(include=['ml_helpers*']),
    setup_requires=[],
    test_suite='tests',
    tests_require=requirements['dev'],
    dependency_links=dependency_links,
    url='https://github.source.internal.cba/gds/ml_helpers',
    version='0.0.1',
    zip_safe=False,
  ) 
