arr = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
def linearsearch(arr,x):
    for l in range(len(arr)):
        if type(arr[l]) == list:
            hasil_x = linearsearch(arr[l],x)
            if hasil_x == -1:
                return -1
            else:
                print(f'{x} telah ditemukan pada indeks {l} pada kolom {hasil_x}')
                exit()
        elif arr[l] == x:
            return l
    return -1
print(arr)

x = input('Masukan nama yang ingin dicari : ')
hasil_y = linearsearch(arr,x)
if hasil_y == -1:
    print(f'{x} telah ditemukan pada indeks {hasil_y}')
else:
    print(f'{x} telah ditemukan pada indeks {hasil_y}')