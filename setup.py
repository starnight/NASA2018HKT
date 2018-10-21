from setuptools import setup

setup(
    name='lightwonder-api',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)