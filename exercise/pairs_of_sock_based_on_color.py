def sockMerchant(n, ar):
    # ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    # n = len(ar) = 9
    unique_color = set(ar)  # (10,20,30,50)
    number_of_pairs = 0
    for warna in unique_color:
        # "//2" always give int and rounded down, example: 3//2 = 1, 5//2 = 2
        number_of_pairs += len([sock for sock in ar if warna == sock])//2

    return number_of_pairs


ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = len(ar)

print(
    f"Banyaknya pasangan kaus kaki dalam list tsb adalah: {sockMerchant(n, ar)}")
