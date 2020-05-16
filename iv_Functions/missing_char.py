def missing_char(str: str, n: int):
    unpacked = [*str]
    unpacked[n]=''
    new_str = ''
    return new_str.join(unpacked)

print(missing_char('code',2))

def missing_char2(str:str,n:int):
    front = str[:n]
    back = str[n+1:]
    return front + back

print(missing_char2('howaboutthat',5))
