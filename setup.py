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

KEYWORDS = ('vagrant')

setuptools.setup(
    name="python-vagrant-metadata",
    version="0.0.5",
    author="LeConTesteur",
    description="Can use and parse metadata information of vagrant box",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeConTesteur/python-vagrant-metadata",
    project_urls={
        "Bug Tracker": "https://github.com/LeConTesteur/python-vagrant-metadata/issues",
    },
    classifiers=[ "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires = requirements,
    tests_require = requirements_tests,
    extras_require = extras,
    keywords=KEYWORDS,
)
