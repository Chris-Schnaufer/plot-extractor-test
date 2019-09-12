#!/usr/bin/env python

"""Extractor algorithm implementation file
"""

import numpy as np

def calculate_canopycover_masked(pxarray):
    """Return greenness percentage of given numpy array of pixels.

    Args:
      pxarray (numpy array): rgb image

    Return:
      (float): greenness percentage
    """

    # For masked images, all nonzero pixels are considered canopy
    nonzeros = np.count_nonzero(pxarray)
    ratio = nonzeros/float(pxarray.size)
    # Scale ratio from 0-1 to 0-100
    ratio *= 100.0

    return ratio

def calculate(pxarray):
    """Algorithm
    Args:
        pxarray(numpy array): RGB pixel data at the plot level
    Returns:
        The calculated greenness ratio
    """
    return calculate_canopycover_masked(np.rollaxis(pxarray, 0, 3))
