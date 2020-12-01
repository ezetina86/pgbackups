from setuptools import find_packages, setup

with open('README.md','r') as f:
    long_description = f.read()

setup(
    name ='pgbackup',
    version = '0.1.0',
    author = 'Enrique Zetina',
    author_email = 'jenzetin@gmail.com',
    decription = 'A utility for backing up PostreSQL databases.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url='http://x.com'
    packages = find_packages('src')
)    
