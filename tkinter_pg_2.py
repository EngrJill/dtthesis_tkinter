import qrCodeDetector as qrd 
import tempChecker as temp
import cv2
import time
import playGround as pg
import QrDataBase as qrdb


def go():
        if(qrd.checkQrCode()):
            cv2.destroyAllWindows()
            put = input("Please input temperature ")
            print(qrdb.qrCodeArr)
            print(qrdb.tempArr)
            if temp.tempCheck(float(put)):
                print("Access Granted")
                time.sleep(2)
                pg.loopingWindow()
            else:
                print("Denied")
                time.sleep(2)
                pg.loopingWindow()
        else:
            print("Denied")
            time.sleep(2)
            pg.loopingWindow()


# if __name__ == "__main__":
#     main()