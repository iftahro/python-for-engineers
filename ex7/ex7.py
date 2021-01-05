''' Exercise #6. Python for Engineers.'''
import sys

sys.setrecursionlimit(10000)


#########################################
# Question 1.a - do not delete this comment
#########################################
def four_bonacci_rec(n):
    if n <= 3:
        return n
    return four_bonacci_rec(n - 1) + four_bonacci_rec(n - 2) + four_bonacci_rec(n - 3) + four_bonacci_rec(n - 4)


#########################################
# Question 1.b - do not delete this comment
#########################################
def four_bonacci_mem(n, memo=None):
    if n <= 3:
        return n
    if memo is None:
        memo = {}
    if n not in memo.keys():
        memo[n] = four_bonacci_mem(n - 1, memo) + \
                  four_bonacci_mem(n - 2, memo) + \
                  four_bonacci_mem(n - 3, memo) + \
                  four_bonacci_mem(n - 4, memo)
    return memo[n]

    #########################################


# Question 2 - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    if n <= 2:
        return n
    if memo is None:
        memo = {}
    if n not in memo.keys():
        memo[n] = climb_combinations_memo(n - 1, memo) + climb_combinations_memo(n - 2, memo)
    return memo[n]


#########################################
# Question 3 - do not delete this comment
#########################################
def catalan_rec(n, memo=None):
    if n == 0:
        return 1
    if memo is None:
        memo = {}
    if n not in memo.keys():
        result = 0
        for i in range(n):
            result += catalan_rec(i) * catalan_rec(n - i - 1)
        memo[n] = result
    return memo[n]


#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    if n == 0:
        return 1
    if len(lst) == 0 or n < 0:
        return 0
    return find_num_changes_rec(n, lst[:-1]) + find_num_changes_rec(n - lst[-1], lst)


#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    if n == 0:
        return 1
    if len(lst) == 0 or n < 0:
        return 0
    if memo is None:
        memo = {}
    key = (n, tuple(lst))
    if key not in memo.keys():
        memo[key] = find_num_changes_mem(n, lst[:-1], memo) + find_num_changes_mem(n - lst[-1], lst, memo)
    return memo[key]
