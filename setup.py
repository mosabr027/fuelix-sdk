from setuptools import setup, find_packages

setup(
    name='fuelix_sdk',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests'],
    include_package_data=True,
    description='Unofficial SDK for FuelIX API',
    author='Your Name',
    author_email='you@example.com',
    zip_safe=False
)
