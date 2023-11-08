from setuptools import setup

setup(
    name='Github Custom CLI',
    version='0.1',
    py_modules=['my_module'],
    entry_points={
        'console_scripts': [
            'gh2do = main:main',
        ],
    },
)