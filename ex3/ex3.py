''' Exercise #3. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def sum_divisible_by_k(lst, k):
    return sum([num for num in lst if num % k == 0])


#########################################
# Question 2 - do not delete this comment
#########################################
def mult_odd_digits(n):
    result = 1
    while n > 0:
        num = n % 10
        if num % 2 == 1:
            result *= num
        n //= 10
    return result


#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):
    result = 0
    counter = 0
    for char in s:
        if char == c:
            counter += 1
        else:
            result = counter if counter > result else result
            counter = 0
    return result or counter


#########################################
# Question 4 - do not delete this comment
#########################################
def upper_strings(lst):
    if not isinstance(lst, list):
        return -1
    for i in range(len(lst)):
        if isinstance(lst[i], str):
            lst[i] = lst[i].upper()


#########################################
# Question 5 - do not delete this comment
#########################################
def div_mat_by_scalar(mat, alpha):
    new_mat = []
    for row in mat:
        new_row = []
        for num in row:
            new_row.append(num // alpha)
        new_mat.append(new_row)
    return new_mat


#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    new_mat = []
    for i in range(len(mat[0])):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[j][i])
        new_mat.append(new_row)
    return new_mat
