"""
This file contains all the functions used to make the graphical interface

@authors: BARTH Werner, BRUNET Julien, THOMAS Morgan
"""

##### IMPORTS #####
from PIL import ImageTk

##### FUNCTIONS #####
def belong_to(number, list):
    """
    This functions is used to classify the number recognized
    :param number: the number recognized by OCR algorithm
    :param list: the list of all speed limits
    :return the speed limit recognized
    """
    for elt in list:
        for type in elt:
            if (number==type):
                return elt[0]

def GUI(img, number, list):
    """
    This function is used to show a reference traffic sign according to the speed limit recognized
    :param img: the img of the GUI to update at each loop of the function
    :param number: the number recognized by the OCR algorithm
    :param list: the list of all speed limits
    :return the img updated
    """
    if number is not None:
        type = belong_to(number, list)
        print(type)
        if type == "30":
            print("@@@@ 30 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref30.jpg")
        elif type == "50":
            print("@@@@ 50 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref50.jpg")
        elif type == "70":
            print("@@@@ 70 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref70.jpg")
        elif type == "90":
            print("@@@@ 90 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref90.jpg")
        elif type == "110":
            print("@@@@ 110 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref110.jpg")
        elif type == "130":
            print("@@@@ 130 @@@@")
            img = ImageTk.PhotoImage(file="assets/ref130.jpg")
    return img

