
data2 = b"\xf1\xa7\xf0\x07\xed"
data = b"\x9dn\x93\xc8\xb2\xb9A\x8b\x94\xc6\xdf3\xc0\xc5\x95\xde7\xc3\x9f\x93\xdf?\xc9\xc3\xc2\x8c2\x93\x90\xc1\x8ee\x95\x9f\xc2\x8c6\xc8\x95\xc0\x90\x00\x00"
out = bytearray()
for i, c in enumerate(data):
    char = data2[4 - (i % 5)]
    out.append(c ^ char)
print(out)