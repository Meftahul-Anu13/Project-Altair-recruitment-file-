import cv2 as cv 
import numpy as np

# def detect_red_and_white_regions(image):
#     # Convert the image from BGR to HSV color space for better color detection
#     hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

#     #  lower and upper boundaries ofred color in HSV
#     lower0fred1 = np.array([0, 100, 100])
#     upper0fred1 = np.array([10, 255, 255])

#     #  red color (wrap-around) in HSV
#     lower0fred2 = np.array([160, 100, 100])
#     upper0fred2= np.array([180, 255, 255])
#     #  lower and upper boundaries of white color in HSV
#     upper_white = np.array([180, 30, 255])
#     lower_white = np.array([0, 0, 200])
#     mask1 = cv.inRange(hsv, lower0fred1, upper0fred1)
#     mask2 = cv.inRange(hsv, lower0fred2, upper0fred2)
#     white_mask = cv.inRange(hsv, lower_white, upper_white)

#     # Combine the two red masks to get the final red mask
#     # red_mask = cv.bitwise_or(mask1,mask2)
#     #or we can bitwise or for adding 2 mask instead + algo 
#     red_mask=mask2+mask1#if i just put mask1 here then only red will be appear 
#     result_red=image.copy()
#     result_red=cv.bitwise_and(result_red,result_red,mask=red_mask)

#     result_white=image.copy()
#     result_white=cv.bitwise_and(result_white,result_white,mask=white_mask)
#     # Combine the red and white masks 
#     # mask = cv.bitwise_or(red_mask, white_mask)
#     mask=red_mask+white_mask
#     result_combined=image.copy()
#     result_combined=cv.bitwise_and(result_combined,result_combined,mask=mask)

#     # Apply the mask to the original image to get the regions of interest
#     #  = cv.bitwise_and(image, image, mask=mask)

#     # Display red region
#     cv.imshow('Detected REd Regions',result_red )
#     # Display white region 
#     cv.imshow('Detected White  Regions',result_white)
#     #combined
#     cv.imshow('Combined Image',result_combined)
#     # cv.waitKey(0)
#     # cv.destroyAllWindows()
   


def analyze_goat(img_array):
     #  image resolution (width and height)
    height, width, _ = image.shape
#  total image size (number of pixels)
    total_pixels = height * width

#claculating ....


    # Calculate statistics
    minPixel = np.min(img_array)
    maxPixel = np.max(img_array)
    avgPixel = np.mean(img_array)
    num_nonzeroPixels = np.count_nonzero(img_array)
    num_zeroPixels = img_array.size - num_nonzeroPixels
     # num_zero_pixels =  total_pixels - num_nonzero_pixels

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




# Load the image
image = cv.imread('GOAT.jpg')

# Call the function to detect red and white regions
# detect_red_and_white_regions(image)


# img=cv.imread('GOAT.jpg')
# the grayscale img
gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

analyze_goat(gray_img)
cv.waitKey(0)
cv.destroyAllWindows()
