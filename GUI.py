"""
This file contains all the functions used to make the graphical interface

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
from PIL import ImageTk

##### FUNCTIONS #####
def GUI(img, number):
    """
    This function is used to show a reference traffic sign according to the speed limit recognized
    :param img: the img of the GUI to update at each loop of the function
    :param number: the number recognized by the OCR algorithm
    :return the img updated
    """
    if number is not None:
        print(number)
        if number == "30":
            print("@@@@ 30 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref30.jpg")
        elif number == "50":
            print("@@@@ 50 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref50.jpg")
        elif number == "70":
            print("@@@@ 70 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref70.jpg")
        elif number == "90":
            print("@@@@ 90 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref90.jpg")
        elif number == "110":
            print("@@@@ 110 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref110.jpg")
        elif number == "130":
            print("@@@@ 130 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref130.jpg")
    return img

