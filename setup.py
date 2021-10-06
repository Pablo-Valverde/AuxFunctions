import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='AuxFunctions',
    version='0.0.3',
    author='Pablo Valverde',
    description='Functions I usually used at my projects',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Pablo-Valverde/AuxFunctions',
    license='MIT',
    packages=['AuxFunctions'],
)
