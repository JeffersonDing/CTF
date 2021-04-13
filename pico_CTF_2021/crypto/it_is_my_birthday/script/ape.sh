#!/bin/bash
sha1sum a.pdf
sha1sum b.pdf
sha1sum invite.pdf
echo "***********************************"
tail -c 1000 invite.pdf > 1000bytes
truncate --size=320 a.pdf
truncate --size=320 b.pdf
cat a.pdf 1000bytes > a_out.pdf
cat b.pdf 1000bytes > b_out.pdf
sha1sum a_out.pdf
sha1sum b_out.pdf