clear
echo ""
echo ""
echo "#######################################################################################"
echo "#######################################################################################"
echo "###                                                                                 ###"
echo "###                                                                                 ###"
echo "###   SCRIPT FOR DEPENDENCIES INSTALLATION FOR TRAFFIC SIGN RECOGNITION PROJECT     ###"
echo "###                                                                                 ###"
echo "###                                                                                 ###"
echo "###  This script downloads and installs dependencies required to launch the project ###"
echo "###                                                                                 ###"
echo "###                                                                                 ###"
echo "###                               Created : 30/11/19                                ###"
echo "###                               Updated : 16/12/19                                ###"
echo "###                             Author : BRUNET Julien                              ###"
echo "###                                                                                 ###"
echo "###                                                                                 ###"
echo "#######################################################################################"
echo "#######################################################################################"

echo ""
echo ""

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get --yes --force-yes install tesseract-ocr
sudo apt-get install python3-pil.imagetk
sudo apt-get --yes --force-yes install libhdf5-dev libhdf5-serial-dev libhdf5-103
sudo apt-get --yes --force-yes install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt-get --yes --force-yes install libatlas-base-dev
sudo apt-get --yes --force-yes install libjasper-dev
sudo apt-get --yes --force yes install tesseract-ocr

wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip install opencv-python
sudo pip install imutils
sudo pip install pytesseract
sudo pip install numpy
sudo pip install pytesseract


echo ""
echo ""

echo "#######################################################################################"
echo "#######################################################################################"
echo "###                                                                                 ###"
echo "###                                                                                 ###"
echo "###                             END OF INSTALLATION                                 ###"
echo "###                                                                                 ###"
echo "###                                                                                 ###"
echo "#######################################################################################"
echo "#######################################################################################"

