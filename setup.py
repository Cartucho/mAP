import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mean_average_precision",
    version="0.0.1",
    author="Peter Siemen",
    author_email="mail@petersiemen.net",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/petersiemen/mAP",
    packages=setuptools.find_packages(exclude=['tests', 'main.py']),  # include all packages under src
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        'numpy',
    ]
)
