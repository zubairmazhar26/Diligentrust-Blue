from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in comp_diligentrust/__init__.py
from comp_diligentrust import __version__ as version

setup(
	name="comp_diligentrust",
	version=version,
	description="Contain Blue Theme For Company DiligenTrust",
	author="Muhammad Zubair form Diligentrust",
	author_email="zubairmazhar23@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
