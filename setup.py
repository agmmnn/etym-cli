from setuptools import setup, find_packages
import etym_cli

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as file:
    requires = [line.strip() for line in file.readlines()]

VERSION = "0.0.1"
DESCRIPTION = "Command-line tool for etymonline with rich output."

setup(
    name="etym-cli",
    version=VERSION,
    url="https://github.com/agmmnn/etym-cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="agmmnn",
    license="Apache License Version 2.0",
    license_files=["LICENSE"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    packages=["etym_cli"],
    install_requires=requires,
    include_package_data=True,
    package_data={"etym_cli": ["etym_cli/*"]},
    python_requires=">=3.5",
    entry_points={"console_scripts": ["etym = etym_cli.__main__:cli"]},
)
