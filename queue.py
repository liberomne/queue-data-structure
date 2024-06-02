from datetime import timedelta, datetime
from time import sleep

class queue:
    # Inisialisasi head
    def __init__(self, max_size = 5):
        self.size = max_size
        self.current_size = 0
        self.data = []

    # Mendefinisikan sebuah fungsi untuk memeriksa apakah antrian penuh
    def isFull(self):
        if self.current_size == self.size:
            return True
        else:
            return False

    # Mendefinisikan sebuah fungsi untuk memeriksa apakah antrian kosong       
    def isEmpty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    # Mendefinisikan sebuah fungsi untuk menambahkan nilai pada antrian
    def enqueue(self,newdata):
        if self.isFull():
            print("\n")
            print("Mohon maaf antrian sudah penuh")
        else:
            self.data.append(newdata)
            self.current_size = len(self.data)
            print("\n==================================================================================================")
            print("\tAntrian tiket ",newdata,"telah berhasil ditambahkan")
            print("==================================================================================================")
        print("Tekan [enter] untuk melanjutkan")
        input()
        self.menu()

    # Mendefinisikan sebuah fungsi untuk menghapus nilai pada antrian yang terdepan
    def dequeue(self):
        if self.isEmpty():
            print("\n")
            print("Maaf antrian tiket kosong")
            print("Tekan [enter] untuk melanjutkan")
            input()
            self.menu()
        else:
            datakeluar = self.data.pop(0)
            self.current_size = len(self.data)
            waktu=datetime.now()
            endtime = waktu + timedelta(seconds=10)
            print("\n=============================================================================")
            print(datakeluar,"akan dilayani pada : " ,waktu)
            print("Mohon untuk memasuki ruangan")
            print("=============================================================================")
            print(datakeluar ,"sedang memasuki ruangan")
            if not self.isEmpty():
                sleep(3)
                print("-----------------------------------------------------------------------------")
                print(self.data[0], "akan memasuki ruangan pada " ,endtime)
            else:
                print("Antrian kosong")
        print("Tekan [enter] untuk melanjutkan")
        input()
        self.menu()

    # Mendefinisikan sebuah fungsi untuk menampilkan data antrian
    def list(self):
        if self.isEmpty():
            print("\n")
            print("Maaf antrian kosong, silahkan tambah data")
        else:
            print("\n")
            print("==========================================")
            print("|           LIST DATA ANTRIAN            |")
            print("==========================================")
            print("Data antrian: ")
            x=1
            for i in self.data:
                print(" " +str(x)+ ". ", i)
                x += 1
        print("Tekan [enter] untuk melanjutkan")
        input()
        self.menu()

    # Mendefinisikan sebuah fungsi untuk melihat informasi data antrian
    def view(self):
        print("\n================ INFORMASI ANTRIAN TIKET ================")
        print("\tKapasitas antrian: ",self.size)
        print("\tBanyak isi antrian saat ini: ",self.current_size)
        print("=========================================================")
        if self.isEmpty():
            print("\n")
            print("Mohon maaf antrian tiket kosong")
        else:
            print("Data antrian pertama: ",self.data[0])
            print("Data antrian terakhir: ",self.data[self.current_size-1])
            print("Total antrian : " ,len(self.data))
            print("=========================================================")
        print("Tekan [enter] untuk melanjutkan")
        input()
        self.menu()

    # Mendefinisikan fungsi exit
    def exit():
        import sys
        sys.exit()

    # Mendefinisikan tampilan menu dari program antrian
    def menu(self):
        import os
        os.system("CLS")
        print("====================================================")
        print("PROGRAM ANTRIAN TIKET BIOSKOP".center(50))
        print("----------------------------------------------------")
        print("Daftar Program yang Tersedia" .center(50))
        print("====================================================")
        print("[1] Tambahkan data antrian")
        print("[2] Panggil data antrian terdahulu")
        print("[3] Cek list data antrian")
        print("[4] Lihat data antrian tersisa")
        print("[5] Keluar dari program antrian")

        pilihan = input("Masukkan no menu yang ingin dipilih [1/2/3/4/5] : ")

        if pilihan == "1":
            print("\n==========================================")
            print("|           Film yang tersedia           |")
            print("------------------------------------------")
            print("| 1. Mencuri Raden Saleh                 |")
            print("| 2. Mariposa                            |")
            print("| 3. Interstellar                        |")
            print("| 4. Inception                           |")
            print("| 5. Hunger Games                        |")
            print("==========================================")
            print("\n----------------------------------------------------------------------------")
            print("Format Input : Nama - Film".center(60))
            newdata = input("Masukkan daftar nama antrian : ")
            print("----------------------------------------------------------------------------")
            self.enqueue(newdata)
        elif pilihan == "2":
            self.dequeue()
        elif pilihan == "3":
            self.list()
        elif pilihan == "4":
            self.view()
        elif pilihan == "5":
            print("\n")
            print("================================================")
            print("| ANDA TELAH KELUAR DARI PROGRAM, TERIMA KASIH |")
            print("================================================")
            exit
        else:
            print("\n")
            print("===============================================")
            print("| MAAF LAYANAN YANG ANDA PILIH TIDAK TERSEDIA |")
            print("===============================================")
            print("Tekan [enter] untuk kembali ke menu")
            input()
            self.menu()

q = queue()
q.menu()
