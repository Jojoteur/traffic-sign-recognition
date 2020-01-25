clear
echo ""
echo "__________________________________________________"
echo "| This script downloads and installs dependencies|"
echo "|          equired to run the application        |"
echo "|                Created : 30/11/19              |"
echo "|                Updated : 25/01/20              |"
echo "|              Author : BRUNET Julien            |"
echo "———————————————————————————————————–––––––––––––––"
echo ""
echo "--> Updating the Raspberry Pi"
sudo apt-get update && sudo apt-get upgrade -y
echo ""
echo "--> Downloading and installing tesseract-ocr"
sudo apt-get --yes --force-yes install tesseract-ocr
echo ""
echo "--> Downloading and installing libraries for OpenCv"
sudo apt-get install python3-pil.imagetk
sudo apt-get --yes --force-yes install libhdf5-dev libhdf5-serial-dev libhdf5-103
sudo apt-get --yes --force-yes install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt-get --yes --force-yes install libatlas-base-dev
sudo apt-get --yes --force-yes install libjasper-dev
echo ""
echo "--> Downloading and installing pip"
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
echo ""
echo "--> Downloading and installing opencv-python"
sudo pip install opencv-python
echo ""
echo "--> Downloading and installing imutils"
sudo pip install imutils
echo ""
echo "--> Downloading and installing pytesseract"
sudo pip install pytesseract
echo ""
echo "--> Downloading and installing numpy"
sudo pip install numpy
echo ""
echo "--> Installation done"

