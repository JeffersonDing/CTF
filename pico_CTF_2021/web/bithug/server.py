#!/usr/local/env python
#!/ -*- coding: utf-8 -*-

# Acts as a proxy for the requests, that's all, but instead of proxify them performs a redirection
# Redirection is set to http://anti-captcha.com/in.php

import os
import traceback
import time

from flask import Flask, redirect
app = Flask(__name__)

# If you have both 80 and 8080 ports in use, feel free to edit port number
global port
port = 80  # port used by GSA-Anticaptcha and Captcha-Sniper


def portToggle():
    port = 80  # another port used so often


def killPort():
    print("Something went wrong")
    print("Killing app binding port" + str(port))
    try:
        # if can't kill current server use 8080
        os.system("sudo fuser -k " + str(port) + "/tcp")
    except:
        traceback.print_exc()
        portToggle()

# TODO: manage hosts file to bypass every captcha service url


@app.route('/', methods=['POST', 'GET'], defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # return 307 temp redirection to avoid POST calls to being tranformed to GET
    return redirect("http://127.0.0.1:1823/_/ape.git/git-receive-pack", code=307)


def main():
    try:
        print("Running flask webserver on port " + str(port))
        app.run(host='0.0.0.0', port=port)
        time.sleep(2)
    except:
        # traceback.print_exc()
        killPort()
        print("Relaunching " + __name__ + "app")
        time.sleep(2)
        main()


if __name__ == '__main__':
    main()
