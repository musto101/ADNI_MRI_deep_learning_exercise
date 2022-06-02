import os
import numpy as np
import nibabel as nib
from nibabel.testing import data_path

example_filename = os.path.join(data_path, 'example4d.nii.gz')
#print(example_filename)

img = nib.load(example_filename)
img.shape

img.get_data_dtype() == np.dtype(np.int16)

img.affine.shape

data = img.get_fdata()
data.shape

hdr = img.header
hdr.get_xyzt_units()