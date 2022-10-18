"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly "STEPS" steps, for every step it was noted if it was an uphill, "U", or a downhill, "D" step. Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example
steps = 8, path = [DDUUUUDD]
The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain  units high. Finally, the hiker returns to sea level and ends the hike.

Function Description : Complete the countingValleys function in the editor below.

countingValleys has the following parameter(s):
-int steps: the number of steps on the hike
-string path: a string describing the path

Returns
-int: the number of valleys traversed
"""


"""
Sample Input:
8
UDDDUDUU

Sample Output:
1

Explanation:
If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

_/\      _
   \    /
    \/\/
The hiker enters and leaves one valley.
"""


def countingValleys(steps, path):
    valley_count = 0
    sea_level = 0
    # dictionary utk memberikan representasi integer dari value "path"
    cases = {"U": 1, "D": -1}
    for i in path:
        if sea_level > 0:
            sea_level += cases[i]
            continue  # utk mengabaikan code dibawahnya, agar "hill" tdk dihitung jd valley_count
        # karna sea_level = 0, maka harusnya di awal running, code dibawah yg akan proses terlebih dahulu
        sea_level += cases[i]
        if sea_level == 0:
            valley_count += 1

    return valley_count


path_mentah = "U,D,D,D,U,D,U,U"  # Up / Down
path = path_mentah.split(",")
steps = len(path)
print(path)

print(countingValleys(steps, path))
