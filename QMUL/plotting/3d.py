import rasterio
from mayavi import mlab
from tvtk.api import tvtk
import numpy as np


# Use gadalwarp or qgis to reproject to utm 17N
filenames = ['be.tif', 'raw.tif']
outnames = ['be.png', 'raw.png']

for i in range(2):

    dataset = rasterio.open(filenames[i])

    surface = dataset.read()[0]
    dataset.close()

    # Get rid of any nodata values
    surface[surface == np.min(surface)] = np.nan

    mlab.figure(size=(640, 640), bgcolor=(1., 1., 1.))

    surf = mlab.surf(surface, colormap='gist_earth', warp_scale=1)

    mlab.savefig(outnames[i])
    mlab.clf()
