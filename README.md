# Traffic Sign Recognition

This project implements a solution for the detection (and recognition of traffic signs)  
For the moment, we only work on speed limits detection (ie. round with red bounders signs)

## General Idea
The idea of this project is to make the detection is several steps :
<ol>
    <li> Detect the red in the image </li>
    <li> Once red has been detected, detect circles </li>
    <li> Extract the circles (ROI) </li>
    <li> Extract the number to recognize the number with a specific algorithm [WIP] </li>
</ol>


## Get started
### Requirements :
This project needs some external libraries :
<ul>
    <li> opencv </li>
</ul>

Installation via command line :   
```console
$ pip install opencv-python
```

### Launch :
To launch the project, simply run "Main.py"