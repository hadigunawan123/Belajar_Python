"""
HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly 5 people on social media.
On the first day, half of those 5 people (i.e., floor(5/2)=2) like the advertisement and each shares it with 3 of their friends. At the beginning of the second day, floor(5/2)*3= 2*3=6 people receive the advertisement

Each day, floor(recepients/2) of the recipients like the advertisement and will share it with 3 friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.

example:
n=5
Day Shared Liked Cumulative
1      5     2       2
2      6     3       5
3      9     4       9
4     12     6      15
5     18     9      24

The progression is shown above. The cumulative number of likes on the 5th day is 24.

return 24 then.
"""


def viralAdvertising(n):
    # di hari pertama itu 2 orang pasti ngelike ads kita, jd kita gk perlu looping day 1
    like_the_ads = [2]
    for _ in range(n-1):  # kita n-1 karna kita hanya ingin tahu day2 berikutnya, karna day 1 udah pasti 2 yg like
        # kita append dengan data paling akhir dari array, lalu di kali 3, lalu dibagi "floor (//)" setengahnya, karna selalu setengahnya yang mau like, begitu terus sampai hari yg terakhir, contoh floor = 7//2=3, 12//5=2
        like_the_ads.append(like_the_ads[-1]*3//2)
    return sum(like_the_ads)


print(viralAdvertising(5))
print(viralAdvertising(10))
print(viralAdvertising(15))
print(viralAdvertising(365))
