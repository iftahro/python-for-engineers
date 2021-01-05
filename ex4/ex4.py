''' Exercise #4. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def most_popular_character(my_string):
    chars = {}
    for char in my_string:
        chars[char] = chars.get(char, 0) + 1
    values = sorted(chars.values())
    popular = [key for key, value in chars.items() if value == values[-1]]
    return min(popular)


#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):
    new_dict = lst[0]
    for dictionary in lst[1:]:
        for key, value in dictionary.items():
            new_dict[key] = new_dict.get(key, 0) - value
    return {key: value for key, value in new_dict.items() if value != 0}


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
    result = {}
    for i in range(len(s) - k + 1):
        key = s[i:i + k]
        if key not in result.keys():
            result[key] = [i]
        else:
            result[key].append(i)
    return result


#########################################
# Question 4 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):
    result = {}
    for pair in tuples_lst:
        student, course = pair[0].lower(), pair[1].lower()
        if student not in result.keys():
            result[student] = [course]
        else:
            result[student].append(course)
    return result


def num_courses_per_student(stud_dict):
    for key, value in stud_dict.items():
        stud_dict[key] = len(value)
