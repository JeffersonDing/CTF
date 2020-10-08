# Satelite
## Find Entry Pass
Find statelite name from README.pdf => "Osmium"
## Find Login Credentials
Run init_sat select function a and get Google docs link.
Get string
```
VXNlcm5hbWU6IHdpcmVzaGFyay1yb2NrcwpQYXNzd29yZDogc3RhcnQtc25pZmZpbmchCg==
```
Base 64 decode
```bash
echo VXNlcm5hbWU6IHdpcmVzaGFyay1yb2NrcwpQYXNzd29yZDogc3RhcnQtc25pZmZpbmchCg==|base64 --decode
```
get user name and password
```
Username: wireshark-rocks
Password: start-sniffing!
```
## Snif Connections
1. Check what connectons init_sat is making
```bash
netstat -tnpa | grep init_sat
```
### netstat flags
* -a Shows the state of all sockets
* -p Show connections or statistics only for a particular protocol
2. Get TCP connection IP and ports
```
*.*.*.*:1337 (* is hidden)
```
3. Wireshark and analyze packages
```bash
wireshark
```
Apply port filter to 1337
^F to search for "CTF" string
4. tcpdump
```bash
tcpdump -nA port 1337 | grep CTF{
```
### tcpdump flags
* -n Dont convert adress
* -A Print packages to ASCII
## Get Flag
```
CTF{4efcc72090af28fd33a2118985541f92e793477f}
```
