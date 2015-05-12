from setuptools import setup, find_packages, Command
from setuptools.command.test import test
from setuptools.command.install import install

import os, sys, subprocess

class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        raise SystemExit(
            subprocess.call([sys.executable,
                             '-m',
                             'unittest',
                             'discover']))

base_dir = os.path.dirname(os.path.abspath(__file__))

install_requires = ['requests', 'PyYAML']

setup(
    name = "ansible_role_installer",
    version = "0.1",
    description = "Install Ansible roles from Git repositories",
    url = "http://github.com/futurice/ansible_role_installer",
    author = "Jussi Vaihia",
    author_email = "jussi.vaihia@futurice.com",
    packages = ["ansible_role_installer"],
    include_package_data = True,
    keywords = 'ansible role installer',
    license = 'BSD',
    install_requires = install_requires,
    entry_points={
        'console_scripts': [
            'role_install = ansible_role_installer.runner:main',
        ],
    },
    cmdclass = {
        'test': TestCommand,
    },
)
