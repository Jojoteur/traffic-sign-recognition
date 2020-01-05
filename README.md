# <ins> Traffic Sign Recognition : </ins>

This project implements a solution for the detection (and recognition of traffic signs) on a Raspberry Pi.  

For the moment, we only work on speed limits detection (ie. round with red bounders signs)

This Readme is a summary, for more informations, you can read the wiki associated to the project on the repository : https://gitlab.com/julienbrunet21/traffic-sign-recognition/wikis/wiki/home

## <ins> Compatibility : </ins>
This project has been developed to work with **Python 3.7**

It uses some external libraries :
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

## <ins> General Idea : </ins>
The idea of this project is to make the detection is several steps :
<ol>
    <li> Detect the red in the image </li>
    <li> Once red has been detected, detect circles </li>
    <li> Extract the circles (region of interest) </li>
    <li> Perform black detection to only keep the number </li>
    <li> Use a based OCR algorithm (Tesseract-OCR) to recognize the number </li>
    <li> Show a reference sign for the number detected </li>
</ol>
