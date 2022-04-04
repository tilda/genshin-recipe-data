from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name="genshinrecipes",
    version="2.6.0",
    author="tilda",
    author_email="tda@stairway.cf",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["genshinrecipes"],
    python_requires=">=3.6",
    package_data={
        "genshinrecipes": ["recipes.json"]
    },
    url="https://github.com/tilda/genshin-recipe-data"
)