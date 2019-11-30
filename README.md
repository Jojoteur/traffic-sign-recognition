# <ins> Traffic Sign Recognition : </ins>

This project implements a solution for the detection (and recognition of traffic signs) on a Raspberry Pi.  

For the moment, we only work on speed limits detection (ie. round with red bounders signs)

This Readme is a summary, for more informations, you can read the wiki associated to the project on the repository : https://gitlab.com/julienbrunet21/traffic-sign-recognition/wikis/wiki/home

## <ins> Compatibility : </ins>
This project has been developed to work with **Python 3.7**

It uses some external librairies :
<ul>
    <li> opencv </li>
    <li> imutils </li>
    <li> numpy </li>
    <li> pytesseract (require tesseract-ocr installed)</li>
</ul>

## <ins> General Idea : </ins>
The idea of this project is to make the detection is several steps :
<ol>
    <li> Detect the red in the image </li>
    <li> Once red has been detected, detect circles </li>
    <li> Extract the circles (ROI) </li>
    <li> Extract the number to recognize the number with a specific algorithm [WIP] </li>
</ol>
