import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cssow-drussell1974", # Replace with your own username
    version=os.environ['CSSOWMODEL_APP__VERSION'],
    author="Dave Russell",
    author_email="dave@daverussell.co.uk",
    description="Computer Science SOW - Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drussell1974/cssow",
    packages=setuptools.find_packages(),
    classifiers=[   
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
