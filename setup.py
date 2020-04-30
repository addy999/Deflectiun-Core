import os,sys
from setuptools import setup

setup(name='deflectiun_core',
      version='0.1',
      description='https://github.com/addy999/Deflectiun-Core',
      url='',
      author='Addy Bhatia',
      author_email='jude.addy999@gmail.com',
      license='MIT',
      install_requires=['numpy', 'shapely'],
      packages=['deflectiun_core'], 
      include_package_data=True,
      zip_safe=True)
