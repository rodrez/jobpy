import setuptools
from distutils.core import setup

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jobpy", # Replace with your own username
    version="0.0.2",
    author="Fabian Rodriguez",
    author_email="fabian.rodrez@gmail.com",
    description="A package built to facilitate job search and match your skills the best job.",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rodrez/jobpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)