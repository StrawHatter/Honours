##  Adapted from https://sarvamblog.blogspot.com/2014/08/supervised-classification-with-k-fold.html
##  This program takes in all files whithin the BENIGN DATASET folder which held all the executable files.
##  And then will convert all the files in that directory into images.
##  1301428 - Paul Dreczkowski
##  

import numpy,scipy.misc, os, array

directory = '/Users/Tsubaki/Movies/Proj/BENIGN DATASET/gy'

for file in os.listdir(directory):
    f = open(file,'rb');
    ln = os.path.getsize(file); # length of file in bytes
    width = 256;
    rem = ln%width; 

    a = array.array("B"); # uint8 array
    a.fromfile(f,ln-rem);
    f.close(); 

    g = numpy.reshape(a,(len(a)/width,width));
    g = numpy.uint8(g);
    print (file);
    print (g);
    scipy.misc.imsave(file[:-4] + '.png',g); # save the image
