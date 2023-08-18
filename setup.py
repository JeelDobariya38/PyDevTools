from setuptools import setup, find_packages

setup(
    name='Pyutils',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    license='MIT',
    author='Jeel Dobariya',
    description='A collection of utility modules for Python development',
    url='https://github.com/JeelDobariya38/Pyutils'
)
