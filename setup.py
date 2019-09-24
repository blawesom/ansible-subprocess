import os
from setuptools import setup


longDesc = ""
if os.path.exists("README.md"):
    longDesc = open("README.md").read().strip()

setup(
    name="ansible-subprocess",
    version="0.4.0",
    author="blawesom",
    author_email="",
    description=("Using Ansible from python subprocess."),
    long_description=longDesc,
    license="MIT License",
    keywords="python Ansible subprocess",
    url="https://github.com/blawesom/ansible-subprocess",
    packages=['ansible_subprocess'],
    package_dir={'ansible_subprocess': 'ansible_subprocess'},
    setup_requires=['wheel'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
