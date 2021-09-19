from setuptools import setup
import etym_cli.__main__ as m

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as file:
    requires = [line.strip() for line in file.readlines()]

VERSION = m.__version__
DESCRIPTION = "Command-line tool for etymonline with rich output."

setup(
    name="etym-cli",
    version=VERSION,
    url="https://github.com/agmmnn/etym-cli",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="agmmnn",
    classifiers=[
        "Programming Language :: Python :: 3",
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
