import imageio.v3 as iio
filenames = ['IMG_1607.jpeg', 'IMG_1612.jpeg','IMG_1613.jpeg']
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('me.gif', images, duration = 500, loop = 0)