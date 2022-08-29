from setuptools import setup

setup(
    name="genshinrecipes",
    version="3.0.0",
    author="tilda",
    packages=["genshinrecipes"],
    python_requires=">=3.6",
    package_data={
        "genshinrecipes": ["recipes.json"]
    },
    project_urls={
        "Source": "https://github.com/tilda/genshinrecipes",
    })