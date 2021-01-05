''' Exercise #8. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
class Minibar:
    def __init__(self, drinks, snacks):
        self.drinks = drinks
        self.snacks = snacks
        self.bill = 0

    def __repr__(self):
        return f"The minibar contains the drinks: {[drink for drink in self.drinks.keys()]}\n" \
               f"And the snacks: {[snack for snack in self.snacks.keys()]}\n" \
               f"The bill for the minibar is: {self.bill}"

    def eat_a_snack(self, snack):
        if snack not in self.snacks.keys():
            raise ValueError("The snack is not in the minibar")
        price = self.snacks.pop(snack)
        self.bill += price

    def drink_a_drink(self, drink):
        if drink not in self.drinks.keys():
            raise ValueError("The drink is not in the minibar")
        price = self.drinks.pop(drink)
        self.bill += price


#########################################
# Question 2 - do not delete this comment
#########################################
class RoomError(Exception):
    pass


class Room:
    def __init__(self, minibar, floor, number, guests, clean_level, rank, satisfaction=1.0):
        if not isinstance(clean_level, int) or not isinstance(rank, int) or not isinstance(satisfaction, (int, float)):
            raise TypeError()
        if not 1 <= clean_level <= 10 or not 1 <= rank <= 3 or not 1 <= satisfaction <= 5:
            raise ValueError()
        self.minibar = minibar
        self.floor = floor
        self.number = number
        self.guests = [guest.lower() for guest in guests]
        self.clean_level = clean_level
        self.rank = rank
        self.satisfaction = float(satisfaction)

    def __repr__(self):
        return f"{self.minibar}\n" \
               f"floor: {self.floor}\n" \
               f"number: {self.number}\n" \
               f"guests: {', '.join(self.guests) or 'empty'}\n" \
               f"clean_level: {self.clean_level}\n" \
               f"rank: {self.rank}\n" \
               f"satisfaction: {float(round(self.satisfaction))}"

    def is_occupied(self):
        return len(self.guests) > 0

    def clean(self):
        self.clean_level = min(10, self.clean_level + self.rank)

    def better_than(self, other):
        if not isinstance(other, Room):
            raise TypeError("Other must be an instance of Room")
        return (self.rank, self.floor, self.clean_level) > (other.rank, other.floor, other.clean_level)

    def check_in(self, guests):
        if self.is_occupied():
            raise RoomError("Cannot check-in new guests to an occupied room")
        self.guests = [guest.lower() for guest in guests]
        self.satisfaction = 1.0

    def check_out(self):
        if not self.is_occupied():
            raise RoomError("Cannot check-out an empty room")
        self.guests = []

    def move_to(self, other):
        if not self.is_occupied():
            raise RoomError("Cannot move guests from an empty room")
        if other.is_occupied():
            raise RoomError("Cannot move guests into an occupied room")
        other.guests = self.guests
        if other.better_than(self):
            other.satisfaction = min(5.0, self.satisfaction + 1.0)
        else:
            other.satisfaction = self.satisfaction
        self.check_out()


#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def __repr__(self):
        return f"{self.name} hotel has:\n" \
               f"{len(self.rooms)} rooms\n" \
               f"{len([room for room in self.rooms if room.is_occupied()])} occupied rooms"

    def check_in(self, guests, rank):
        for room in self.rooms:
            if room.rank == rank and not room.is_occupied():
                room.check_in(guests)
                return room
        return None

    def check_out(self, guest):
        room = self._find_room(guest)
        if room:
            room.check_out()
        return room

    def upgrade(self, guest):
        room = self._find_room(guest)
        if room:
            for other_room in self.rooms:
                if other_room.better_than(room) and not other_room.is_occupied():
                    room.move_to(other_room)
                    return other_room
        return None

    def _find_room(self, guest):
        for room in self.rooms:
            if guest.lower() in room.guests:
                return room
        return None
