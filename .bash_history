openssh
openssl
sudo su
kITKAT445
wget http://swupdate.openvpn.org/as/openvpn-as-2.0.7-Ubuntu12.amd_64.deb
sudo wget http://swupdate.openvpn.org/as/openvpn-as-2.0.7-Ubuntu12.amd_64.deb
sudo su
sudo ./openvpn-ubuntu-install.sh
nano openvpn-ubuntu-install.sh
sudo systemctl stop openvpn-server@server.service
sudo systemctl start openvpn-server@server.service
sudo su
