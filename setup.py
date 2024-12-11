from setuptools import setup, find_packages

setup(
    name="meow-pip",
    version="0.1.0",
    author="Peter Wagner",
    author_email="1559510+thepwagner@users.noreply.github.com",
    description="A brief description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thepwagner-org/meow-pip",
    packages=find_packages(exclude=["*/test_*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 