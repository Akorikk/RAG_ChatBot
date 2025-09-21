#setup.py this will help you to install any kinds of folder as a local package  

from setuptools import setup, find_packages

setup(
    name = "Rag_chatbot",
    version = "0.1.0",
    author="Abhishek Kori",
    author_email="abhishekkori601@gmail.com",
    packages=find_packages(),
    install_requires=[]
)