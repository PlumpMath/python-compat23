from setuptools import setup
from os.path import join, dirname


def _get_readme():
    with open(join(dirname(__file__), 'README.rst')) as f:
        return f.read()


setup(name='compat23',
      version='0.2a1',
      packages=['compat23'],
      author='Ian Denhardt',
      author_email='ian@zenhack.net',
      description='python 2/3 compatibiltiy library',
      long_description=_get_readme(),
      license='MIT',
      url='https://github.com/zenhack/python-compat23',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Topic :: Software Development :: Libraries',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.0',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ])
