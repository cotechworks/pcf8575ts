from setuptools import setup


def get_requirements_from_file():
    with open("./requirements.txt") as f_in:
        requirements = f_in.read().splitlines()
    return requirements


setup(
    name="pcf8575ts",
    version="1.0",
    author="cotechworks",
    author_email="cotechworks63@gmail.com",
    description="Library for PCF8575TS, an 16port I2C I/O Expander",
    package_dir={"": "src"},
    install_requires=get_requirements_from_file()
)