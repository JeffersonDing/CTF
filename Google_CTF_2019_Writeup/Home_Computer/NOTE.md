# Home Computer
## Mount family.ntfs
Ues ntfs-3g to mount .ntfs file system
```bash
mkdir family
sudo ntfs-3g family.ntfs family
```
## Go though the file system
By using the bash find and grep command to find the files we need.
```bash
find .|grep family
find .|grep Family
```
Indeed we see a directory name **Family** under Users.  
If we go under the Family directory and check each subdirectory with ls -l, we could see that there is a lot of files that are just placeholders with a size of 0.  
Soon found a file called credentials.txt under the documents file that has a size of 58.
```bash
cd documents
cat credentials.txt
I keep pictures of my credentials in extended attributes.
```
This piece of text hints us that there should hidden data under some files within the file system. This is achieved by using something called **Extended Attributes**  
## Extended Attributes
In linux, we could see the extended attributes by using a tool called getfattr, by running it on credentials.txt we get:
```bash
(install)sudo apt-get install attr
getfattr credentials.txt

# file: credentials.txt
user.FILE0
```
Indeed we see that there is data hidden under credentials.txt. Now by using a getfattr flag, we could get the raw bytes of the data by using -D
```bash
getfattr --only-values credentials.txt > raw
```
If we inspect it with a hex editor:
```bash
xxd raw

00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```
we can see it start with our good old png headers. So now we could just open the raw file with eog.
```bash
eog raw
```
## Get the flag
We get the flag in the images we rendered from raw.  
```
CTF{congratsyoufoundmycreds}
```
