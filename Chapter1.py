# must understand difference of bytes,str and unicode.

# Regardless of input type,str or bytes.
# You need Method of being sure to return str.

def to_str(bytes_or_str):
    if isinstance(bytes_or_str,bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # instance of str

# In addition to, You need method of lways return bytes.

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str,str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

# Insted of writing complicated code, using a helper method.

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)
print(repr(my_values))
# >>> {'red':['5'],'green':[''],'blue':['0']}

print('Red:     ',my_values.get('red'))
print('Green:     ',my_values.get('green'))
print('Opacity:     ',my_values.get('opacity'))

# Red:      ['5']
# Green:    ['']
# Opacity:  None

# applying below code to my_values,('red=5&blue=0&green=')....

red = my_values.get('red',[''])[0] or 0
green = my_values.get('green',[''])[0] or 0
opacity = my_values.get('opacity',[''])[0] or 0
print('Red':   %r' % red')
print('Green':   %r' % green')
print('Opacity':   %r' % opacity')

# Red:    '5'
# Green:   0
# Opacity: 0

a = ['a','b','c','d','e','f','g','h']
print('First four',a[:4])
print('Last four',a[-4:])
print('Middle two',a[3::-3])

# First four:['a','b','c','d']
# Last four:['e','f','g','h']
# Middle two:['d','e']

