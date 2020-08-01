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

