from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from os.path import isfile, join
import os
import numpy, cv2

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

mypath = r"C:/Users/cocoslabs/Desktop/adil aug/"
onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
images = numpy.empty(len(onlyfiles), dtype=object)
os.mkdir("C:/Users/cocoslabs/Desktop/New1")
for n in range(0, len(onlyfiles)):
    images[n] = cv2.imread(join(mypath, onlyfiles[n]))
    os.mkdir("C:/Users/cocoslabs/Desktop/New1/" + "img%d" % n)
    path1 = os.getcwd()
    Folder_name = "C:/Users/cocoslabs/Desktop/New1/" + "img%d" % n
    Extension = ".jpg"

    img = images[n]
    x = img_to_array(img)
    # creating a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # converting to a Numpy array with shape (1, 3, 150, 150)
    # os.makedirs('preview')
    i = 0

    for batch in datagen.flow(x, save_to_dir=Folder_name, save_prefix='-%d' % n, save_format=".jpg"):
        i += 1
        if i > 36:
            break