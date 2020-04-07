import cv2
import numpy as np 
import imutils

def license_plate_extractor(car=cv2.imread("carz.jpg")):
    
    #resizing the given image
    car = imutils.resize(car, width=500)

    #Showing the original image
    cv2.imshow("Original car", car)

    #Converting to grayscale
    gray = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
    cv2.imshow("1 - Grayscale Conversion", gray)

    #Sharpening the image by bilateral Filter
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    cv2.imshow("2 - Bilateral Filter", gray)

    #Taking the edges out of the image
    edged = cv2.Canny(gray, 170, 200)
    cv2.imshow("4 - Canny Edges", edged)

    #Taking out all the contours from the image
    cnts,_ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
    
    # Making a list of number_plates in the picture
    NumberPlateCnt = None 

    #Taking out the relevant contours
    count = 0
    for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4 and cv2.isContourConvex(approx):
                NumberPlateCnt = approx
                cont=c 
                break

    #Taking out The number plate out of the image
    rect= cv2.minAreaRect(approx)
    center,size,theta=rect
    
    center,size = tuple(map(int,center)), tuple(map(int,size))
    M=cv2.getRotationMatrix2D( center,theta, 1)
    dst=cv2.warpAffine(car, M, (car.shape[0],car.shape[1]))
    output = cv2.getRectSubPix(dst, size, center)
    output = cv2.resize(output, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
    w,l,_= output.shape
    
    #Writing the image at a secure folder
    #cv2.imwrite(r"/home/ultracurse/Project/workspace/license1.png",output)

    #calling the segmentation and returning its output :
    return segment(output)


def segment(license):
    import License_no
    #Cropping the unwanted pixels
    width,length,_=license.shape
    license=license[3:width-3,3:length-3]
    
    #Converting to grayscale
    gray=cv2.cvtColor(license,cv2.COLOR_BGR2GRAY)

    #Making the noises diappear by gaussian blur
    gray=cv2.GaussianBlur(gray,(7,7),0)

    #Thresholding the images to convert to only two value array either 0 or 255
    ret,mask = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

    #Dilating the image for use
    use=cv2.dilate(mask,None,iterations=1)

    #Taking out the contours from the images
    cnts = cv2.findContours(use.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[1] if imutils.is_cv3() else cnts[0]


    orig = license.copy()
    i = 0

    #Sorting the image's Contour from left to right
    cnts = sorted(cnts, key=lambda ctr:cv2.boundingRect(ctr)[1])

    #Sorting the image's contour from top to bottom
    cnts = sorted(cnts, key=lambda ctr: cv2.boundingRect(ctr)[0] + cv2.boundingRect(ctr)[1] * license.shape[1] )
    for cnt in cnts:
        

        # Filtered countours are detected
        x,y,w,h = cv2.boundingRect(cnt)

        # Taking ROI of the cotour
        roi = license[y:y+h, x:x+w]

        # Marking on the license
        cv2.rectangle(orig,(x,y),(x+w,y+h),(0,255,0),2)

        # Save your contours or characters
        cv2.imwrite("roi/roi" + str(i) + ".png", roi)

        i = i + 1
    
    return License_no.plate_no()

if __name__== "__main__":

    image=cv2.imread("carz.jpg")
    segment(license_plate_extractor(image))
       