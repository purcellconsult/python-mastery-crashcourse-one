from enum import Enum

class DayOfWeek(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


print(type(DayOfWeek.Monday))	                 # get the type it belongs to

print(isinstance(DayOfWeek.Tuesday, DayOfWeek))  # True 

print(DayOfWeek.Monday)				 # DayOfWeek.Monday

print(repr(DayOfWeek.Tuesday))			 # <DayOfWeek.Tuesday: 2>


# iterating over an enum

for day in DayOfWeek:
    print(day)