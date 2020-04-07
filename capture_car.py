def take_pic(sigt,strt,turn,flag):

    import cv2
    import numpy as np
    import time
    import motion
    import mail

    capture=cv2.VideoCapture(0)             #'GenYoutube.net_Cars_moving_on_road_Stock_Footage_-_Free_Download.mp4.mp4')
    fgmk=cv2.createBackgroundSubtractorMOG2()

    def get_image():
        ret, frame=capture.read()
        frame1=fgmk.apply(frame)
        frame2=cv2.bitwise_and(frame,frame,mask=frame1)
        return frame2,frame1,frame


    for i in range(30):
        temp = get_image()
    print('Taking image...')
    t= round(time.time())
    nm = "/home/rahul/Project/images/"+ str(t)
    camera_capture, mask, orig = get_image()
    cv2.imwrite(nm+'.png',camera_capture)
    #cv2.imwrite(nm+'_mask.png',mask)
    cv2.imwrite(nm+'_orig.png',orig)
    #cv2.imshow(nm+'_orig.png',orig)
    #time.sleep(5)

    del(capture)
    cv2.destroyAllWindows()

    mail.find_plate(nm) # image extesion is missing added later in the called function

    motion.motion(sigt,strt,turn,flag)
    '''
    img=cv2.imread('first.png',cv2.IMREAD_GRAYSCALE)
    threshold = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
    cv2.imwrite('second.png',threshold)
    NOT THE RIGHT IDEA
    '''


    '''To remove noise
    img=cv2.imread('first.png')
    kernel = np.ones((115,15),np.float32)/255
    smooth =cv2.filter2D(img,-1,kernel)
    cv2.imshow('smoother',smooth)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    NO USE
    '''


    '''kernel = np.ones((5,5),np.int8)
    erosion =cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations =1)
    opening =cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    add=cv2.bitwise_and(opening,opening,mask=erosion)

    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('Morpho',add)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    NO USE
    '''
if __name__ == '__main__':
    take_pic(sigt=15)
