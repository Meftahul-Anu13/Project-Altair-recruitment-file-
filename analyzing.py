import cv2
import numpy as np

# img= cv2.imread('GOAT.jpg') 
# cv2.imshow('goat',img)
# cv2.waitKey(0)

def analyze_goat(img_array):
    # Calculate statistics
    # Get the image resolution (width and height)
    height, width, _ = img_array.shape
# Calculate the total image size (number of pixels)
    total_pixels = height * width

#claculating ...........

    min_pixel_value = np.min(img_array)
    max_pixel_value = np.max(img_array)
    avg_pixel_value = np.mean(img_array)
    num_nonzero_pixels = np.count_nonzero(img_array)
    num_zero_pixels =  total_pixels- num_nonzero_pixels
    # num_zero_pixels =  img_array.size- num_nonzero_pixels


# Display the results
    # print("Image resolution (width x height): {} x {}".format(width, height))
    # print("Total image size (number of pixels):", total_pixels)

    # Display the information on the grayscale img
    # font = cv2.FONT_HERSHEY_SIMPLEX
    font=cv2.FONT_HERSHEY_TRIPLEX
    font_scale = 1
    font_thickness = 2
    text_color = (255,255,255)  # White color for text AUTOMATICALLY RGB BLACK HYE JAY
    line_type = cv2.LINE_AA

    # Draw the text on the img
    result_img = cv2.putText(img_array, f"Min Value: {min_pixel_value}", (10, 30), font, font_scale, text_color, font_thickness, line_type)
    result_img = cv2.putText(result_img, f"Max Value: {max_pixel_value}", (10, 60), font, font_scale, text_color, font_thickness, line_type)
    result_img = cv2.putText(result_img, f"Avg Value: {avg_pixel_value:.2f}", (10, 90), font, font_scale, text_color, font_thickness, line_type)
    result_img = cv2.putText(result_img, f"img size : {total_pixels}", (10, 180), font, font_scale, text_color, font_thickness, line_type)
    result_img = cv2.putText(result_img, f"Nonzero Pixels: {num_nonzero_pixels}", (10, 120), font, font_scale, text_color, font_thickness, line_type)
    # result_img = cv2.putText(result_img, f"img size : {img_array.size}", (10, 180), font, font_scale, text_color, font_thickness, line_type)
    result_img = cv2.putText(result_img, f"Zero Pixels: {num_zero_pixels}", (10, 150), font, font_scale, text_color, font_thickness, line_type)
 



    # Display the img with information
    cv2.imshow('Analyzed Grayscale Img', result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Sample usage:
# Load the grayscale img
img=cv2.imread('GOAT.JPG')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Call the function to analyze the grayscale img
analyze_goat(gray_img)

# import cv2

# # Read the image
# image = cv2.imread('bw.jpg')


