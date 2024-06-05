from setuptools import find_packages, setup


def read(filename):
    with open(filename, "r") as file:
        return file.read()

setup(
    name="pythonwebui",
    version="1.0.0",
    packages=find_packages(),
    url="https://github.com/RadwanHegazy/pythonwebui",
    license="MIT",
    description="Build your HTML and CSS with ease",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Radwan Hegazy",
    python_requires=">=3.8",
    project_urls={
        "source": "https://github.com/RadwanHegazy/pythonwebui"
    }
)


