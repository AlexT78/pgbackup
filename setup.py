from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='alexT78',
    author='alexandre.tamavond@gmail.com',
    description='a utility for backing PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AlexT78/pgbackup',
    packages=find_packages('src')
)