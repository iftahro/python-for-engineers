''' Exercise #6. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    if len(s) == 0:
        return ''
    return s[-1] + reverse_string(s[:-1])


#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst: list):
    if len(lst) == 0:
        return -1
    if len(lst) == 1:
        return lst[0]
    if lst[0] > lst[1]:
        lst[1] = lst[0]
    return find_maximum(lst[1:])


#########################################
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    if len(s) == 2:
        return s[0] == s[1]
    if len(s) == 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False


#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_combinations(n - 1) + climb_combinations(n - 2)


#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt=0):
    if len(s) == 0:
        return cnt == 0
    if s[0] == '(':
        cnt += 1
    if s[0] == ')':
        if cnt == 0:
            return False
        cnt -= 1
    return is_valid_paren(s[1:], cnt)
