''' Exercise #5. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def sum_nums(file_name):
    with open(file_name, "r") as file:
        text = file.read()
        numbers = map(int, text.split(" "))
        return sum(numbers)


#########################################
# Question 2 - do not delete this comment
#########################################
def copy_lines_with_str(in_file_name, out_file_name, target_str):
    lines = []
    try:
        with open(in_file_name, "r") as input_file:
            for line in input_file.readlines():
                if target_str in line:
                    lines.append(line)
    except IOError as e:
        return e
    finally:
        with open(out_file_name, "w") as output_file:
            output_file.writelines(lines)


#########################################
# Question 3 - do not delete this comment
#########################################
def write_twin_primes(num, out_file_name):
    if num <= 0:
        raise ValueError("Illegal value num={}".format(num))
    twins = []
    prime_number = 3
    while num > 0:
        if is_num_prime(prime_number) and is_num_prime(prime_number + 2):
            twins.append((prime_number, prime_number + 2))
            num -= 1
        prime_number += 1
    try:
        with open(out_file_name, "w") as file:
            file.writelines(["%s,%s\n" % twin for twin in twins])
    except IOError:
        raise ValueError("Cannot write to {}".format(out_file_name))


def is_num_prime(num: int):
    return not any([num % i == 0 for i in range(2, num)])


#########################################
# Question 4 - do not delete this comment
#########################################
def calc_avg_position_per_band(in_file_name):
    bands_ratings = {}
    with open(in_file_name, "r") as file:
        for line in file.readlines():
            band_name = line.split(",")[1]
            band_ratings = bands_ratings.get(band_name, [])
            band_ratings.append(int(line.split(",")[2]))
            bands_ratings[band_name] = band_ratings
    if len(bands_ratings) < 3:
        raise ValueError("At least one of the bands does not appear in the file {}".format(in_file_name))
    return {band: round(sum(ratings) / len(ratings)) for band, ratings in bands_ratings.items()}
