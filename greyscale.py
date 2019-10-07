import cv2
import os.path
from PIL import Image
from cv2 import copyMakeBorder as make_border 

def greyscale(filename):
	extension = os.path.splitext(filename)[1][1:]
	image = cv2.imread('image.' + extension, 0)
	cv2.imwrite('output_img.' + extension, image)

def squarefit(filename):
	extension = os.path.splitext(filename)[1][1:]
	image = Image.open('image.' + extension)
	im_read = cv2.imread('image.' + extension)
	#color = [101, 52, 152] #FOR PURPLE BORDER
	#color = [0, 0, 0] #FOR BLACK BORDER
	color = [256, 256, 256] #FOR WHITE BORDER
	w, h = image.size
	if w > h:
		padding = (w - h)/2
		top, btm, lft, rgt = padding, padding, 0, 0
		border_img = make_border(im_read, top, btm, lft, rgt, cv2.BORDER_CONSTANT, value = color)
		cv2.imwrite('output_img.' + extension, border_img)
	elif h > w:
		padding = (h - w)/2
		top, btm, lft, rgt = 0, 0, padding, padding
		border_img = make_border(im_read, top, btm, lft, rgt, cv2.BORDER_CONSTANT, value = color)
		cv2.imwrite('output_img.' + extension, border_img)
	else:
		cv2.imwrite('output_img.' + extension, im_read)

def edging(filename):
	extension = os.path.splitext(filename)[1][1:]
	image = cv2.imread('image.' + extension)
	laplace = cv2.Laplacian(image, cv2.CV_64F)
	cv2.imwrite('output_img.' + extension, laplace)

