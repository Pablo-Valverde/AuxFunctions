import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='auxfunctions',
    version='0.0.0',
    author='Pablo Valverde',
    description='Functions I usually used at my projects',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Pablo-Valverde/auxfunctions',
    license='GNU AGPLv3',
)
