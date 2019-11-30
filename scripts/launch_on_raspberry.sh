cd ../
git pull
sudo find / -type f -name ‘atom.so*’ /usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0
LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0 python3 MainRaspberry.py