from PIL import Image
import numpy as np
# import matplotlib.pyplot as plt

# %matplotlib inline


ascii_index = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def get_img_ready(path):
  img = Image.open(path)
  img.show()
  img.resize((50,50))
  print("Image dimensions : ",img.size)
  img_arr = np.array(img)
  print("Dimension of pixels : ",img_arr.shape)
  return img_arr
def rgb_bright(pix):
    return sum(pix)//3
def min_max(pix):
    return (max(pix)+min(pix))//2
def luminosity(pix):
    return round(0.21*pix[0] + 0.72*pix[1] + 0.07*pix[2])

def get_brightness_matrix(img_arr,cat):
  brightness_mat = []
  if cat=="brightness":
      formula = rgb_bright
  elif cat =="luminosity":
      formula = luminosity
  else:
      formula = min_max
  for row in img_arr:
    brightness_row = []
    for pixel in row:
      brightness_row.append(formula(pixel))
    brightness_mat.append(brightness_row)
  brightness_mat  = np.array(brightness_mat)
  return brightness_mat
def get_ascii_mat(img_mat):
  ascii_mat = []
  for row in img_mat:
    ascii_row = []
    for  brightness_val in row:
      ascii_row.append(ascii_index[brightness_val//5])
    ascii_mat.append(ascii_row)
  return ascii_mat

img_arr = get_img_ready("C:\\Users\\dell\\Downloads\\tux.jpg")

brightness_mat = get_brightness_matrix(img_arr,"brightness")
ascii_mat = get_ascii_mat(brightness_mat)

for i in ascii_mat:
  print("".join(i))