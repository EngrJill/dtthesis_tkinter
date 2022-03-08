import cv2
import SystemDataBase as db

def checkQrCodeAdmin():
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
            if data == "76392085910341-45":
                print("QR Code for Admin is Accepted")
                return True
                break
            else:
                print("QR Code for Admin Not Allowed")
                return False
                break
        
        # display the image preview
        #cv2.imshow("code detector", img)
        if(cv2.waitKey(1) == ord("q")):
            break
        
    # free camera object and exit
    cap.release()
    cv2.destroyAllWindows()
    







