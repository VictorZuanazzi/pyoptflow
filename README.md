[![image](https://zenodo.org/badge/DOI/10.5281/zenodo.1043971.svg)](https://doi.org/10.5281/zenodo.1043971)

[![image](https://travis-ci.org/scivision/pyoptflow.svg?branch=master)](https://travis-ci.org/scivision/pyoptflow)
[![image](https://coveralls.io/repos/github/scivision/pyoptflow/badge.svg?branch=master)](https://coveralls.io/github/scivision/pyoptflow?branch=master)
[![image](https://ci.appveyor.com/api/projects/status/9iv32q84vd3gbdde?svg=true)](https://ci.appveyor.com/project/scivision/pyoptflow)
[![Maintainability](https://api.codeclimate.com/v1/badges/b7a550fa1d50af8491d3/maintainability)](https://codeclimate.com/github/scivision/pyoptflow/maintainability)
[![Python versions (PyPI)](https://img.shields.io/pypi/pyversions/pyoptflow.svg)](https://pypi.python.org/pypi/pyoptflow)
[![PyPi Download stats](http://pepy.tech/badge/pyoptflow)](http://pepy.tech/project/pyoptflow)

Credits: Original implementation forked from [scivision](https://github.com/scivision/pyoptflow)

# Optical Flow: Horn-Schunck

Python implementation of optical flow estimation using only the Scipy stack for:

* Horn Schunck

The implementation of Lucas-Kanade is not currently working, colaboration on that is welcome. 

## Install

```sh
python -m pip install -e .
```

optionally, to run self-tests:

```sh
python -m pip install -e .[tests]

pytest -v
```

## Examples

The program scripts expect `directory` `glob pattern`

[imageio](https://imageio.github.io/) loads a wide varity of images *and* video.

### Box

    python HornSchunck.py

### Office

all time steps:

    python HornSchunck.py --stem data/office --pat office*.bmp
   
![](https://github.com/VictorZuanazzi/pyoptflow/blob/master/data/office_out/flow.gif)

or just the first 2 time steps:

    python HornSchunck.py --stem data/office --pat office.[0-2].bmp

### Rubic

    python HornSchunck.py --stem data/rubic --pat rubic*.bmp
    
![](https://github.com/VictorZuanazzi/pyoptflow/blob/master/data/rubic_out/flow.gif)

### Sphere

    python HornSchunck.py --stem data/sphere --pat sphere*.bmp
    
![](https://github.com/VictorZuanazzi/pyoptflow/blob/master/data/sphere_out/flow.gif)

## Compare: Matlab Computer Vision toolbox

In `Matlab` directory, similar method in Octave and a comparison plot using Matlab Computer Vision toolbox.

## Reference

[Inspiration](https://github.com/ablarry91/Optical-Flow-LucasKanade-HornSchunck/)
