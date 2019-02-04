from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
from setuptools import setup, find_packages

pfile = Project(chdir=False).parsed_pipfile

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='appfollow_api',
    version='0.0.1',
    author='Denis Bondarenko',
    author_email='denis.bondarenko@appfollow.io',
    description='A Python 3.6 wrapper for the AppFollow API',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/AppFollow/appfollow-api-python',
    packages=find_packages(),
    install_requires=convert_deps_to_pip(pfile['packages'], r=False),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
)
