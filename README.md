# Image-Steganography
DSP Assignment

## Submitted by Ananya Nair, EC5A.

## Image Steganography
  Steganography is the method of hiding secret data in any image/audio/video. 

## LSB Method
Steps:
  1: The cover image and secret images are converted to 256x256 pixel greyscale image and then converted into numpy arrays.
  2: The last 4 binary digits (i.e LSBs) are masked to store the MSBs of secret image.
  3: The last 4 binary digits of the secret image are also hidden, and the first 4 digits are then shifted right.
  4: The last 4 binary digits of secret image and first 4 binary digits of cover image are merged together.
  5: The resultant numpy array is then converted to an image.

## References

1. [Steganography: Hiding an image inside another](https://towardsdatascience.com/steganography-hiding-an-image-inside-another-77ca66b2acb1)
2. [Image based Steganography using Python](https://www.geeksforgeeks.org/image-based-steganography-using-python/)

  


