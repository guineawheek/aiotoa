import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    reqs = f.read().splitlines()

setuptools.setup(
    name="aiotoa",
    version="0.0.1",
    author="guineawheek",
    author_email="guineawheek@gmail.com",
    license="MIT",
    description="a lib for the orange alliance (TOA) apiv3 using asyncio/aiohttp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guineawheek/aiotoa",
    packages=setuptools.find_packages(),
    install_requires=reqs,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
