from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

with open("requirements.txt", "r", encoding="utf-8") as req:
    requires = req.read()

setup(name='spec-reader',
      version='0.1.6',
      description='The spectrum reader',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/ADv0rnik/SpecReader.git',
      author='Alex Dvornik',
      author_email='aadvornik@gmail.com',
      license='MIT',
      keywords="reader spectrum radiation",
      packages=find_packages(),
      package_data={"reader": ['*.spe', 'data/*']},
      install_requires=requires,
      entry_points={
          "console_scripts": ['spec-reader=reader.main:runner']
      },
      zip_safe=False)
