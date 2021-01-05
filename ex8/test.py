from ex8 import Minibar, Room, Hotel

m = Minibar({'coke': 10, 'lemonade': 7}, {'bamba': 8, 'mars': 12})
rooms = [Room(m, 15, 140, [], 5, 1), Room(m, 12, 101, ["Ronen", "Shir"], 6, 2),
         Room(m, 1, 2, ["Liat"], 7, 1), Room(m, 2, 23, [], 6, 3)]
h = Hotel("Dan", rooms)
test_sep = '\n------------------'
print('PRINT h:\n', h, test_sep, sep="")
print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
print('CALL: h.check_in(["Alice", "Wonder"], 2)\n', h.check_in(["Alice", "Wonder"], 2), test_sep, sep="")
print('CALL: h.check_in(["Alex"], 3)\n', h.check_in(["Alex"], 3), test_sep, sep="")
print('PRINT h:\n', h, test_sep, sep="")
print('CALL: h.check_in(["Oded", "Shani"], 3)\n', h.check_in(["Oded", "Shani"], 3), test_sep, sep="")
print('CALL: h.check_in(["Oded", "Shani"], 1)\n', h.check_in(["Oded", "Shani"], 1), test_sep, sep="")
print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
print('PRINT h:\n', h, test_sep, sep="")