     
from setuptools import setup, find_packages

# Installation requirements needed absolutely for the program to run
# prometheus_api_client используется последней версии из master
install_requires = [
    "fastapi==0.110.0",
]

# Additional feature sets and their requirements
extras_require = {
    "dev": [
        "flake8-black",
        "markdown-toc",
        "matplotlib",
    ]
}


def read_file(fname):
    with open(fname, "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="webapp",
    version="0.1.0",
    author="Evgeny Basov",
    author_email="Evgen.Basov@x5.ru",
    description="Anomaly Detection in Time-Series",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github...",
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={"console_scripts": ["webapp=webapp.main:main"]},
    python_requires=">=3.9.*",
)
