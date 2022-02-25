import cv2
import thesis_request as tr

def checkQrCode():
    # set up camera object
    cap = cv2.VideoCapture(0)
    # QR code detection object
    detector = cv2.QRCodeDetector()

    i = 0
    while True:
        # get the image
        _, img = cap.read()
        # get bounding box coords and data
        data, bbox, _ = detector.detectAndDecode(img)
        
        if data:
            if data == tr.getTodaysData()[i]:
                return True
            elif len(tr.getTodaysData())-1 == i:
                return False
            else:
                i = i+1
        
        # display the image preview
        cv2.imshow("code detector", img)
        if(cv2.waitKey(1) == ord("q")):
            break

    # free camera object and exit
    cap.release()
    cv2.destroyAllWindows()

checkQrCode()

