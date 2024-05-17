candles = [4, 4, 1, 3]

#maximum height candles are 4 unit high, there are 2 of them, so return 2
#solusi 1
print(candles.count(max(candles)))

#solusi 2
# runut = sorted(candles)
# max_value = max(candles)

# result = 0
# for i in candles:
#     if i == max_value:
#         result +=1
# print(result)

#solusi 3
# print(len([i for i in candles if i==max(candles)]))