def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'    
a=old_macdonald('ishaa')

print(a)


def reverse(sent):
    return  ' '.join(sent.split()[::-1])

print(reverse('i am a sent'))


a = float(input())
b = float(input())
c = a * b
print(c)

