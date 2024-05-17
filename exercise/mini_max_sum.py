arr = [1, 3, 5, 7, 9]

#the minimum sum is 1+3+5+7 = 16
#the maximum sum is 3+5+7+9 = 24
#return 16 24
# solusi 1
# mini, maxi = arr[0], arr[0]

# for i in arr:
#     if i<mini:
#         mini=i
#     elif i>maxi:
#         maxi=i
# print(sum(arr)-maxi, sum(arr)-mini)

#solusi 2
arr.sort() #fungsi sort akan menghasilkan "inplace" pada listnya
print(sum(arr[:-1]), sum(arr[1:]))

#solusi 3
# runut = sorted(arr) #fungsi sorted akan menghasilkan list baru
# print(sum(arr[:-1]), sum(arr[1:]))

#solusi 4
# print(sum(arr)-max(arr), sum(arr)-min(arr))