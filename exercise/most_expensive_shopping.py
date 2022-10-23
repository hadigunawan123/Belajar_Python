"""
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.

budget = 60
keyboards = [40,50,60]
drives = [5,8,12]

The person can buy a 40 "keyboards" + 12 "drives" = 52, or a 50 "keyboards" + 8 "drives" = 58. Choose the latter as the more expensive option and return 58.
return -1 if "keyboards"+"drives" > "budget"
"""


def getMoneySpent(keyboards, drives, budget):
    spendings = []
    for i in keyboards:
        for j in drives:
            spendings.append(i+j)
    print(spendings)

    sorted_spendings = sorted(spendings)
    for spent in sorted_spendings[::-1]:
        if budget-spent >= 0:
            return spent
    return -1

    # SOLUSI 2
    # spendings = [k+d for k in keyboards for d in drives]
    # spendings.append(-1)
    # return max([x for x in spendings if x <= budget])


budget = 10
keyboards = [3, 1]
drives = [5, 2, 8]

budget2 = 5
keyboards2 = [4]
drives2 = [5]

printcoy = getMoneySpent(keyboards, drives, budget)
printcoy2 = getMoneySpent(keyboards2, drives2, budget2)
print(f"Maximal spent money if budget >= spending {printcoy}")
print("="*10)
print(f"Maximal spent money if budget < spending {printcoy2}")
