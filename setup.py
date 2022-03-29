from setuptools import setup

setup(
    name='mergepdfs',
    version='0.1.0',
    py_modules=['mergepdfs'],
    install_requires=[
        'Click', 'PyPDF2'
    ],
    entry_points={
        'console_scripts': [
            'mergepdfs = mergepdfs:cli',
            ],
        },
)
