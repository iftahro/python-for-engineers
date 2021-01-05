''' Exercise #9. Python for Engineers.'''

import numpy as np
import imageio
import math


#########################################
# Question 1 - do not delete this comment
#########################################

class Roman:
    def get_int_from_roman(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_string = self.roman_value.strip('-')
        int_val = 0
        for counter in range(len(roman_string)):
            if counter > 0 and rom_val[roman_string[counter]] > rom_val[roman_string[counter - 1]]:
                int_val += rom_val[roman_string[counter]] - 2 * rom_val[roman_string[counter - 1]]
            else:
                int_val += rom_val[roman_string[counter]]
        int_val = -int_val if self.is_neg else int_val
        return int_val

    def get_roman_from_int(self):
        num = self.int_value if not self.is_neg else -self.int_value
        roman_num = '' if not self.is_neg else '-'
        counter = 0

        roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        int_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        while num > 0:
            for _ in range(num // int_vals[counter]):
                roman_num += roman_char[counter]
                num -= int_vals[counter]
            counter += 1
        return roman_num

    def __init__(self, input_value):
        if isinstance(input_value, int):
            self.is_neg = input_value < 0
            self.int_value = input_value
            self.roman_value = self.get_roman_from_int()
        elif isinstance(input_value, str):
            self.is_neg = input_value.startswith('-')
            self.roman_value = input_value
            self.int_value = self.get_int_from_roman()

    def __str__(self):
        return f"The integer value is {self.int_value} " \
               f"and the Roman Numeral is denoted by '{self.roman_value}'"

    def __repr__(self):
        return self.roman_value

    def __neg__(self):
        return Roman(-self.int_value)

    def __add__(self, other):
        if isinstance(other, Roman):
            value = self.int_value + other.int_value
        elif isinstance(other, int):
            value = self.int_value + other
        if value == 0:
            raise ValueError("There is no representation of the digit 0 in Roman numbers!")
        return Roman(value)

    def __lt__(self, other):
        if isinstance(other, Roman):
            return self.int_value < other.int_value
        elif isinstance(other, int):
            return self.int_value < other

    def __gt__(self, other):
        if isinstance(other, Roman):
            return self.int_value > other.int_value
        elif isinstance(other, int):
            return self.int_value > other

    def __floordiv__(self, other):
        if isinstance(other, Roman):
            value = self.int_value // other.int_value
        elif isinstance(other, int):
            value = self.int_value // other
        if value == 0:
            raise ValueError("Divide value is 0!")
        return Roman(value)


#########################################
# Question 2 - do not delete this comment
#########################################

def load_training_data(filename):
    n = np.loadtxt(filename, delimiter=",", dtype="str")
    return {
        "column_names": n[0][1:],
        "row_names": n[:, 0][1:],
        "data": n[1:, 1:].astype(float)
    }


def get_highest_weight_loss_trainee(data_dict):
    change = data_dict["data"][:, 0] - data_dict["data"][:, -1]
    index = np.argmax(change)
    return data_dict["row_names"][index]


def get_diff_data(data_dict):
    return data_dict["data"][:, 1:] - data_dict["data"][:, :-1]


def get_highest_loss_month(data_dict):
    diffs = get_diff_data(data_dict)
    diffs_sum = diffs.sum(axis=0)
    return data_dict["column_names"][np.argmin(diffs_sum) + 1]


def get_relative_diff_table(data_dict):
    return get_diff_data(data_dict) / data_dict["data"][:, :-1]


#########################################
# Question 3 - do not delete this comment
#########################################

def compute_entropy(img):
    im = imageio.imread(img)
    histogramdd = np.histogramdd(np.ravel(im), bins=256)[0] / im.size
    entropy = 0
    for h in histogramdd:
        if h != 0:
            entropy += -h * math.log2(h)
    return entropy


def nearest_enlarge(img, a):
    im = imageio.imread(img)
    new_rows = im.shape[0] * a
    new_cols = im.shape[1] * a
    new_mat = np.zeros((new_rows, new_cols))

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            new_mat[i * a:i * a + 3, j * a: j * a + 3] = im[i, j]

    return new_mat
