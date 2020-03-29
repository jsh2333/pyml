def reverse(x, y, z):
   return z, y, x

ret = reverse(1, 2, 3)
print(ret)                       # (3, 2, 1)이 출력됨

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1); print(r2); print(r3)      # ‘c’, ‘b’, ‘a’ 순으로 출력됨
