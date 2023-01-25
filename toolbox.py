import numpy as np
import numpy.ma as ma

def lonlat_index(lon_grid, lat_grid, lon_target, lat_target, inc=0.5):
    """
    Find the closet indexes from a coordiantes grid to a point.
    inc should have the magnitude of the grd size
    """

    j1, i1 = ma.where(ma.logical_and(lat_grid < lat_target + inc, lat_grid > lat_target - inc))
    j2 = ma.where(ma.logical_and(lon_grid[j1, i1] < lon_target + inc, lon_grid[j1, i1] > lon_target - inc))[0]
    j_out, i_out = ma.where(ma.logical_and(lat_grid == lat_grid[j1, i1][j2][0], lon_grid == lon_grid[j1, i1][j2][0]))

    return i_out, j_out

def kgs_to_sv(array):
    return array*10**(-9)

