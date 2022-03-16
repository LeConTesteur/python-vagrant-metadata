import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    "packaging",
    "dataclasses-json",
    "requests"
]

requirements_tests = [
    "requests_mock",
    "flake8",
    "coverage"
]

extras = {
    'tests': requirements_tests,
}

setuptools.setup(
    name="python-vagrant-metadata",
    version="0.0.1",
    author="LeConTesteur",
    description="Can use and parse metadata information of vagrant box",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeConTesteur/python-vagrant-metadata",
    project_urls={
        "Bug Tracker": "https://github.com/LeConTesteur/python-vagrant-metadata/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires = requirements,
    tests_require = requirements_tests,
    extras_require = extras,

)
