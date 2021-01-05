import imageio
import matplotlib.pyplot as plt
import numpy as np

from ex10 import ascii_to_np_array, arr_dist, find_best_place, create_image_with_msg, put_message, \
    get_message, read_missions_file, add_daily_gain_col, sum_rewards, find_best_kingdom, find_best_duration

a1 = ascii_to_np_array('Hello')
a2 = ascii_to_np_array('Halmo')
print(arr_dist(a1, a2))
im1 = imageio.imread('parrot.png')
idx = find_best_place(im1, a1)
print(idx)
print(type(idx))
create_image_with_msg(im1, idx, a1)
put_message(im1, "Hello")
im2 = imageio.imread('parrot_encr.png')
get_message(im2)
df = read_missions_file("missions.csv")
add_daily_gain_col(df)
find_best_kingdom(df)
find_best_duration(df)
print(df)
print(sum_rewards(df))


def question_A_test():
    msg1 = 'Hello, NUMPY!'
    orig_file_name = 'parrot.png'

    im1 = imageio.imread(orig_file_name)
    im2 = put_message(im1, msg1)

    plot_image = np.concatenate((im1, im2), axis=1)

    plt.figure()
    plt.imshow(plot_image, cmap=plt.cm.gray)
    plt.show()

    msg2 = get_message(im2)
    return msg2


print(question_A_test() == "Hello, NUMPY!")
