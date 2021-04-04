# Microsoft Weekedge
Given a Microsoft Power-point file. Tried regular enumeration techniques like `strings`, opening the file and looking for templates, macros etc.   
After some research, realized that PPT files are just archives and could be unziped to see inner content.  
## Method
Unzipped the `.ppt` file and looked through folders and files found a file called `hidden`. Inside was base64 encoded flag.