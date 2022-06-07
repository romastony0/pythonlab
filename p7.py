friends = ['kumar', 'sekar', 'gopal', 'moorthy'];
findNameIndex = friends.index('gopal');
findSekarIndex = friends.index('sekar')

# a) add MCA: at begining of to all name in rhe namelist
for i in range(len(friends)):
    friends[i] = "MCA: "+friends[i]

print(friends);

# b) add ,Bharathiar University at end of all names in the namelist
for i in range(len(friends)):
    friends[i] = friends[i]+", Bharathiar University"

print(friends);

# c) remove gopal from the list
friends.pop(findNameIndex);
print(friends);

# d) add 'Manoj' before two element
friends.insert(2, 'vishwanath')
print(friends)

# e) find 'sekar' in the list, if found abd get the position
print("Sekar position is :",findSekarIndex)

# f) sort the decending order
# for i in reversed(friends):
#     print(i)
reverse = friends.reverse();
print(friends)


# g) clear the element 2 to 3

del friends[2:3];
print(friends)
