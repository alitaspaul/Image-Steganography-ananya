import numypy as np
from PIL import Image

class Steg:
  #Image Steganogrpahy using LSB method
  def stegnaography():
    #convert cover image to grayscale
    img1 = Image.open("image1.jpg")
    grey_img1 = np.array(img1.convert('L'))

      #convert the secret image to greyscale
    img2 = Image.open("secret.jpg")
    grey_img2 = np.array(img2.convert('L'))

    #embedded image
    new = np.zeros(grey_img2.size)
    new.shape = (256,256)

      #remove 4 lsb in cover image
    for i in range(256):
      for j in range(256):
        grey_img1[i][j] = grey_img1[i][j] & 240

    #padding zeros to secret image by shifting right
    for i in range(256):
      for j in range(256):
        if len(np.binary_repr(grey_img2[i][j])) == 7:
          grey_img2[i][j] = grey_img2[i][j] >> 3
        if len(np.binary_repr(grey_img2[i][j])) == 8:
          grey_img2[i][j] = grey_img2[i][j] >> 4

    #merging msb of cover and secret image
    for i in range(256):
      for j in range(256):
        new[i][j] = grey_img1[i][j] + grey_img2[i][j]
    new = new.astype(int)
    return new

  #reversing the image
  def decode():
    final = Steg.steganography()
    for i in range (256):
      for j in range (256):
        final[i][j] = final[i][j] & 15
        final[i][j] = final[i][j] << 4 
  return final
