def valid(pin):
    pin_str = str(pin)
    if len(pin_str) == 4 or len(pin_str) == 6:
        if pin_str.isdigit() == True:
            if ' ' not in pin_str:
                return True
            else:
                return False
        else: 
            return False
    else:
        return False


print(valid(15556))
print(valid(335748))
print(valid('a145'))
print(valid('aaaaaa'))
print(valid('1045'))