from setuptools import setup, find_packages

def readme():
  with open('README.md') as f:
    return f.read()

setup(name='pyqwave',
      version='0.1.0',
      description='Toolkit for Quantum wave propagations',    
      long_description=readme(),  
      author='Daniel & Miguel A Sepulveda',
      license='Unknown',
      packages=['pyqwave'],
      install_requires=['matplotlib', 
                        'numpy',
                        'Pillow',
                        'pyquaternion',
                        'uuid',
                        'nose',
                        'pyYAML',
                        'scipy',
                        ],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
)
