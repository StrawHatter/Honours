## Same script adapted from the one mentioned in convert_all.py but will just take the file used as an argument in Terminal. 
## 1301428 - Paul Dreczkowski
## 
##

import numpy,scipy.misc, os, array, sys, argparse
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
image_path=sys.argv[1]
filename = dir_path +'/' +image_path
f = open(filename,'rb');
ln = os.path.getsize(filename); # length of file in bytes
width = 256;
rem = ln%width; 

a = array.array("B"); # uint8 array
a.fromfile(f,ln-rem);
f.close(); 

g = numpy.reshape(a,(len(a)/width,width));
g = numpy.uint8(g);
print (g);
scipy.misc.imsave(filename[:-4] +'.png',g); # save the image
