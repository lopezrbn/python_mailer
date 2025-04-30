from setuptools import setup, find_packages

setup(
    name="python_mailer",  # Name of the package (to be used with `pip install`)
    version="0.1",
    description="Package to send emails in a Python script",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Rubén López",
    author_email="lopezrbn@gmail.com",
    url="https://github.com/lopezrbn/python_mailer",  # URL to the package repository
    license="MIT",
    packages=find_packages(),  # Find all packages in the current directory
    install_requires=[],  # Dependencies can be added here if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the minimum Python version required
)