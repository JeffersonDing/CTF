# It is my birthday

This challenge is regarding a `SHA-1` collision on PDF documents. Looking at the hint `shattered.io` we see that it is possible for 2 different PDF files to have identical `SHA1` hashes. But for this challenge, it has to have the same last 1000 bytes as the original invite.

## Method

To solve this challenge, I first found 2 SHA1 colliding PDF from the internet(you can use a generator or even the provided example from shattered.io). Looking at it's raw bytes in `hexedit` we can clearly differentiate the header the content and the footer data. By testing around, I realized that the raw data and the footer in my 2 files are identical. Theoretically, If I remove them, the file should still be SHA1 collided because I just remove the same data from both files. In fact, that was the case and I just simply added the last 1000 bytes, which contains some data(mostly empty `00` bytes) and the footer, to the 2 PDF files. Because it was already SHA1 collided, we added the same data to both, it still remains a collision.
