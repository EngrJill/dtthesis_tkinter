import qrCodeDetector as qrd 
import tempChecker as temp
import cv2


def go():
        if(qrd.checkQrCode()):
            cv2.destroyAllWindows()
            put = input("Please input temperature ")
            if temp.tempCheck(float(put)):
                print("Access Granted")
            else:
                print("Denied")
        else:
            print("Denied")


# if __name__ == "__main__":
#     main()