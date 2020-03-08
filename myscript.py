from user import User

# a = User('Alex')
# b = User('Misi')
# c = User('Yato')
#
# a.name = 'Victor'
#
# print(a.name, a.id)
# print(b.name, b.id)
# print(c.name, c.id)

list_of_users = [User() for _ in range(15)]

for user in list_of_users:
    print('id', user.id)