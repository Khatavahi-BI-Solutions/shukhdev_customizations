from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in shukhdev_customizations/__init__.py
from shukhdev_customizations import __version__ as version

setup(
	name="shukhdev_customizations",
	version=version,
	description="Shukhdev Customizations",
	author="Jigar Tarpara",
	author_email="jigartarpara@khatavahi.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
