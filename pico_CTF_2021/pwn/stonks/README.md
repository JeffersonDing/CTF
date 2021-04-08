# Stonks

This challenges exploits the `printf` vulnerability. We can leak values from the stack by using decorators such as `%x` which prints reverse hex values.

## Method

In a for loop, loop through the positions on the stack and check whether the leaked data is printable characters. If so, it will be added to the output flag.
