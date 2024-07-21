for num in range(10):
    print(num)

for num in range(0,10,2):
    print(num)

index_count=0

for letter in 'abcdef':
    print('At index {} letter is {}'.format(index_count,letter))
    index_count+=1

#zip function (Makes item into tuple)
word='igec'
for item in enumerate(word):
    print(item)

#zip function (Makes item into tuple)
mylist=[1,2,3,4]
mylist2=['a','b','c','d']

for letter in zip(mylist,mylist2):
    print(letter)


#min and max
anotherlist=[1,2,3,4,5,6,7,8,9]

a=min(anotherlist)
b=max(anotherlist)

print(a)
print(b)


ok_list=[num**2 for num in range(0,11)]
print(ok_list)

quet='ishisafromit'
for it in quet:
    quet.append(it)
    print(x)