from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="blurplefier-standalone",
    version="0.0.8",
    description="A standalone version of the blurplefier that the Blurplefier bot has.",
    license="MIT",
    long_description=long_description,
    author="Project Blurple, Astrea49",
    url="https://github.com/Astrea49/blurplefier-standalone",
    packages=["blurplefier"],
    install_requires=["pillow"],
    python_requires=">=3.8.0",
)
