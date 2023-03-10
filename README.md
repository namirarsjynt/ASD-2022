# post test asd02
Cara kerja program
Program tersebut merupakan sebuah implementasi dari algoritma linear search untuk mencari suatu nilai dalam array 
pada baris pertama program tersebut , sebuah array dengan elemen yang di tentukan,kemudian sebuah fungsi "linesearch" didefinisikan dengan dua parameter,
yaitu paramater "arr" dan "x" fungsinya melakukan pencarian nilai "x" pada array "arr" dengan menggunakan algoritma Linear Search,
pada saat fungsi "linearsearch" dipanggil, maka ia akan melakukan iterasi pada setiap elemen pada array yang diberikan sebagai parameter
pada setiap iterasi,ia akan memeriksa apakah sebuah  elemen tersebut merupakan sebuah list atau bukan, jika elemen tersebut merupakan list,Maka fungsi "linearsearch"
akan terpanggil secara rekursif dengan parameter array tersebut sebagai parameter "arr",Fungsi "linearsearch" akan terus melakukan suatu pencarian hingga menemukan 
elemen yang sesuai dengan nilai "x" tersebut.
Jika elemen yang sedang diperiksa bukan sebuah list dan nilainya sama dengan "x",maka fungsi "linearsearch" akan mengembalikan indeks elemen tersebut,
jika elemen tersebut bukan elemen yang dicari,Maka fungsi akan mengembalikan nilai -1

Pada program utama,pengguna diminta untuk memasukkan nilai "x" yang ingin ia cari.Kemudian, fungsi "linearsearch" dipanggil dengan parameter array "arr" dan nilai "x"
hasil pencarian tersebut kemudian disimpan didalam variabel "hasil_y",Jika nilai "hasil_y" sama dengan -1 maka program akan mencetak bahwa nilai "x" tidak ditemukan.
jika "hasil_y" tidak sama dengan -1, maka program akan mencetak indeks dari elemen yang sesuai dengan nilai "x" tersebut.
