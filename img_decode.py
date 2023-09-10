from PIL import Image
from Steganography import Steg

final = Steg.decode()
new_img = Image.fromarray(final)
new_img.show()
