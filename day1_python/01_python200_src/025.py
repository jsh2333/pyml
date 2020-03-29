bit1 = 0x61
bit2 = 0x62
print(hex(bit1 & bit2))    # 0x60이 출력됨
print(hex(bit1 | bit2))     # 0x63이 출력됨
print(hex(bit1 ^ bit2))     # 0x3 이 출력됨
print(hex(bit1 >> 1))      # 0x30이 출력됨
print(hex(bit1 << 2))      # 0x184가 출력됨
