# Trivial Flag Transfer Protocol
Looking at the name of the challenge, it's probably sending data using `TFTP`. We import the `.pcap` into wireshark and see that indeed, there is `TFTP` traffic going on.
## Method
We can extract objects using wireshark and if we select TFTP, we see that wireshark detected a couple of files. `instructions`, `plan`, `program` and 3 pictures. Running `file` on the program file shows us it's a `.deb` file and it's installing `steghide`. This means that the flag is hidden in the images using `steghide`  
The plan and instructions didn't look like anything but after a while I realized that it's just a cipher. Passing it through a online cracker or in my case, the `caesar` command from the command line did the job.  
We recovered the passphrase for the `steghide` all we need to do is extract the data. 