from setuptools import setup, find_packages

# Get  __version__
exec(open('nbserve/meta.py').read())

requires = ['flask',
            'runipy',
            'ipython[notebook]']
setup(
    name=__progname__,
    version=__version__,
    long_description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    keywords=__keywords__,
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points = {
        'console_scripts': ['nbserve=nbserve.cli:main']
        }
)
