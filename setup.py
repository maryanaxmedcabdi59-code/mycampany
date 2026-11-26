from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mycampany/__init__.py
from mycampany import __version__ as version

setup(
	name="mycampany",
	version=version,
	description="campany",
	author="Hilal Ahmed",
	author_email="hilal@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
