import pydatagovph

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=pydatagovph.__app_name__,
    version=pydatagovph.__version__,
    description=pydatagovph.__description__,
    author=pydatagovph.__author__,
    author_email=pydatagovph.__author_email__,
    packages=['pydatagovph'],
    install_requires=['requests==2.0.1'],
    url=pydatagovph.__app_url__,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'License :: Freeware',
    ),
    download_url=pydatagovph.__download_url__,
)