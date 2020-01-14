clear
echo ""
echo ""
echo "This script runs the application"
echo "Created : 30/11/19"
echo "Updated : 05/01/20"
echo "Author : BRUNET Julien"
echo ""
echo ""
cd /home/pi/traffic-sign-recognition
git pull
sudo find / -type f -name ‘atom.so*’ /usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0
LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0 python3 MainRaspberry.py $1
echo ""
echo ""
echo "End of application"