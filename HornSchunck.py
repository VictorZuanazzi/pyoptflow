#!/usr/bin/env python
"""
./HornSchunck.py data/box/box
./HornSchunck.py data/office/office
./HornSchunck.py data/rubic/rubic
./HornSchunck.py data/sphere/sphere
"""
# from scipy.ndimage.filters import gaussian_filter
import imageio
from matplotlib.pyplot import show
from argparse import ArgumentParser
from pyoptflow import HornSchunck, getimgfiles
from pyoptflow.plots import compareGraphs
import numpy as np

FILTER = 7


def main():
    p = ArgumentParser(description='Pure Python Horn Schunck Optical Flow')
    p.add_argument('--stem',
                   help='path/stem of files to analyze',
                   default='data/box/')
    p.add_argument('--pat',
                   help='glob pattern of files',
                   default='box*.bmp')
    p = p.parse_args()

    U, V = horn_schunck(p.stem, p.pat)

    show()


def horn_schunck(stem, pat: str):
    flist = getimgfiles(stem, pat)

    for i in range(len(flist)-1):
        fn1 = flist[i]
        im1 = imageio.imread(fn1, as_gray=True)

        im1 = np.flip(im1, 0)

#       Iold = gaussian_filter(Iold,FILTER)

        fn2 = flist[i+1]
        im2 = imageio.imread(fn2, as_gray=True)
        im2 = np.flip(im2, 0)
#        Inew = gaussian_filter(Inew,FILTER)

        U, V = HornSchunck(im1, im2, 1., 100)
        compareGraphs(U, V, im2, fn=fn2.name)

    return U, V


if __name__ == '__main__':
    main()
