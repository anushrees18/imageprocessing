import cv2
img = cv2.imread("pic.png", cv2.IMREAD_COLOR)


cv2.imshow("image", img)

cv2.waitKey(0)


path = r'pic.png'

src = cv2.imread(path)

window_name = 'Image'

image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow(window_name, image)
cv2.waitKey(0)

import cv2 
import numpy as np 
  
image = cv2.imread('pic.png') 

height, width = image.shape[:2] 
  
quarter_height, quarter_width = height / 4, width / 4
  
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]]) 

img_translation = cv2.warpAffine(image, T, (width, height)) 
  
cv2.imshow("Originalimage", image) 
cv2.imshow('Translation', img_translation) 
cv2.waitKey() 
  
cv2.destroyAllWindows() 

import cv2 

img = cv2.imread('pic.png')

avging = cv2.blur(img,(10,10))
 
cv2.imshow('Averaging',avging)
cv2.waitKey(0)


gausBlur = cv2.GaussianBlur(img, (5,5),0) 
cv2.imshow('Gaussian Blurring', gausBlur)
cv2.waitKey(0)


medBlur = cv2.medianBlur(img,5)
cv2.imshow('Media Blurring', medBlur)
cv2.waitKey(0)

ng
bilFilter = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral Filtering', bilFilter)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

img = cv2.imread('img.jpg')

# cv2.imread() -> takes an image as an input
h, w, channels = img.shape

half = w//2


# this will be the first column
left_part = img[:, :half] 

# [:,:half] means all the rows and
# all the columns upto index half

# this will be the second column
right_part = img[:, half:] 

# [:,half:] means all the rows and all
# the columns from index half to the end
# cv2.imshow is used for displaying the image
cv2.imshow('Left part', left_part)
cv2.imshow('Right part', right_part)

# this is horizontal division
half2 = h//2

top = img[:half2, :]
bottom = img[half2:, :]

cv2.imshow('Top', top)
cv2.imshow('Bottom', bottom)

# saving all the images
# cv2.imwrite() function will save the image 
# into your pc
cv2.imwrite('top.jpg', top)
cv2.imwrite('bottom.jpg', bottom)
cv2.imwrite('right.jpg', right_part)
cv2.imwrite('left.jpg', left_part)
cv2.waitKey(0)

