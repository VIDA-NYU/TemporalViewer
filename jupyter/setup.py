from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="model-viewer",
    version="0.1.2",
    author="Sonia Castelo",
    author_email="s.castelo@nyu.edu",
    description="Model Viewer. Enables the exploration of temporal distribution of the model outputs in Jupyter Notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soniacq/TemporalViewer",
    packages=find_packages(exclude=['js', 'node_modules']),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "python-dateutil",
        "numpy",
        "notebook",
        "pandas"
    ]
)
