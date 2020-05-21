import setuptools

with open("jobpy/_version.py") as f:
    __version__ = f.read()

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jobpy", # Replace with your own username
    version=__version__[15:-1], # Grabas the version from _version.py
    author="Fabian Rodriguez",
    license = "MIT",
    author_email="fabian.rodrez@gmail.com",
    description="A package built to facilitate job search and match your skills the best job.",
    long_description= long_description,
    long_description_content_type="text/markdown",
    keywords = ['jobs', 'jobpy', 'job tool'],
    install_requires=[            # I get to this in a second
          'pandas',
          'beautifulsoup4',
          'requests',
      ],
    url="https://github.com/rodrez/jobpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python_requires='>=3.7',
)