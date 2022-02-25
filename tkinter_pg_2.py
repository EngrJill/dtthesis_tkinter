import qrCodeDetector as qrd 
import tempChecker as temp


def go():
        if(qrd.checkQrCode()):
            put = input("Please input temperature ")
            if temp.tempCheck(float(put)):
                print("Access Granted")
            else:
                print("Denied")
        else:
            print("Denied")


# if __name__ == "__main__":
#     main()