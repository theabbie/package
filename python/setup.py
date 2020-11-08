import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="package",
    version="1.0.0",
    description="Package Description",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://theabbie.github.io",
    author="TheAbbie",
    author_email="abhishek7gg7@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["package"],
    include_package_data=True,
    install_requires=[
        "importlib_resources"
    ],
    entry_points={"console_scripts": ["package=package.__main__:main"]},
)
