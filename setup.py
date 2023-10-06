from setuptools import setup, find_packages

setup(
    name='pydevtools',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pylint',
            'flake8',
        ],
    },
    author='Jeel Dobariya',
    author_email='dobariyaj34@gmail.com',
    description='A collection of utility modules for Python development',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JeelDobariya38/PyDevTools',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
