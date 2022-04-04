from setuptools import setup

setup(
    name="genshinrecipes",
    version="2.6.0",
    author="tilda",
    author_email="tda@stairway.cf",
    packages=["genshinrecipes"],
    python_requires=">=3.6",
    package_data={
        "genshinrecipes": ["recipes.json"]
    },
    url="https://github.com/tilda/genshin-recipe-data"
)