clear
echo ""
echo ""
echo "#######################################################################################"
echo "#######################################################################################"
echo "#######################################################################################"
echo "###### SCRIPT FOR DEPENDENCIES INSTALLATION FOR TRAFFIC SIGN RECOGNITION PROJECT ######"
echo "#######################################################################################"
echo "#######################################################################################"
echo "#######################################################################################"
echo ""
echo ""
echo "######                 STEP 1 : Update and Upgrade of the system                 ######"
sudo apt-get update && sudo apt-get upgrade -y
echo ""
echo ""
echo "######            STEP 2 : Download and installation of tesseract-ocr            ######"
sudo apt-get --yes --force-yes install tesseract-ocr
echo ""
echo ""
echo "######       STEP 3 : Download and installation of dependencies for opencv       ######"
sudo apt-get --yes --force-yes install libhdf5-dev libhdf5-serial-dev libhdf5-103
sudo apt-get --yes --force-yes install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt-get --yes --force-yes install libatlas-base-dev
sudo apt-get --yes --force-yes install libjasper-dev
echo ""
echo ""
echo "######                STEP 4 : Download and install pip function                 ######"
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
echo""
echo""
echo"###### STEP 5 : Download and install opencv-python, imutils, pytesseract and numpy ######"
sudo pip install opencv-python
sudo pip install imutils
sudo pip install pytesseract
sudo pip install numpy
echo "#######################################################################################"
echo "#######################################################################################"
echo "#######################################################################################"
echo "######                              FINISH                                       ######"
echo "#######################################################################################"
echo "#######################################################################################"
echo "#######################################################################################"
