try:
    from setuptools import setup
    from setuptools import find_packages

    packages = find_packages()
except ImportError:
    from distutils.core import setup
    import os

    packages = [
        x.strip("./").replace("/", ".")
        for x in os.popen('find -name "__init__.py" | xargs -n1 dirname')
        .read()
        .strip()
        .split("\n")
    ]

setup(
    name="hacrs",
    version="0.0.1",
    python_requires=">=3.7",
    packages=packages,
    install_requires=[
        'flask',
        'flask_login',
        'gunicorn',
        'psycopg2',
        'boto',
        'boto3',
        'pystache'
    ],
)
