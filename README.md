![GitHub repo file count](https://img.shields.io/github/directory-file-count/ADv0rnik/SpecReader?style=flat-square) ![GitHub language count](https://img.shields.io/github/languages/count/ADv0rnik/SpecReader?style=flat-square)![Tests](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject/actions/workflows/tests.yml/badge.svg)

## SpecReader
### General information
The Spec-reader utility was designed to read spectrum data (in .spe format) from radiation detection device produced by 
ATOMTEX (Belarus) and transform it into spectrogram. The program was tested on data from the following models:
- [AT6101DR Spectrometer](https://atomtex.com/en/at6101dr-spectrometer)
- [AT6101C Spectrometer](https://atomtex.com/en/portable-spectrometers-backpack-based-radiation-detectors-brd/at6101c-at6101cm-spectrometers)

The spec-reader is presented in form of CLI application. Current version of the application is 0.1.7. Current version includes basic functionality like parser implemented by core.py, plot representation implemented by plot.py, cli basic commands - help, version, plot (see description below) 

### Requirements

The spec-reader require Python version 3.8 or older. For Windows users the oldest version of python interpreter can be found
here [http://www.python.org](http://www.python.org.). Python interpreter is usually pre-installed on Ubuntu Linux. However,
you may want to update it. In this case use the following [guideline](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/)

The list of packages required for Spec-Reader is presented in `requirements.txt`

`art`
`pandas`
`pytest`
`matplotlib`
`tqdm`

### Installation 
The Spec-Reader has been tested on Windows and UNIX-based systems (Ubuntu v.20.04).
There are two ways to install the program on your machine: 1 - by extracting all files from "reader" directory (the root)
to your local machine; 2 - install package from [PyPi test repo](https://test.pypi.org/project/spec-reader/).

1 - Extract root directory of script with all files and subdirectories to a local directory

2 - Run terminal. Install and activate virtual environment:

     for UNIX-based systems:
       python -m venv venv
       source venv/bin/activate
     for Windows:    
       python -m venv venv
       C:\><venv>\Scripts\activate

3 - Install requirements: 

    pip install -r requirements.txt`

To install Spec-Reader package form PyPi Test repo use the following command:

`pip install -i https://test.pypi.org/simple/ spec-reader==0.1.6`

Possible issues during the installation:
If requirements installation won't run automatically make sure that all required packages are installed in your virtual env.
In this case you may trigger the installation manually by using the following command:

`pip install <package name>`

### Usage

To run Spec-Reader run CLI command `spec-reader`. The following options are available:

`usage: spec-reader [-h] [-v] [-p] path`

* `path` - is a mandatory argument (path to spectrum file to be treated) 
* `-h, --help` - show help
* `-v, --version` - show application's version
* `-p, --plot` - make plot from data


