from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(name='spec-reader',
      version='0.3',
      description='The spectrum reader',
      long_description=long_description,
      url='https://github.com/ADv0rnik/SpecReader.git',
      author='Aliaksandr Dvornik',
      author_email='aadvornik@gmail.com',
      license='MIT',
      keywords="reader spectrum",
      packages=find_packages(exclude=['tests*']),
      include_package_data=True,
      install_requires=['matplotlib', 'pandas', 'art'],
      package_data={
          "sample": ['sample.spe']
      },
      entry_points={
            "console_scripts": ['sreader=main.py']
      },
      zip_safe=False)
