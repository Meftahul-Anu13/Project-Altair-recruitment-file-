import cv2 as cv
import numpy as np

# img= cv.imread('GOAT.jpg') 
# cv.imshow('goat',img)
# cv.waitKey(0)

def analyze_goat(img_array):
     #  image resolution (width and height)
    height, width, _ = img.shape
#  total image size (number of pixels)
    total_pixels = height * width

#claculating ....


    # Calculate statistics
    minPixel = np.min(img_array) #0-255 range thake mostly 
    maxPixel = np.max(img_array)
    avgPixel = np.mean(img_array)
    num_nonzeroPixels = np.count_nonzero(img_array)
    num_zeroPixels = img_array.size - num_nonzeroPixels
     # num_zero_pixels =  img_array.size- num_nonzero_pixels

    # Display the information on the grayscale img
    font = cv.FONT_HERSHEY_TRIPLEX
    font_scale = 1
    #white color 
    text_color = (255, 255, 255)  
    # text_color = (0,255,0)
    line_type = cv.FILLED
  
    font_thickness = 2
    x=190
    y=255

    # Draw the text on the img

    result_img = cv.putText(img_array, f"Min Value: {minPixel}", (50+x, 50+y), font, font_scale, text_color, font_thickness, line_type)
    result_img = cv.putText(result_img, f"Max Value: {maxPixel}", (50+x, 80+y), font, font_scale, text_color, font_thickness, line_type)
    result_img = cv.putText(result_img, f"Avg Value: {avgPixel:.2f}", (50+x, 110+y), font, font_scale, text_color, font_thickness, line_type)
    result_img = cv.putText(result_img, f"Image  size : {img_array.size}", (50+x, 140+y), font, font_scale, text_color, font_thickness, line_type)
    result_img = cv.putText(result_img, f"Nonzero Pixels: {num_nonzeroPixels}", (50+x, 170+y), font, font_scale, text_color, font_thickness, line_type)
    result_img = cv.putText(result_img, f"Zero Pixels: {num_zeroPixels}", (50+x, 200+y), font, font_scale, text_color, font_thickness, line_type)
   # if i just want to just print the pixels values on the console 
    # print("Min Value: {}".format(minPixel))
    # print("Max Value: {}".format(maxPixel))
    # print("avg Value: {}".format(avgPixel))
    # print("Non zero Value: {}".format(num_nonzeroPixels))
    # print("zero Value: {}".format(num_zeroPixels))
    # print("Total resulation:{}".format(totalPixels))

    # Display the img with information
    cv.imshow('Analyzed Image', result_img)

#IMAGE READING FUNCTION 
img=cv.imread('GOAT.JPG')
# the grayscale img
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#function calling for img array 
analyze_goat(gray_img)
cv.waitKey(0)
# cv.destroyAllWindows()
