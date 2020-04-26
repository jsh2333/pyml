# pip install pickle-mixin
# https://wikidocs.net/83
import pickle
users = {'idabc':'123', 'idefg':'345', 'iddda':'567'}
f = open('pickle_users.txt', 'w')

pickle.dump(users, f)
f.close()


f = open('pickle_users.txt')
a = pickle.load(f)
print(a)
