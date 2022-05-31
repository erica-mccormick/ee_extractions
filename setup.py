import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()

setup(
    name="waterpyk",
    version="1.1.7",
    description="Extract hydrological data for a lat/long or USGS gauge ID and make simple plots.",
    long_description=README,
    long_description_content_type="text/x-rst",
    #url="https://github.com/realpython/reader",
    author="Erica L. McCormick",
    author_email="erica.elmstead@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),  # Required
    include_package_data= True,
    package_data={'': ['layers_data/*.csv']}
)