from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: Inactive',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows',
  'Operating System :: POSIX :: Linux',
  'Operating System :: MacOS',
  'License :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='GoogleApiHelper',
  version='0.0.1',
  description='A package with functionalities to help you develop faster code using google apis',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Dulea Mihai-Alexandru',
  author_email='duleasoft@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='api', 
  packages=find_packages(),
  install_requires=[
    'google-api-python-client',
    'google-auth-httplib2',
    'google-auth-oauthlib'
  ] 
)