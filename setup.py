# code from https://packaging.python.org/tutorials/packaging-projects/ and modified

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OdooApiHandler-pkg-MatéoWatelet",
    version="0.0.1",
    author="Matéo Watelet",
    author_email="mateo.watelet@gmail.com",
    description="little script getting the list of articles of a given odoo db",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux, MacOs",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)