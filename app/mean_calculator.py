def calculatemean():
    print("Program Python Untuk Menghitung Nilai Rata-Rata")
    print("="*48)
    data = list()
    jmldata = int(input("Ada berapa data? : "))
    print("="*48)
    for i in range(jmldata):
        datainputan = float(input(f"Masukkan data ke-{i+1}: "))
        data.append(datainputan)

    print(f"List data yang anda masukkan = {data}")
    mean = sum(data)/len(data)
    print(f"Rata-rata dari keseluruhan nilai yang di input adalah : {mean}")


calculatemean()
