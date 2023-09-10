from PIL import Image
from Steganography import Steg

final = Steg.steganography()
#convert numpy array to CASA image
new_img = Image.fromarray(final)
new_img.show()
