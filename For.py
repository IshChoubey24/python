

my_nums=[1,2,3,4,5,6,7,8,9,10]
for loop in my_nums:
    print(loop)

#Check for eveeeen or odd
for num in my_nums:
    if num%2 == 0:
        print(num)
    else:
        print(f'ODD: {num}')

#Sum 
list_sum=0

for num in my_nums:
    list_sum=list_sum+num

    print(list_sum)

mystring='Ish kumar choubey'
for letter in mystring:
    print(letter)

tup=(1,2,3,4,5,6)

for item in tup:
    print(item)

item_list=[(1,2),(3,4),(5,6)]
a=len(item_list)
for item in item_list:
    print(item)
print(a)


#to be specific,if we provide indexing to each value in tuple

for a,b in item_list:
    print(a)


