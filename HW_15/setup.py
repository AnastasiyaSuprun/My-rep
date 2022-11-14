from os import path
from setuptools import setup
from setuptools import find_namespace_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

setup(
    name='fibonacci',
    version='1.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AnastasiyaSuprun/My_rep',
    author='Anastasiya',
    author_email='suprun.anastasiya.work@gmail.com',
    package_dir={' ': 'src'},
    packages=find_namespace_packages(where='src'),
    python_requires='>=3.6',
)
