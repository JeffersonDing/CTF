# Credits to @ZeroDayTea from Discord
import requests
from base64 import b64decode
from base64 import b64encode

# Visualization Tools


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r", text=''):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# CBC bit flipping attack

s = requests.Session()
url = 'http://mercury.picoctf.net:{}/'.format(
    input("Please enter your port number:"))
print("Starting enumeration on {}".format(url))
response = s.get(url)
cookie = s.cookies['auth_name']
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
total = len(cookie)*len(alphabet)
printProgressBar(0, total, prefix='Testing Cookie (0/0):',
                 suffix='Complete', length=50)

for i in range(0, len(cookie)):
    for j, alphchar in enumerate(alphabet):
        newcookie = cookie[:i] + alphchar + cookie[i + 1:]
        curr = i*len(alphabet)+j
        printProgressBar(curr, total, prefix='Testing Cookie ({}/{}):'.format(curr, total),
                         suffix='Index:{} | Letter:{}'.format(i, alphchar), length=50, text=newcookie)
        cookies_dict = {'auth_name': newcookie}
        response = requests.get(
            url, cookies=cookies_dict)
        if "pico" in response.content.decode():
            print(newcookie)
            print("************************")
            print(response.content.decode().split(
                "<code>")[1].split("</code>")[0])
            print("************************")
            exit()
