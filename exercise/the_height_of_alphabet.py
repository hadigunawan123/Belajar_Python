"""
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle (lets say). In this PDF viewer, each word is highlighted independently. For example:

abc is higlighed in blue, cause they are 1 phrases

There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given (h parameter).

example:
h = [1,2,2,3,3,3,3,3,3,3,3,2,2,2,2,4,4,4,4,4,5,6,6,6,6,6], len(h) = 26, pas dgn jumlah alfabet
word = "hadi"
the heights are h=3, a=1, d=3, i=3
paling tinggi maka 3
3*len(word) = 3*4 = 12
that's it, 12 is the answer
"""


def designerPdfViewer(h, word):
    alfabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    dictku = {key: value for key, value in zip(alfabet, h)}
    print("="*20)
    print(dictku)
    print("="*20)
    huruf_tertinggi = max([dictku[huruf] for huruf in word])
    return huruf_tertinggi*len(word)

    alfabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    dictku = {key: value for key, value in zip(alfabet, h)}
    print(dictku)
    huruf_tertinggi = max([dictku[huruf] for huruf in word])
    return huruf_tertinggi*len(word)

    # #solusi dengan module string
    # import string
    # dictku = {key:value for key, value in zip(string.ascii_lowercase, h)}
    # return max([dictku[huruf] for huruf in word]) * len(word)


h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5,
     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word1 = "hadi"
word2 = "gunawan"
print(
    f'huruf terbesar * len(word) dari {word1} adalah: {designerPdfViewer(h, word1)}')
print(
    f'huruf terbesar * len(word) dari {word2} adalah: {designerPdfViewer(h, word2)}')
