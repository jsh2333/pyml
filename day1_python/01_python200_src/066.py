bnum = 0b11110000; bstr = '0b11110000'
onum = 0o360; ostr = '0o360'
hnum = 0xf0; hstr = '0xf0'
b1 = int(bnum); b2 = int(bstr, 2)   # b2 = int(bstr, 0)로도 가능
o1 = int(onum); o2 = int(ostr, 8)   # o2 = int(ostr, 0)로도 가능
h1 = int(hnum); h2 = int(hstr, 16)  # h2 = int(hstr, 0)로도 가능
print(b1); print(b2)
print(o1); print(o2)
print(h1); print(h2)
