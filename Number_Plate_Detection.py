import numpy as np
import cv2

cropped_image = cv2.imread('./output/ROI.jpg')

gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)



bilateral_filtered = cv2.bilateralFilter(gray, 11, 50, 50)
cv2.imshow('Bilateral Filtered', bilateral_filtered)


ret, plate_inverse_threshold = cv2.threshold(bilateral_filtered, 115, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold', plate_inverse_threshold)


# Vertical and Horizontal Scanning to reduce the region of interest
middle_x = int(plate_inverse_threshold.shape[0]/2)
middle_y = int(plate_inverse_threshold.shape[1]/2)
# while True:
#     if cv2.waitKey(1)==ord('q'):
#         break


def getTopCoordinate():
    for x in range(middle_x,-1,-1):
        black_count = 0
        white_count = 0
        for y in range(0, plate_inverse_threshold.shape[1]):
            if(plate_inverse_threshold[x][y] == 255):
                white_count += 1
            else:
                black_count += 1
        
        ratio = 400         #calculates a ratio for each row.
                            # This ratio essentially quantifies the balance between white and black pixels in the row. A high ratio means there are more white pixels relative to black pixels, indicating a region that is predominantly white. Conversely, a low ratio means there are more black pixels relative to white pixels, suggesting a predominantly black region.
        
        if(black_count != 0):
            ratio = white_count/black_count         
        
        # print((white_count,black_count, ratio))
        if(ratio > 10 or ratio < 0.3):          #If the calculated ratio for a given row is greater than 10 (meaning there are significantly more white pixels than black pixels) or less than 0.3 (meaning there are significantly more black pixels than white pixels), it indicates that the balance of pixel colors in that row is skewed.
            return x                            #A ratio greater than 10 suggests a predominantly white region, which might indicate the top part of the area of interest, like the top of a license plate.
                                                #A ratio less than 0.3 suggests a predominantly black region, which might indicate the presence of text or symbols (e.g., characters on a license plate).


    return 0

def getBottomCoordinate():
    for x in range(middle_x,250,1):
        black_count = 0
        white_count = 0
        for y in range(0, plate_inverse_threshold.shape[1]):
            if(plate_inverse_threshold[x][y] == 255):
                white_count += 1
            else:
                black_count += 1
        
        ratio = 400
        
        if(black_count != 0):
            ratio = white_count/black_count
        
        # print(ratio)
        if(ratio > 10 or ratio < 0.3):
            return x
        
    
    return 150

def getLeftCoordinate():
    for y in range(middle_y,-1,-1):
        black_count = 0
        white_count = 0
        for x in range(0, plate_inverse_threshold.shape[0]):
            if(plate_inverse_threshold[x][y] == 255):
                white_count += 1
            else:
                black_count += 1
        
        ratio = 150
        if(black_count != 0):
            ratio = white_count/black_count
        
        if(ratio > 30):
            return y
    return 0

def getRightCoordinate():
    for y in range(middle_y,450,1):
        black_count = 0
        white_count = 0
        for x in range(0, plate_inverse_threshold.shape[0]):
            if(plate_inverse_threshold[x][y] == 255):
                white_count += 1
            else:
                black_count += 1
        
        ratio = 150
        if(black_count != 0):
            ratio = white_count/black_count
        
        if(ratio > 40):
            return y
    return plate_inverse_threshold.shape[1]


top = getTopCoordinate()
bottom = getBottomCoordinate()
left = getLeftCoordinate()
right = getRightCoordinate()
print(top)
print(bottom)
print(left)
print(right)

#img1 = cropped_image[top:bottom, left:right]
#cv2.imshow('cropped', img1)

for i in range(1,7):        # Making adjustments to the coordinates of a region of interest by expanding the ROI in all directions (up, down, left, and right) by a certain number of pixels. 
    if(top-i >= 0):
        top = top-i
    
    if(bottom+i < cropped_image.shape[0]):
        bottom = bottom+i
    
    if(left-i >= 0):
        left = left-i
    
    if(right+i < cropped_image.shape[1]):
        right = right+i

img = cropped_image[top:bottom, left:right]
cv2.imshow('crop', img)

cv2.imwrite('./output/plate_ROI.jpg', img)

# while True:
#     if cv2.waitKey(1)==ord('q'):
#         break

