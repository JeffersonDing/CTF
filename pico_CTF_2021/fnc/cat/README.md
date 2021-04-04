# Cat
This challenge gives us an image. By enumerating through regular forensics techniques such as `strings`,`hexdump`, `exiftool` etc. we are able to see that there are some metadata that has been modified.   
## Method
By running `exiftool` and focusing on the metadata again, we see that the XMP licence is custom and has a name of `picoCTF`. Looking at it's licence, we can identify a base 64 encoded string which will be our flag.