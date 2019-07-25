from setuptools import setup, find_packages

def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()

setup(
    name='graphish',
    version='1.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package to search & delete emails using Microsoft Graph API',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('./requirements.txt'),
    keywords=['graph', 'microsoft', 'office365', 'email', 'ediscovery', 'phish', 'phishing', 'swimlane'],
    url='https://github.com/swimlane/graphish',
    author='Swimlane',
    author_email='info@swimlane.com',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4'
)