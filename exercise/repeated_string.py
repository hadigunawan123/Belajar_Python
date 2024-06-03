'''
There is a string, s, of lowercase English letters that is repeated infinitely many times. Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.

Example
s = 'abcac'
n = 10
The substring we consider is abcacabcac, the first 10 characters of the infinite string. There are 4
occurrences of a in the substring.
'''

def repeatedString(s, n):
    # Write your code here
    
    # Hitung jumlah 'a' dalam string s
    count_a_in_s = s.count('a')
    
    # Hitung jumlah pengulangan penuh string s dalam n karakter
    full_repeats = n // len(s)
    
    # Hitung sisa karakter setelah pengulangan penuh
    remainder = n % len(s)
    
    # Hitung total 'a' dari pengulangan penuh
    total_a = full_repeats * count_a_in_s
    
    # Tambahkan jumlah 'a' dalam sisa karakter
    total_a += s[:remainder].count('a')
    
    return total_a

print(repeatedString('a', 1000000000000))
print(repeatedString('aba', 10))