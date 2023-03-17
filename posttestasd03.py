class Motor:

    def __init__(self, nama, jenis, tahun):
        self.nama = nama
        self.jenis = jenis
        self.tahun = tahun
        self.next_motor = None

class LinkedMotor:
    def __init__(self):
        self.head = None

    # fungsi untuk menambahkan motor ke linked list
    def tambah_motor(self, nama, jenis, tahun):
        motor_baru = Motor(nama, jenis, tahun)
        if self.head is None:
            self.head = motor_baru
        else:
            current_motor = self.head
            while current_motor.next_motor is not None:
                current_motor = current_motor.next_motor
            current_motor.next_motor = motor_baru

    # fungsi untuk menampilkan semua motor pada linked list
    def tampilkan_motor(self):
        current_motor = self.head
        while current_motor is not None:
            print("Nama Motor:", current_motor.nama)
            print("Jenis Motor:", current_motor.jenis)
            print("Tahun Pembuatan:", current_motor.tahun)
            current_motor = current_motor.next_motor

    # fungsi untuk menghapus motor dari linked list
    def hapus_motor(self, nama):
        current_motor = self.head
        prev_motor = None
        while current_motor is not None:
            if current_motor.nama == nama:
                if prev_motor is None:
                    self.head = current_motor.next_motor
                else:
                    prev_motor.next_motor = current_motor.next_motor
                return
            prev_motor = current_motor
            current_motor = current_motor.next_motor

    # fungsi untuk mengubah informasi motor pada linked list
    def ubah_motor(self, nama, jenis, tahun):
        current_motor = self.head
        while current_motor is not None:
            if current_motor.nama == nama:
                current_motor.jenis = jenis
                current_motor.tahun = tahun
                return
            current_motor = current_motor.next_motor

# contoh penggunaan linked list untuk pencucian motor
linked_motor = LinkedMotor()

# tambahkan motor ke linked list
linked_motor.tambah_motor("Vario", "Matic", "2015")
linked_motor.tambah_motor("Ninja", "Sport", "2021")
linked_motor.tambah_motor("PCX", "Matic", "2019")

# tampilkan semua motor pada linked list
linked_motor.tampilkan_motor()

# hapus motor dari linked list
linked_motor.hapus_motor("Ninja")

# tampilkan semua motor pada linked list setelah dihapus
linked_motor.tampilkan_motor()

# ubah informasi motor pada linked list
linked_motor.ubah_motor("Vario", "Automatic", "2015")

# tampilkan semua motor pada linked list setelah diubah
linked_motor.tampilkan_motor()