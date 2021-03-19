from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='FaucetPy',
	version='0.2.1',
	description='FaucetPay + Python = FaucetPy',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/HanzHaxors/FaucetPy',
	author='HanzHaxors',
	author_email='hanzhaxors@gmail.com',
	license='BSD 2-clause',
	packages=['FaucetPy'],
	install_requires=[
		'requests==2.25.1'
	],
	classifiers=[
		'License :: OSI Approved :: BSD License',
	        'Operating System :: POSIX :: Linux',
		'Intended Audience :: Developers',
		'Intended Audience :: Financial and Insurance Industry'
	]
)
