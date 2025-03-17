import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "kivy_garden", "simpletablelayout", "readme.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="kivy-garden.simpletablelayout", 
    version="0.1",
    author="Kivy",
    author_email="kivy@kivy.org",
    description="Simple Table Layout – Layout simile a una tabella HTML che supporta rowspan e colspan, integrato in Kivy Garden.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tungsteno74/garden.simpletablelayout", 
    packages=find_packages(),
    namespace_packages=["kivy_garden"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: User Interfaces",
    ],
    python_requires=">=3.0",
    install_requires=["kivy>=2.0.0"],
)
