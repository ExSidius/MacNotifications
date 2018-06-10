from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'macnotifications',
    packages = ['macnotifications'],
    version = '0.4',
    description = 'MacOS Notifications from within Python.',
    long_description=long_description,
    author = 'Mukul Ram',
    author_email = 'mukul.ram97@gmail.com',
    url = 'https://github.com/ExSidius/MacNotifications',
    download_url = 'https://github.com/ExSidius/MacNotifications/archive/0.1.tar.gz',
    keywords = ['notifications', 'macos'],
    classifiers = [
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
    ],
)
