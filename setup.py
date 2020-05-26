from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    readme = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='appfollow_api',
    version='1.0.0',
    author='Denis Bondarenko',
    author_email='denis.bondarenko@appfollow.io',
    description='A Python 3.6 wrapper for the AppFollow API',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/AppFollow/appfollow-api-python',
    packages=find_packages(),
    install_reqs=required,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
)
