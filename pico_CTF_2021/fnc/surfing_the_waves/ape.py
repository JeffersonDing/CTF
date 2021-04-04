# Full credit to @ZeroDayTea
from scipy.io import wavfile

samplerate, data = wavfile.read('main.wav')

rounded_data = []
unique = []
for i in data:
    r = round(i, -2)
    rounded_data.append(r)
    if r in unique:
        continue
    else:
        unique.append(r)
unique.sort()

flag_hex = []
for a in rounded_data:
    flag_hex.append(hex(unique.index(a))[2:])

print(bytearray.fromhex("".join(flag_hex)).decode())
