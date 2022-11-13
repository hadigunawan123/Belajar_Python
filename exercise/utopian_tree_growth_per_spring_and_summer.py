"""
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of SPRING. How tall will the tree be after "n" growth cycles?

For example, if the number of growth cycles is n=5, the calculations are as follows:

Period  Height
0          1 <(FIRST PLANTED) (SPRING), INITIAL 1 METER
1          2 <SPRING
2          3 <SUMMER
3          6 <SPRING
4          7 <SUMMER
5          14 <SPRING
"""


def utopianTree(n):
    tinggi = 1
    print(f"initial height = {tinggi} meter")
    for i in range(1, n+1):
        tinggi = tinggi+1 if i % 2 == 0 else tinggi*2
        print(f'tinggi pohon setelah melewati cycles ke- {i} (which is spring) = {tinggi}' if i %
              2 != 0 else f'tinggi pohon setelah melewati cycles ke- {i} (which is summer) = {tinggi}')
    return tinggi

    # solusi 2, dapet dari org lain, agak sulit dimengerti tp worth to noted here
    # return (2**(n//2+1)-1 if n%2==0 else (2**(n//2+1)-1)*2)


print(
    f'Hasil Total Tinggi Utopian Tree Setelah n = 10 cycles : {utopianTree(10)} Meter')
print("")
print("===CONTOH KE 2===")
print(
    f'Hasil Total Tinggi Utopian Tree Setelah n = 25 cycles : {utopianTree(25)} Meter')
