from ex7 import find_num_changes_mem, find_num_changes_rec, catalan_rec, climb_combinations_memo, four_bonacci_mem, \
    four_bonacci_rec

print(four_bonacci_rec(0) == 0)
print(four_bonacci_rec(5) == 12)
print(four_bonacci_rec(8) == 85)

# Question 1.b tests - you can and should add more

print(four_bonacci_mem(0) == 0)
print(four_bonacci_mem(5) == 12)
print(four_bonacci_mem(8) == 85)

# Question 2 tests - you can and should add more

print(climb_combinations_memo(4) == 5)
print(climb_combinations_memo(7) == 21)
print(climb_combinations_memo(42) == 433494437)

# Question 3 tests - you can and should add more

cat_list = [1, 1, 2, 5, 14, 42, 132, 429]
for n, res in enumerate(cat_list):
    print(catalan_rec(n) == res)

# Question 4.a tests - you can and should add more

print(find_num_changes_rec(5, [1, 2, 5, 6]) == 4)
print(find_num_changes_rec(4, [1, 2, 5, 6]) == 3)
print(find_num_changes_rec(1, [2, 5, 6]) == 0)
print(find_num_changes_rec(-1, [1, 2, 5, 6]) == 0)
print(find_num_changes_rec(0.9, [1, 2, 5, 6]) == 0)
print(find_num_changes_rec(105, [1, 105, 999, 100]) == 3)

# Question 4.b tests - you can and should add more

print(find_num_changes_mem(5, [1, 2, 5, 6]) == 4)
print(find_num_changes_mem(4, [1, 2, 5, 6]) == 3)
print(find_num_changes_mem(1430, [1, 2, 5, 6, 13]) == 231919276)
print(find_num_changes_mem(105, [1, 105, 999, 100]) == 3)