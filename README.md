![GitHub repo file count](https://img.shields.io/github/directory-file-count/ADv0rnik/SpecReader?style=flat-square) ![GitHub language count](https://img.shields.io/github/languages/count/ADv0rnik/SpecReader?style=flat-square) ![Tests](https://github.com/ADv0rnik/SpecReader/actions/workflows/tests.yml/badge.svg) ![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/ADv0rnik/SpecReader?style=flat-square) [![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3100/)

## SpecReader
### General information
The Spec-reader utility was designed to read spectrum data (in .spe format) from radiation detection devices and transform it into a human-readable format (.csv). The program was tested on data from GammaVision v.7.01 and detectors produced by ATOMTEX Inc. (Belarus). 

The following models were used for testing:
- [AT6101DR Spectrometer](https://atomtex.com/en/at6101dr-spectrometer)
- [AT6101C Spectrometer](https://atomtex.com/en/portable-spectrometers-backpack-based-radiation-detectors-brd/at6101c-at6101cm-spectrometers)

The spec-reader is presented as a CLI application. The current version of the application is [0.2.2](https://github.com/ADv0rnik/SpecReader/tree/v.0.2.2). This version includes basic functionality such as:

- A parser implemented in data_parser.py
- Basic CLI commands: help, version, out and format (see description below)

### Requirements

The spec-reader requires Python version 3.10 or older. For Windows users, the oldest Python interpreter can be found
here: http://www.python.org (http://www.python.org/). While Python is typically pre-installed on Ubuntu Linux, you might want to update it.
If so, follow these [steps](https://www.debugpoint.com/install-python-3-12-ubuntu/)

The list of packages required for Spec-Reader is presented in `requirements.txt`

```commandline
art
pandas
pytest
matplotlib
numpy
```

### Installation 
The Spec-Reader has been tested on Windows 11, macOS, and Ubuntu 20.04. You can install it on your machine in two ways:
- Extract all files from the "reader" directory (the root) to your local machine; 
- Install the package from [PyPi test repo](https://test.pypi.org/project/spec-reader/).

1 - Clone the github repo with all files and subdirectories to a local directory:
```commandline
git clone https://github.com/ADv0rnik/SpecReader.git
```
or
```commandline
git clone git@github.com:ADv0rnik/SpecReader.git
```

2 - Open a terminal or command prompt in the directory where you extracted the Spec-Reader files. Create and activate a virtual environment:

     for UNIX-based systems:
       python -m venv venv
       source venv/bin/activate
     for Windows:    
       python -m venv venv
       C:\><venv>\Scripts\activate

3 - Install requirements: 

    pip install -r requirements.txt`

To install the Spec-Reader package from the PyPI Test repository, use the following command::

```commandline
pip install -i https://test.pypi.org/simple/ spec-reader==0.2.2
```


#### Possible issues during installation:
If the requirements installation does not run automatically, make sure that all required packages are installed in your virtual environment.

In this case, you can trigger the installation manually by using the following command:

```commandline
pip install <package name>
```

### Usage

To run Spec-Reader run CLI command `spec-reader`. The following options are available:

`usage: spec-reader [-h] [-v] path`

* `path` - is a mandatory argument (path to spectrum file to be treated) 
* `-h, --help` - show help
* `-v, --version` - show application's version
* `-o, --out` - specify the name for the output file. If name is not specified the default filename will be applied
* `-f, --format` - specify the format of the input files (*.spe or *.Spe). *.Spe is using by default

The CLI command can be combined with `-f` or `-o` flags. For example:

`spec-reader c:\20240925\ -f Spe -o cs_data`

Example of program workflow is presented below

```commandline
____ ___  ____ ____    ____ ____ ____ ___  ____ ____ 
[__  |__] |___ |       |__/ |___ |__| |  \ |___ |__/ 
___] |    |___ |___    |  \ |___ |  | |__/ |___ |  \ 
                                                     

[+] Run program
usage: spec-src [-h] [-v] [-o OUT] [-f FORMAT] path
spec-src: error: the following arguments are required: path
```

### Outputs

The Spec-Reader provides data about spectra in .csv format. The latest version of the Spec-Reader package can be downloaded from test.pypi.org by using the following command:

`pip install -i https://test.pypi.org/simple/ spec-reader==0.2.2`
