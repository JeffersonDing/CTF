# Whats your Input
This is a python2 input vuln. We know that python2 input is basically `eval(raw_input(prompt))`
## Method
For the second user input, just type `city` since we know that it will evaluated to whatever randm city it chose and thus printing the flag.
