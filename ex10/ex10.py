''' Exercise #10. Python for Engineers.'''

import numpy as np
import pandas as pd


#########################################
# Question 1 helper functions - do not delete
# this comment or change these functions
#########################################

def np_array_to_ascii(darr):
    return ''.join([chr(item) for item in darr])


def ascii_to_np_array(s):
    return np.frombuffer(s.encode(), dtype=np.uint8)


#########################################
# Question 1 - do not delete this comment
#########################################


# 1----------------------------------------------------------------------------
def arr_dist(a1, a2):
    return sum(np.absolute(a1.astype(int) - a2.astype(int)))


# 2----------------------------------------------------------------------------
def find_best_place(im, np_msg):
    shape = im.shape
    ravel = im.ravel()
    dst, index = arr_dist(np_msg, ravel[:len(np_msg)]), 0
    for i in range(len(ravel) - len(np_msg) + 1):
        current_dist = arr_dist(np_msg, ravel[i:i + len(np_msg)])
        if current_dist < dst:
            index = i
            dst = current_dist
    return index // shape[1], index % shape[1]


# 3----------------------------------------------------------------------------
def create_image_with_msg(im, img_idx, np_msg):
    copy = im.copy()
    shape = copy.shape
    ravel = copy.ravel()
    index = img_idx[0] * shape[1] + img_idx[1]
    ravel[index: index + len(np_msg)] = np_msg
    copy[0, 0] = img_idx[0]
    copy[0, 1] = img_idx[1]
    copy[0, 2] = len(np_msg)
    return copy


# 4----------------------------------------------------------------------------
def put_message(im, msg):
    np_msg = ascii_to_np_array(msg)
    idx = find_best_place(im, np_msg)
    return create_image_with_msg(im, idx, np_msg)


# 5----------------------------------------------------------------------------
def get_message(im):
    row, column, length = im[0, 0], im[0, 1], im[0, 2]
    ravel_index = row * im.shape[1] + column
    return np_array_to_ascii(im.ravel()[ravel_index:ravel_index + length])


#########################################
# Question 2 - do not delete this comment
#########################################

# A----------------------------------------------------------------------------
def read_missions_file(file_name):
    try:
        return pd.read_csv(file_name, index_col=0)
    except IOError:
        raise IOError("An IO error occurred")


# B----------------------------------------------------------------------------
def add_daily_gain_col(bounties):
    bounties["Daily gain"] = (bounties.Bounty - bounties.Expenses) / bounties.Duration


# C----------------------------------------------------------------------------
def sum_rewards(bounties):
    return sum(bounties.Bounty - bounties.Expenses)


# D----------------------------------------------------------------------------
def find_best_kingdom(bounties):
    add_daily_gain_col(bounties)
    return bounties['Daily gain'].idxmax()


# E----------------------------------------------------------------------------
def find_best_duration(bounties):
    add_daily_gain_col(bounties)
    duration_df = bounties.groupby(['Duration']).mean()
    return duration_df['Daily gain'].idxmax()
