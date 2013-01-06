#!/usr/bin/env python
"""
flask-gae_runtools
-----------------------

Flask extension for working with the App Engine sdk.

Links
`````

* `documentation <http://packages.python.org/flask-gae_runtools>`_
* `development version
  <http://github.com/gregorynicholas/flask-gae_runtools/zipball/master#egg=flask_gae_runtools-dev>`_

"""
from setuptools import setup

setup(
  name='flask-gae_runtools',
  version='1.0.0',
  url='http://github.com/gregorynicholas/flask-gae_runtools',
  license='MIT',
  author='gregorynicholas',
  description='Flask extension for working with the App Engine sdk.',
  long_description=__doc__,
  py_modules=['gae_runtools'],
  # packages=['flaskext'],
  # namespace_packages=['flaskext'],
  include_package_data=False,
  data_files=[],
  zip_safe=False,
  platforms='any',
  install_requires=[
    'flask'
  ],
  test_suite='gae_runtools_tests',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ]
)
