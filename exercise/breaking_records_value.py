scores_list = [5, 5, 4, 7, 10, 10, 10, 12, 9, 25, 9, 8, 2, 1]


def breakingRecords(scores):
    # Write your code here
    low, high = scores[0], scores[0]
    n_low, n_high = 0, 0

    for i in scores[1:]:
        if i < low:
            low = i
            n_low += 1
        elif i > high:
            high = i
            n_high += 1
        # code diatas bisa disingkat pakai ternary, seperti dibawah ini:
        # low, n_low = (i, n_low+1) if  i<low else (low, n_low)
        # high, n_high = (i, n_high+1) if  i>high else (high, n_high)
    return n_high, n_low


print(breakingRecords(scores_list))
