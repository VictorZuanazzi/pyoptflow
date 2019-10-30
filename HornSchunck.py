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
from pyoptflow.plots import *
import numpy as np
import os
from tqdm import tqdm as tqdm

FILTER = 7


def main():
    p = ArgumentParser(description='Pure Python Horn Schunck Optical Flow')
    p.add_argument('--stem',
                   help='path/stem of files to analyze',
                   default='data/box/')
    p.add_argument('--pat',
                   help='glob pattern of files',
                   default='box*.bmp')
    p.add_argument('--save_to',
                   default=None,
                   help='path to save the files')
    p.add_argument('--make_gif',
                   action='store_true',
                   help='save flow frames as a gif')
    p = p.parse_args()

    if p.save_to is not None:
        try:
            os.makedirs(p.save_to, exist_ok=True)
        except OSError:
            print(f"Could not create directory {p.save_to}")
    else:
        p.save_to = p.stem

    U, V = horn_schunck(p.stem, p.pat, p.save_to)

    if p.make_gif:
        gif_generator(p.save_to)

    show()


def rgb2gray(img):
    """from rgb to gray conversion"""
    if len(img.shape) == 2:
        # image already is in gray scale
        return img

    if len(img.shape) > 3:
        # Not RGB image, just ignore the other channels!
        img = img[0:3]

    return np.average(img, weights=[0.299, 0.587, 0.114], axis=2)


def horn_schunck(stem, pat: str, save_to: str):
    flist = getimgfiles(stem, pat)

    for i in tqdm(range(len(flist)-1), ncols=100, desc="HS flow"):
        fn1 = flist[i]
        im1 = imageio.imread(fn1, as_gray=False)

        im1 = np.flip(im1, 0)

        fn2 = flist[i+1]
        im2 = imageio.imread(fn2, as_gray=False)
        im2 = np.flip(im2, 0)

        U, V = HornSchunck(rgb2gray(im1), rgb2gray(im2), 1., 100)

        path = save_to + "/" + fn2.name
        compareGraphs(U, V, im2, fn=fn2.name, save=path)

    return U, V


if __name__ == '__main__':
    main()
