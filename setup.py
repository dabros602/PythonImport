from setuptools import setup, find_packages

setup(
    name='PythonImport',  # The name of your package
    version='1.0.0',         # The current version
    author='dabros602',
    author_email='tabros602@gmail.com',
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package_name',
    packages=find_packages(),
    install_requires=[]
)
