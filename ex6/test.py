from ex6 import is_valid_paren, climb_combinations, is_palindrome, find_maximum, reverse_string

print(reverse_string("abc") == 'cba')
print(reverse_string("Hello!") == '!olleH')

print(find_maximum([9, 3, 0, 10]) == 10)
print(find_maximum([9, 3, 0]) == 9)
print(find_maximum([]) == -1)

print(is_palindrome("aa") is True)
print(is_palindrome("aa ") is False)
print(is_palindrome("caca") is False)
print(is_palindrome("abcbbcba") is True)

print(climb_combinations(3) == 3)
print(climb_combinations(10) == 89)

print(is_valid_paren("(.(a)") is False)
print(is_valid_paren("p(()r((0)))") is True)
print(is_valid_paren("") is True)