import qrCodeDetector as qrd 
import cv2
import time
import idleWindow as iw
import SystemDataBase as db

def process():
    

    # def goQRandTemp():
    #         if(qrd.checkQrCode()):
    #             cv2.destroyAllWindows()
    #             put = input("Please input temperature ")
    #             print(qrdb.qrCodeArr)
    #             print(qrdb.tempArr)
    #             if temp.tempCheck(float(put)):
    #                 print("Access Granted")
    #                 time.sleep(2)
    #                 pg.loopingWindow()
    #             else:
    #                 print("Denied")
    #                 time.sleep(2)
    #                 pg.loopingWindow()
    #         else:
    #             print("Denied")
    #             time.sleep(2)
    #             pg.loopingWindow()
    
    # def TempOnly():

    def goQROnly():
        if (qrd.checkQrCode()):
            print("QR Code is Accepted")
            iw.loopingWindow()
        else:
            print("QR Code is invalid")
            iw.loopingWindow()

    if (db.accessData == 'QRandTemp'):
        goQRandTemp()
    elif (db.accessData == 'QROnly'):
        goQROnly()
    elif (db.accessData == 'TempOnly'):
        goTempOnly()
    

# if __name__ == "__main__":
#     main()