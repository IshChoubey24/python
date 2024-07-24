def say_hello(name):
    print(f'Hello {name}')
    print('are')
    print('you')
    
say_hello('ish')


def cal(num_1,num_2):
    return num_1+num_2

result=cal(10,20)
print(result)


#even number
def even_odd(num):
    result=num%2==0
    return result

#even number or not
def check_even_list(num_list):
    
    for num in num_list:
        if num %2 ==0:
            return True
        else:
            pass

    return False

print(check_even_list([1,2,3]))




work_hours=[("Bill",110),("John",220),("Kenedy",50)]



