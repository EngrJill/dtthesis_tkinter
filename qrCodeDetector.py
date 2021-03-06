import cv2
import SystemDataBase as db

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
            if data == db.todaysQRData:
                db.qrCodeArr.append(data)
                print("QR Code is Accepted")
                return [True, data]
                break
            elif len(db.todaysQRData)-1 == i:
                print("QR Code Not Allowed")
                return [False, data]
                break
            else:
                i = i+1

        
        # display the image preview
        #cv2.imshow("code detector", img)
        if(cv2.waitKey(1) == ord("q")):
            break
        
    # free camera object and exit
    cap.release()
    cv2.destroyAllWindows()
    






