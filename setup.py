from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


README = read('README.rst')
CHANGES = read('CHANGES.rst')


setup(
    name = "lesscss-python",
    packages = find_packages(),
    version = "0.3",
    author = "Andrey Fedoseev",
    author_email = "andrey.fedoseev@gmail.com",
    url = "https://github.com/andreyfedoseev/django-less",
    description = "Django template tags to compile LESS into CSS",
    long_description = "\n\n".join([README, CHANGES]),
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = ["less", "css"],
)