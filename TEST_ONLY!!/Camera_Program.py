import cv2
import numpy as np
from operator import itemgetter

def compV():
    image = cv2.imread('example3.jpg')                                             # loads first copy of the water meter
    cont = cv2.imread('example3.jpg')                                              # loads second copy of the water meter
    image2 = cv2.imread('example3.jpg')                                            # loads third copy of the water meter



    # preparing for image processing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                          # performs grayscaling on image(required to make image easier to work with)
    gray = cv2.GaussianBlur(gray, (9, 9), 0)                                                # Blurs the grayscaled image(required to reduce noise in the image)
    edge = cv2.Canny(gray, 100, 100, 3)                                                     # performs edge detection(can be used in place of thresholding if thresholding doesn't give you the results you need

    # performs binary inverse on image
    (ret, bin_inv) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)   # performs binary_inverse threshold with OTSU on gray(grayscaled image)

    # finding contours (cnt=contours[10] is the contour for the rectangle that is saved in the list: contours)
    contours, hierarchy = cv2.findContours(bin_inv, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # finds the contours (chain_approx_simple finds contours using the minimum amount of points faster than chain_approx
    rect = contours                                                                          # places contours into rect
    rect = sorted(rect, key=cv2.contourArea, reverse=True)                                   # sorts contours from largest area to smalest area

    rect.pop(0)                                                                              # remove the largest area because for this instance it's the image border which prevents LCD detect
                                                                                             # once fixed it can be removed could be due to the ms paint modification
    displayRect = None

    # loop over the contours
    for c in rect:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if the contour has four vertices, then we have found
        # the thermostat display
        if len(approx) == 4:
            displayRect = approx
            break

    # finding coordinates for a rectangle and placing it on original image
    (x, y, w, h) = cv2.boundingRect(displayRect)                  # gets the coordinates for the rectangle which is cnt in list contours at index 10
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # draws the rectangle on (image of name image from up top)
    cv2.imshow('bounding rectangle', image)                       # shows the results of putting rectangle on image
    cv2.waitKey(0)                                                # moves to next part of code when any key is pressed

    # extracting roi from the original image
    roi = image[y:y + h, x:x + w]                                 # gets the bounding coordinates
    cv2.imwrite("roi.jpeg", roi)                                  # saves image

    # turning roi into a grayscale and thresholding with binary_inverse
    bounded = cv2.imread('roi.jpeg')                              # reads in the roi image
    bounded_2 = cv2.imread('roi.jpeg')                            # reads in the roi image

    # Applying erosion to the extracted ROI
    kernel = np.ones((3, 3), np.uint8)                            # creates a kernel which can be used for morphological transforms as well as a few other functions
    erosion = cv2.erode(bounded, kernel, iterations=1)            # performs the erosion morphological transform
    b_gray = cv2.cvtColor(erosion, cv2.COLOR_BGR2GRAY)            # performs gray scale to make image easier to work with

    (ret, binary) = cv2.threshold(b_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # performs binary_inverse threshold to make image easier to work with again

    cv2.imwrite("roi_thresh.jpeg", binary)                                  # saves the image

    # finding the contours in the extracted roi
    contours2, hierarchy2 = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours2  # store contours2 list in cnt(list of contours inside of roi)
    digitNum = []    # stores the contour coordinates
    num = []
    rec = cv2.imread('roi.jpeg')

    for c in cnt:
        (x, y, w, h) = cv2.boundingRect(c)                 # get coordinates for bounding rectangles for each contour
        if w >= 25 and ((h >= 20) and (h <= 60)):          # saves contours that match width and height requirements
            digitNum.append(c)

    # sort contours based on their X position
    # Sorting  according to a key change number in itemgetter(number) will sort by that enrty in matrix
    Mat = np.zeros((9, 4))                                  # A matrix to hold the contour coordinates

    for i in range(0, 9):
        (x, y, w, h) = cv2.boundingRect(digitNum[i])        # grabs the coordinates for each of the contours bounding box
        Mat[i] = (x, y, w, h)                               # saves those coordinates to a matrix


    Mat = sorted(Mat, key=itemgetter(0))                    # sorts the coordinates in order by the x-coordinate based on key which is first value of each matrix entry(in ascending order)
    conSort = [0] * 9

    redo = cv2.imread('roi.jpeg')                           # reads in roi.jpeg

    # sorts the actual contours and stores in conSort
    for i in range(0, 9):
        (x, y, w, h) = cv2.boundingRect(digitNum[i])                                    # loads the unsorted contour and its coordinates for sorting

        if x == Mat[0][0] and y == Mat[0][1] and w == Mat[0][2] and h == Mat[0][3]:
            conSort[0] = digitNum[i]                                                    # if the contour is equal to the first sorted contour store it in position 0
        elif x == Mat[1][0] and y == Mat[1][1] and w == Mat[1][2] and h == Mat[1][3]:
            conSort[1] = digitNum[i]                                                    # if the contour is equal to the second sorted contour store it in position 1
        elif x == Mat[2][0] and y == Mat[2][1] and w == Mat[2][2] and h == Mat[2][3]:
            conSort[2] = digitNum[i]                                                    # if the contour is equal to the third sorted contour store it in position 2
        elif x == Mat[3][0] and y == Mat[3][1] and w == Mat[3][2] and h == Mat[3][3]:
            conSort[3] = digitNum[i]                                                    # if the contour is equal to the fourth sorted contour store it in position 3
        elif x == Mat[4][0] and y == Mat[4][1] and w == Mat[4][2] and h == Mat[4][3]:
            conSort[4] = digitNum[i]                                                    # if the contour is equal to the fifth sorted contour store it in position 4
        elif x == Mat[5][0] and y == Mat[5][1] and w == Mat[5][2] and h == Mat[5][3]:
            conSort[5] = digitNum[i]                                                    # if the contour is equal to the sixth sorted contour store it in position 5
        elif x == Mat[6][0] and y == Mat[6][1] and w == Mat[6][2] and h == Mat[6][3]:
            conSort[6] = digitNum[i]                                                    # if the contour is equal to the seventh sorted contour store it in position 6
        elif x == Mat[7][0] and y == Mat[7][1] and w == Mat[7][2] and h == Mat[7][3]:
            conSort[7] = digitNum[i]                                                    # if the contour is equal to the eighth sorted contour store it in position 7
        elif x == Mat[8][0] and y == Mat[8][1] and w == Mat[8][2] and h == Mat[8][3]:
            conSort[8] = digitNum[i]                                                    # if the contour is equal to the ninth sorted contour store it in position 8


    for j in range(0, 9):
        (x, y, w, h) = cv2.boundingRect(conSort[j])                     # grabs the coordinates for each of the contours bounding box

        cv2.rectangle(redo, (x, y), (x + w, y + h), (0, 255, 0), 1)     # draws a rectangle around the contour
        bond = redo[y:y + h, x:x + w]                                   # extracts the area inside that rectangle as an image
        num.append(bond)                                                # stores the image of each number in an array

    cv2.imshow('h', redo)
    cv2.waitKey(0)
    screenRead = [-1] * 9                              # list that holds the numeric value of the display

    # code that determines which segments from the display are on and off
    for k in range(0, 9):
        cv2.imwrite('CurrentNum.jpg', num[k])        # writes the image stored in the array into an image file to be used
        img = cv2.imread('CurrentNum.jpg')           # reads the image to the variable img
        #cv2.imshow('name', img)                      # shows the image saved to img
        #cv2.waitKey(0)                               # moves on to next part of code when button is pressed

        (x, y, W, H) = cv2.boundingRect(conSort[k])  # grabs the coordinates for each of the contours bounding box

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converts image to grayscale

        (ret1, binary) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)   # thresholds the image

        #cv2.imshow('thresh', binary)
        cv2.imwrite('thresh.jpg', binary)
        matrix = np.array(binary)
        np.savetxt('Image Array', matrix)
        #cv2.waitKey(0)

        on = 255                # value of an "on" pixel
        Segment = [0] * 7       # array of each segment of 7 segment display
        W_add = 6               # average width of the side segments
        H_add = 5               # average height of the top, middle, and bottom segments
        H_temp = (H - 2) / 2
        Htop = int(H_temp)      # start/stop point of the side segments

        Mid_temp = H_add / 2
        Mid = int(Mid_temp)     # position of middle pixel with regard to H

        Middle = Htop + 1       # position of bottom left/right segment (j) start with regard to H

        # Top Segment
        i = 1                   # initialize i
        j = 1                   # initialize j
        Total_Top = []          # initialize the list of totals to NULL
        add = 0                 # initialize add to 0

        for top in range(1, W - W_add + 2):
            total = 0                           # reset total
            for top2 in range(1, (H_add + 1)):
                total = total + matrix[j][i]    # adds up total of each column
                j = j + 1                       # increment row
                add = add + 1                   # increment number of pixels added

            Total_Top.append(total)             # insert total into list
            j = 1                               # reset row
            i = i + 1                           # increment column

        segment_T = sum(Total_Top)              # sum of all the column totals
        avg = segment_T / add                   # average pixel value for the segment
        segment_T = avg / on                    # calculates how close to pixel value 255 segment is

        if segment_T >= .55:
            Segment[0] = 1                      # if segment shows 60% match or higher it is set to on

        # Top Left Segment
        i = 1                                   # initialize i
        j = 1                                   # initialize j
        Total_Top = []                          # initialize list of totals to NULL
        add = 0                                 # resets add to 0

        for top_L in range(1, Htop + 1):
            total = 0                           # resets total to 0
            for top_L2 in range(1, W_add + 1):
                total = total + matrix[j][i]    # adds pixel values in each row
                add = add + 1                   # increment number of pixels added
                i = i + 1                       # increment column

            Total_Top.append(total)             # insert total into list
            j = j + 1                           # increment row
            i = 1                               # reset column

        segment_T = sum(Total_Top)              # sum of all the row totals
        avg = segment_T / add                   # average pixel value for the segment
        segment_T = avg / on                    # calculate how close to pixel value 255 segment is

        if segment_T >= .55:
            Segment[1] = 1                      # if segment shows 60% match or higher it is set to on

        # Top Right Segment
        i = W - W_add                           # initialize i
        j = 1                                   # initialize j
        Total_Top = []                          # initialize list of totals to NULL
        add = 0                                 # resets add to 0

        for top_R in range(1, Htop + 1):
            total = 0                           # resets total to 0
            for top_R2 in range(1, W_add + 1):
                total = total + matrix[j][i]    # adds pixel values in each row
                add = add + 1                   # increment number of pixels added
                i = i + 1                       # increment column

            Total_Top.append(total)             # insert total into list
            j = j + 1                           # increment row
            i = W - W_add                       # reset column

        segment_T = sum(Total_Top)              # sum of all the row totals
        avg = segment_T / add                   # average pixel value for the segment
        segment_T = avg / on                    # calculate how close to pixel value 255 segment is

        if segment_T >= .55:
            Segment[2] = 1                      # if segment shows 60% match or higher it is set to on

        # Middle Segment
        i = 1                                   # initialize i
        j = Htop - Mid                          # initialize j
        Total_Top = []                          # initialize list of totals to NULL
        add = 0                                 # resets add to 0

        for middle in range(1, W - W_add):
            total = 0                           # resets total to 0
            for middle2 in range(1, H_add + 1):
                total = total + matrix[j][i]    # adds pixel values in each column
                j = j + 1                       # increment row
                add = add + 1                   # increment number of pixels added

            Total_Top.append(total)             # insert total into list
            j = Htop - Mid                      # resets row
            i = i + 1                           # increments column

        segment_T = sum(Total_Top)              # sum of all the column totals
        avg = segment_T / add                   # average pixel value for the segment
        segment_T = avg / on                    # calculate how close to pixel value 255 segment is

        if segment_T >= .55:
            Segment[3] = 1                      # if segment shows 60% match or higher it is set to on

        # Bottom Left Segment
        i = 1                                   # initialize i
        j = Middle                              # initialize j
        Total_Top = []                          # initialize list of totals to NULL
        add = 0                                 # resets add to 0

        for bottom_L in range(1, ((Htop + 1 - H_add) + 1)):
            total = 0                               # resets total to 0
            for bottom_L2 in range(1, W_add + 1):
                total = total + matrix[j][i]        # adds pixel values in each row
                i = i + 1                           # increment column
                add = add + 1                       # increment number of pixels added

            Total_Top.append(total)             # insert total into list
            j = j + 1                           # increment row
            i = 1                               # reset column

        segment_T = sum(Total_Top)              # sum of all the column totals
        avg = segment_T / add                   # average pixel value for the segment
        segment_T = avg / on                    # calculate how close to pixel value 255 segment is

        if segment_T >= .55:
            Segment[4] = 1                      # if segment shows 60% match or higher it is set to on

        # Bottom Right Segment
        i = W - 1 - W_add                       # initialize i
        j = Middle                              # initialize j
        Total_Top = []                          # initialize list of totals to NULL
        add = 0                                 # resets add to 0

        for bottom_R in range(1, ((Htop - H_add + 1) + 1)):
            total = 0                               # resets total to 0
            for bottom_R2 in range(1, W_add + 1):
                total = total + matrix[j][i]        # adds pixel values in each row
                i = i + 1                           # increment column
                add = add + 1                       # increment number of pixels added

            Total_Top.append(total)             # insert total into list
            j = j + 1                           # increment row
            i = W - 1 - W_add                   # reset column

        segment_T = sum(Total_Top)              # sum of all the column totals
        avg = segment_T / add                   # average pixel value for the segment
        segment_T = avg / on                    # calculate how close to pixel value 255 segment is

        if segment_T >= .55:
            Segment[5] = 1                      # if segment shows 60% match or higher it is set to on

        # Bottom Segment
        i = W_add + 1                           # initialize i
        j = H - 2 - H_add                       # initialize j
        Total_Top = []                          # initialize list of totals to NULL
        add = 0                                 # resets add to 0

        for bottom in range(1, (W - 2 * W_add - 2)):
            total = 0                               # resets total to 0
            for bottom2 in range(1, (H_add + 1)):
                total = total + matrix[j][i]        # adds pixel values in each column
                j = j + 1                           # increment column
                add = add + 1                       # increment number of pixels added

            Total_Top.append(total)             # insert total into list
            i = i + 1                           # increment column
            j = H - 2 - H_add                   # resets row

        segment_T = sum(Total_Top)              # sum of all the column totals
        print(segment_T)
        avg = segment_T / add                   # average pixel value for the segment
        print(avg)
        segment_T = avg / on                    # calculate how close to pixel value 2555 segment is
        print(segment_T)

        print(Segment)

        if segment_T >= .55:
            Segment[6] = 1                      # if segment shows 60% match or higher it is set to on

        if Segment == [1,1,1,0,1,1,1]:
            screenRead[k] = 0
        elif Segment == [0,0,1,0,0,1,0]:
            screenRead[k] = 1
        elif Segment == [1,0,1,1,1,0,1]:
            screenRead[k] = 2
        elif Segment == [1,0,1,1,0,1,1]:
            screenRead[k] = 3
        elif Segment == [0,1,1,1,0,1,0]:
            screenRead[k] = 4
        elif Segment == [1,1,0,1,0,1,1]:
            screenRead[k] = 5
        elif Segment == [1,1,0,1,1,1,1]:
            screenRead[k] = 6
        elif Segment == [1,0,1,0,0,1,0]:
            screenRead[k] = 7
        elif Segment == [1,1,1,1,1,1,1]:
            screenRead[k] = 8
        elif Segment == [1,1,1,1,0,1,1]:
            screenRead[k] = 9
        else:
            screenRead[k] = 1

    print(screenRead)
compV()
