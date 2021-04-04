# Tunnel Vision
The challenge gave us an file. Running `file` on it shows that it's a `bmg` image but it's corrupted so we cannot open it. This is probably due to corrupt or wrong headers.  
## Method
Following the [wikipedia](https://en.wikipedia.org/wiki/BMP_file_format) file format specifications for `bmp` I was able to recover after fixing the `header size` and the `The number of color planes` metadata to recover the file.