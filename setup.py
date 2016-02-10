from os.path import join, dirname
from setuptools import setup, find_packages

__version__ = open(join(dirname(__file__), 'slackbot/VERSION')).read().strip()

install_requires = (
    'requests>=2.4.0',
    'websocket-client>=0.22.0',
    'slacker>=0.5.5',
    'six>=1.10.0'
) # yapf: disable

excludes = (
    '*test*',
    '*local_settings*',
) # yapf: disable

setup(name='marvin',
      version=__version__,
      license='BSD',
      description='A sarcastically useful bot',
      author='Jamie Houston',
      author_email='foresterh@gmail.com',
      url='http://github.com/foresterh/slackbot',
      platforms=['Any'],
      packages=find_packages(exclude=excludes),
      install_requires=install_requires,
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5'])
