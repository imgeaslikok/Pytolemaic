import os

from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))
setup_reqs = []

with open(os.path.join(this_dir, 'requirements.txt'), 'r') as fp:
    install_reqs = [r.rstrip() for r in fp.readlines() if
                    not r.startswith(('#', 'git+'))]

from pytolemaic.version import version

setup(
    name='pytolemaic',
    author='Orion Talmi',
    author_email='otalmi@gmail.com',
    description='',
    version=str(version),
    packages=find_packages(exclude=['tests', 'scripts', 'examples']),
    setup_requires=setup_reqs,
    install_requires=install_reqs,
    # test_suite='nose.collector', #TODO: replace nose with unittest
    include_package_data=True,
    platforms=['Linux'],
    python_requires='>=3.6.*',
    url='',
)
