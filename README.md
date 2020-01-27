# <ins> Traffic Sign Recognition : </ins>

This project implements a solution for the detection and recognition of traffic signs on a Raspberry Pi.  

For the moment, we only work on speed limits detection (ie. round with red bounders signs)

This Readme is a summary, for more information, you can read the [wiki](https://gitlab.com/julienbrunet21/traffic-sign-recognition/wikis/wiki/home) associated to the project on the repository. 

## <ins> Compatibility : </ins>
This project has been developed to work with **Python 3.7**

It uses some external libraries:
<ul>
<li> 

[OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_intro/py_intro.html) 

</li>
<li> 

[Immutils](https://github.com/jrosebr1/imutils) 

</li>
<li> 

[Numpy](https://numpy.org/) 

</li>
<li> 

[Pyterssarct](https://github.com/madmaze/pytesseract) (based on Tesseract-OCR) 


</li>
</ul>

## <ins> General Idea: </ins>
The idea of this project is to make the detection is several steps:
<ol>
    <li> Detect the red in the image </li>
    <li> Once red has been detected, detect circles </li>
    <li> Extract the circles (region of interest) </li>
    <li> Perform black detection to only keep the number </li>
    <li> Use a based OCR algorithm (Tesseract-OCR) to recognize the number </li>
    <li> Show a reference sign for the number detected </li>
</ol>

## <ins> Architecture: </ins>
<ul>
    <li>MainTests.py --> contains the code used to test the application in development</li>
    <li>MainRaspberry.py --> contains the code executed when application launched on Raspberry Pi (threads definition
    and call to functions)</li>
    <li>Processing.py --> contains all the function used to pre-process the image before application of OCR</li>
    <li>Recognition --> contains OCR algorithm code</li>
    <li>GUI --> contains the graphical interface code</li>
    <li>OldFunctions.py --> old functions used to develop</li>
    <li>Scripts --> folder that contains scripts used to install the dependencies and to launch application on Raspberry</li>
    <li>Assets --> folder that contains file (images and videos) used to test the application</li>
</ul>
