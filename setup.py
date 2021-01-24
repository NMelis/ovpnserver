import setuptools
from pathlib import Path

setuptools.setup(
    name="ovpn-server-creator-do",
    version="0.0.1",
    description=('OpenVPN server in Digitalocean', ),
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="MIT",
    maintainer="NMelis",
    author='NMelis',
    url='https://github.com/NMelis/ovpn-server-creator-do',
    install_requires=[
        'python-digitalocean==1.16.0',
        'scp==0.13.3',
        'loguru==0.5.3',
    ],
    entry_points={
        'console_scripts': ['ovpnserver=ovpnserver.main:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries'
    ],
)