member_name = input("Add a new member: ")

file = open('members.txt', 'r')
members = file.readlines()
print(members)
file.close()
members.append(f"{member_name}\n")
file = open('members.txt', 'w')
file.writelines(members)
file.close()
