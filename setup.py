from setuptools import setup, find_packages

setup(
    name="CD",
    version="1.0.0",
    py_modules=["CD"],
    install_requires=[
        "pyfiglet",
    ],
    author="NeverStopTheCoder",
    description="A terminal ASCII engine that supports inline multi-color and formatting tags.",
)
