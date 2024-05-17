'''
Get the proportions of positif, negative, and zero
'''

arr = [1, 2, -5, 0, -2, -1, 9]

jml_data = len(arr)
#solusi 1
# positif, negatif, nol = 0, 0, 0

# for i in arr:
#     if i > 0:
#         positif += 1
#     elif i < 0:
#         negatif += 1
#     else:
#         nol += 1

# def persentase(data):
#     return data/jml_data
    
# print(persentase(positif), persentase(negatif), persentase(nol)) 
# print((positif/jml_data), (negatif/jml_data), (nol/jml_data)) 


#solusi 2
positif = len([i for i in arr if i>0])
negatif = len([i for i in arr if i<0])
nol = len([i for i in arr if i==0])

print((positif/jml_data), (negatif/jml_data), (nol/jml_data)) 

#solusi 3
# positif = len(tuple(filter(lambda x:x>0, arr)))
# negatif = len(tuple(filter(lambda x:x<0, arr)))
# nol = len(tuple(filter(lambda x:x==0, arr)))

# # print((positif/jml_data), (negatif/jml_data), (nol/jml_data)) 