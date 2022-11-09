"""
A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights, and the characters have a maximum height they can jump. There is a magic potion they can take that will increase their maximum jump height by 1 unit for each dose. How many doses of the potion must the character take to be able to jump all of the hurdles. If the character can already clear all of the hurdles, return 0.

Example:
height = [1,2,3,3,2]
k = 1

The character can jump 1 unit high initially and must take "3-1 = 2 OR lets say max(height)-k" doses of potion to be able to jump all of the hurdles.
"""


def hurdleRace(k, height):
    highestHurdle = max(height)
    dosesNeeded = highestHurdle-k
    if abs(dosesNeeded) == 0:
        return 0
    elif highestHurdle < k:
        return 0
    return abs(dosesNeeded)

    # #simpler answer:
    # doses = max(height)-k
    # return doses if doses > 0 else 0


# returning 2 "max(height)-k"
print(hurdleRace(4, [1, 6, 3, 5, 2]))
# returning 0 "5-7=-2" which is (return doses if doses > 0 else 0)
print(hurdleRace(7, [2, 5, 4, 5, 2]))
