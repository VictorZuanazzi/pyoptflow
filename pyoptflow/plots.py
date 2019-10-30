from matplotlib.pyplot import figure, draw, pause, gca, imsave, savefig
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import imageio


def plotderiv(fx, fy, ft):

    fg = figure(figsize=(18, 5))
    ax = fg.subplots(1, 3)

    for f, a, t in zip((fx, fy, ft), ax, ('$f_x$', '$f_y$', '$f_t$')):
        h = a.imshow(f, cmap='bwr')
        a.set_title(t)
        fg.colorbar(h, ax=a)


def compareGraphs(u, v, Inew, scale: int = 3, quivstep: int = 5, fn: Path = None, save: str = None):
    """
    makes quiver
    input:
    u, v: np.array(Inew.shape), x and y coordinates of the dense optical flow.
    Inew: np.array(), image where optical flow was computed.
    scale: int, scale of the quiver arrows.
    quivstep: int, grid spacing for the quiver in pixels. Same spacing is used in x and y.
    fn: str, title of the image. If None, image is not titled.
    save: str, path to save the image. If None, image is not saved.
    """

    ax = figure().gca()
    ax.imshow(Inew,  cmap='gray', origin='lower')

    # downsamples u and v
    U = u[::quivstep, ::quivstep]
    V = v[::quivstep, ::quivstep]

    # creates the original X and Y coordinates
    X = np.zeros(U.shape) + np.arange(0, u.shape[0], quivstep)
    Y = (np.zeros(U.T.shape) + np.arange(0, u.shape[1], quivstep)).T

    # plot frame
    ax.quiver(X, Y, U, V)

    if fn:
        ax.set_title(fn)

    draw()

    if save is not None:
        plt.savefig(fname=save+".png")


def compareGraphsLK(imgOld, imgNew, POI, V, scale=1., fn: Path = None):

    ax = gca()
    ax.imshow(imgNew, cmap='gray', origin='lower')
    # plt.scatter(POI[:,0,1],POI[:,0,0])
    for i in range(len(POI)):
        ax.arrow(POI[i, 0, 1], POI[i, 0, 0],
                 V[i, 1]*scale, V[i, 0]*scale,
                 color='red')
    # plt.arrow(POI[:,0,0],POI[:,0,1],0,-5)
    if fn:
        ax.set_title(fn)

    draw()
    pause(0.5)
