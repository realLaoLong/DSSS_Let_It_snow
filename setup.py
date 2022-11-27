from setuptools import setup

setup(
   name='snowflake',
   version='1.0.0',
   author='Salomo Isheim',
   url='https://github.com/realLaoLong/DSSS_Let_It_snow.git',
   license='LICENSE.md',
   description='An awesome package for drawing colorful snowflakes with turtle',
   long_description=open('README.md').read(),
   install_requires=[
       "numpy >= 1.23.5"
   ],
)