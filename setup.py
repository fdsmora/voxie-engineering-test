import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="project",
    version="1.0.0",
    url="https://github.com/fdsmora/voxie-engineering-test",
    license="BSD",
    maintainer="Fausto Salazar",
    maintainer_email="fausto.ds.mora@gmail.com",
    description="voxie engineering test in python",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "coverage"]},
)
