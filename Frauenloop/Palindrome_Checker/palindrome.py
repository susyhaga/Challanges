def isPalindrome(a):
    a_str = str(a)
    return a_str == a_str[::-1]

print(isPalindrome('ana'))
print(isPalindrome('1112'))
print(isPalindrome('14541'))
print(isPalindrome('amrssa'))