"""
This file contains all the functions used to make the graphical interface

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
from PIL import ImageTk

##### FUNCTIONS #####
def GUI(img, number, type):
    """
    This function is used to show a reference traffic sign according to the speed limit recognized
    :param img: the img of the GUI to update at each loop of the function
    :param number: the number recognized by the OCR algorithm
    :return the img updated
    """
    if number is not None:
        # Case of speed limits
        if type == "speed_limit":
            print(number)
            if "10" in number:
                if "110" in number:
                    print("@@@@ 110 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref110.jpg")
                else:
                    print("@@@@ 10 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref10.jpg")
            elif "30" in number:
                if "130" in number:
                    print("@@@@ 130 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref130.jpg")
                else:
                    print("@@@@ 30 @@@@")
                    img = ImageTk.PhotoImage(file="assets/ref30.jpg")
            elif "45" in number:
                print("@@@@ 45 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref45.jpg")
            elif "50" in number:
                print("@@@@ 50 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref50.jpg")
            elif "70" in number:
                print("@@@@ 70 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref70.jpg")
            elif "80" in number:
                print("@@@@ 80 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref80.jpg")
            elif "90" in number:
                print("@@@@ 90 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref90.jpg")
        # Case of end speed limits
        elif type == "speed_limit_end":
            print("END", number)
            if "30" in number:
                print("@@@@ END 30 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref30end.jpg")
            elif "50" in number:
                print("@@@@ END 50 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref50end.jpg")
            elif "70" in number:
                print("@@@@ END 70 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref70end.jpg")
            elif "80" in number:
                print("@@@@ END 80 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref80end.jpg")
            elif "90" in number:
                print("@@@@ END 90 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref90end.jpg")
            if "110" in number:
                print("@@@@ END 110 @@@@")
                img = ImageTk.PhotoImage(file="assets/ref110end.jpg")
    return img

