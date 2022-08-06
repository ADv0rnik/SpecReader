![GitHub repo file count](https://img.shields.io/github/directory-file-count/ADv0rnik/SpecReader?style=flat-square)

## SpecReader
### General information
The Spec-reader utility was designed to read spectrum data (in .spe format) from radiation detection device produced by 
ATOMTEX (Belarus) and transform it into spectrogram. The program was tested on data from the following models:
- [AT6101DR Spectrometer](https://atomtex.com/en/at6101dr-spectrometer)
- [AT6101C Spectrometer](https://atomtex.com/en/portable-spectrometers-backpack-based-radiation-detectors-brd/at6101c-at6101cm-spectrometers)

The spec-reader is presented in form of CLI application. Current version of the application is 0.3 beta. Current version includes basic functionality like parser implemented by core.py, plot representation implemented by plot.py, cli basic commands- help, version, plot (see description below) 

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

 
