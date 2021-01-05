from ex4 import num_courses_per_student, courses_per_student, find_substring_locations, diff_sparse_matrices, \
    most_popular_character

# Q1
print(most_popular_character("HelloWorld") == 'l')
print(most_popular_character('aabbAA') == 'A')
# Q2
print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): -4, (2, 7): 1})
print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 2}]) == {(2, 7): 1})
print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6, (9, 10): 7}, {(2, 7): 0.5, (4, 2): 10}]) == {
    (1, 3): -4, (2, 7): 0.5, (9, 10): -7, (4, 2): -10})
# Q3
print(find_substring_locations('TTAATTAGGGGCGC', 2) == {'TT': [0, 4], 'TA': [1, 5], 'AA': [2], 'AT': [3], 'AG': [6],
                                                        'GG': [7, 8, 9], 'GC': [10, 12], 'CG': [11]})
print(
    find_substring_locations('TTAATTAGGGGCGC', 3) == {'TTA': [0, 4], 'TAA': [1], 'AAT': [2], 'ATT': [3], 'TAG':
        [5], 'AGG': [6], 'GGG': [7, 8], 'GGC': [9], 'GCG': [10], 'CGC': [11]})
# Q4
stud_dict = courses_per_student(
    [('Tom', 'Math'), ('Oxana', 'Chemistry'), ('Scoobydoo', 'python'), ('Tom', 'pYthon'), ('Oxana', 'biology')])
print(stud_dict == {'tom': ['math', 'python'], 'oxana': ['chemistry', 'biology'], 'scoobydoo': ['python']})
num_courses_per_student(stud_dict)
print(stud_dict == {'tom': 2, 'oxana': 2, 'scoobydoo': 1})