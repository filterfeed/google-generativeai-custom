from setuptools import setup, find_packages

setup(
    name="google-generativeai-custom",  # match the name you use after #egg=
    version="0.1.0",
    packages=find_packages(include=['google', 'google.*']),
    install_requires=[],
)
