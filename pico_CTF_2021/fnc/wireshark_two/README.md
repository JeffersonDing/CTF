# Wireshark Two
Given a `.pcapng` file. Open it in wireshark and we see a lot of traffic. 
## Intuition
Looking at the packets, a lot of them had flag like strings in them such as `picoCTF{a97d3ee943221888bd1157429e4a00ed5e9905a610e64664f7e36c7f5e0a4ef9}` which was a distraction. Then I saw that there were also a lot of `DNS` quires to weird destinations involving `red shrimp and herring`. 
## Method
Taking a deeper look at these DNS records, we see that it's all going to similar domains but the subdomain part is random characters that looks like `base 64`. I tried to capture some of them but a lot was gibberish.  
A further look revealed that only some DNS records are pointing to a different destination IP and by using wireshark filters, I was able to filter them out. By concatenating the subdomain name and decoding using `b64` was able to recover flag.