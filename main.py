from __future__ import unicode_literals

def capitalize(a) :
    return ' '.join(word.capitalize() for word in a.split())

def cekModul():
    print("Memuat program...")
    command = "python -m pip install -r requirements.txt"
    subprocess.run(command, shell=True, check=True)

class mapel :
    # edit bagian sini ajah klo mw ngubah jadwal
    isi = []
    with open("jadwal.txt", "r+") as file :
        isi += file.readlines()
        file.close()
    senin = isi[0].split(', ')
    selasa = isi[1].split(', ')
    rabu = isi[2].split(', ')
    kamis = isi[3].split(', ')
    jumat = isi[4].split(', ')
    sabtu = isi[5].split(', ')

    semua_mapel_raw =[]
    for mapels in isi :
        semua_mapel_raw += mapels.split(', ')

    i = 0
    while i < len(semua_mapel_raw) :
        try :
            semua_mapel_raw[i] = semua_mapel_raw[i].strip()
        except AttributeError :
            pass
        i += 1

    semua_mapel = []
    semua_mapel.append(semua_mapel_raw[0])
    indeks = 1
    reactor = False
    while indeks < len(semua_mapel_raw):
        for i in semua_mapel :
            if i == semua_mapel_raw[indeks] :
                reactor = True
        if reactor != True :
            semua_mapel.append(semua_mapel_raw[indeks])
        indeks += 1
        reactor = False


    #semua_mapel = ["ekonomi", "fisika", "sejarah", "bahasa inggris", "matematika", "kimia", 
    #          "bahasa indonesia", "sosiologi", "agama", "pendidikan pancasila", "knkp", 
    #          "pkwu", "seni budaya", "geografi", "biologi", "bela negara", "informatika", 
    #          "bahasa jawa", "p5"]
    #senin = ["ekonomi", "fisika", "sejarah", "bahasa inggris", "matematika"]
    #selasa = ["kimia", "bahasa indonesia", "sosiologi", "agama", "pendidikan pancasila", "knkp"]
    #rabu = ["pkwu", "seni budaya", "ekonomi", "geografi", "bahasa inggris", "biologi", "bela negara"]
    #kamis = ["kimia", "informatika", "geografi", "knkp"]
    #jumat = ["bahasa indonesia", "bahasa jawa", "matematika"]
    #sabtu = ["sejarah", "biologi", "penjas", "fisika", "sosiologi"]

def fisrtLogin() :
    # grand master kita dek 🗣️🔥
    with open("mapel_pilihan.txt", "r+") as file :
        mbaca = file.read()
        temp = mapel()
        temp = temp.senin + temp.selasa + temp.rabu + temp.kamis + temp.jumat + temp.sabtu
        if mbaca == "":
            print("Masukkan mapel apa saja yang ingin dijadikan sebagai mapel tambahan:")
            print("1. Ekonomi\n2. Fisika\n3. Sejarah\n4. Bahasa Inggris\n5. Matematika\n6. Kimia\n" +
              "7. Bahasa Indonesia\n8. Sosiologi\n9. Agama\n10. Pendidikan Pancasila\n11. KNKP\n" +
              "12. PKWU\n13. Seni Budaya\n14. Geografi\n15. Biologi\n16. Bela Negara\n17. Informatika\n" +
              "18. Bahasa Jawa\n")
            listUK = []
            while True:
                milih = input("(tidak menggunakan indeks) > ")
                milih = milih.lower()
                if milih in temp:
                    trigger = False
                    for w in listUK :
                        if w == milih :
                            trigger = True
                            break
                    if trigger == False :
                        file.write(milih + "\n")
                        print(f"oke {capitalize(milih)}, ada lagi? (engga/udahan):")
                        listUK.append(milih)
                    else :
                        print(f"Udah kepilih atuh bang, apusi")
                elif milih == "engga" or milih == "udahan" or milih == "bang udah bang":
                    file.seek(0)
                    if file.read() == "" :
                        print("kok gitu bang, belum ada isinya lho bang. coba pilih dlu")
                        file.seek(0, 2)
                    else:
                        os.system('cls')
                        print("oke lanjut yak.")
                        file.close()
                        time.sleep(2)
                        os.system('cls')
                        break
                else:
                    print(f"mang eak milih {capitalize(milih)}? coba deh milih lagi : ")
    os.system('cls')
    with open(os.getcwd() + "\\mapel\\mingguIni.txt", "r") as file :
        getPS = file.readline()
        file.close()
    if getPS != "" :
        pass
    else :
        while True :
            print("Btw minggu ini pkwu apa senbud ?")
            senOrPk = input("> ")
            senOrPk = senOrPk.lower()
            if senOrPk == "senbud" or "pkwu" :
                with open(os.getcwd() + "\\mapel\\mingguIni.txt", "w") as file :
                    file.write(senOrPk)
                    file.close()
                break
            else :
                print("Yang benerlah bang")
    os.system('cls')
    print("oke done maszeh, lanjut aplikasi.")
    time.sleep(2)
    os.system('cls')

def keluar() :
    os.system('cls')
    print("Program dihentikan.")
    input()
    sys.exit()

def muzekBackground(menuIsCall = False, mode = "", pesan="") :
    if menuIsCall == False :
        if mode in "vol" :
            mode = mode.split()
            pygame.mixer.music.set_volume(mode[1])
            return
        pygame.mixer.init()
        with open(os.getcwd() + "\\bgmusic\\config\\usedBgMusic.txt", "r") as file :
            musikDigunakan = file.readline()
            file.close()
        musikDigunakan = musikDigunakan.replace(' ', '_')
        dirMusikBg = os.getcwd() + "\\bgmusic\\" + musikDigunakan +".wav"
        pygame.mixer.music.load(dirMusikBg)
        mode = mode.split()
        if mode[0] == "on" :
            pygame.mixer.music.play(loops=-1)
            doc = open(os.getcwd() + "\\bgmusic\\config\\toggle.txt", "w")
            doc.write("on")
            doc.close()
        elif mode[0] == "off" :
            pygame.mixer.music.stop()
            doc = open(os.getcwd() + "\\bgmusic\\config\\toggle.txt", "w")
            doc.write("off")
            doc.close()
    elif menuIsCall == True :
        os.system("cls")
        direktori = os.getcwd() + "\\bgmusic"
        files = os.listdir(direktori)
        print("Menu musik :")
        listMusik = []
        def revExt(a) :
            return os.path.splitext(a)[0]
        indeks = 1
        for file in files :
            if os.path.isfile(os.path.join(direktori, file)) :
                listMusik.append(revExt(file.replace('_', ' ')))
                print(f"{indeks}. " + capitalize(revExt(file.replace('_', ' '))))
                indeks += 1
        indeksList = len(listMusik)
        if pesan == "" :
            print("\nDownload musik dari yt menggunakan command \"add\"")
        else :
            print("\n" + pesan)
        # print(listMusik)
        pilihan = input(">")
        pilihan = pilihan.split()
        pilihan[0] = pilihan[0].lower()
        if pilihan[0] == "back" or pilihan[0] == "kembali" :
            menu("")
        elif pilihan[0] == "add" :
            if "https" in pilihan[1] :
                batas = len(pilihan)
                nama = ""
                iter = 2
                while iter < batas :
                    if iter == batas -1 :
                        nama += pilihan[iter]
                    else :
                        nama += pilihan[iter] + " "
                    iter += 1
                url = pilihan[1]
                AUDIO_NAME = nama.replace(' ', '_')
                loc = os.getcwd() + "\\bgmusic\\"
                ydl_opts = {
                    'format': 'bestaudio/best',
                    #    'outtmpl': 'output.%(ext)s',
                    'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                }],
                "outtmpl": f'{loc}{AUDIO_NAME}',  # this is where you can edit how you'd like the filenames to be formatted

                }
                def download_from_url(url):
                    ydl.download([url])
                    #stream = ffmpeg.input('output.m4a')
                    #stream = ffmpeg.output(stream, 'output.wav')

                try :
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        download_from_url(url)
                except yt_dlp.utils.DownloadError as e :
                    muzekBackground(True, pesan=f"Terjadi kesalahan saat mengunduh lagu {capitalize(nama)}.\n{e}")
                else :
                    muzekBackground(True, "", f"Berhasil mengunduh lagu {capitalize(nama)}")
            else :
                loc = os.getcwd() + "\\bgmusic\\"
                iter = -1
                while True :
                    if ".mp3" in pilihan[iter] :
                        break
                    iter -= 1
                lokasiRaw = pilihan[1:iter + 1] 
                #iterRaw = len(lokasiRaw)
                lokasi = ""
                for i in lokasiRaw :
                    if ".mp3" in i :
                        lokasi += i
                    else :
                        lokasi += i + ' '
                if "\"" in lokasi :
                    lokasi = lokasi.strip('\"')
                tkp = lokasi.split('\\')
                namFile = tkp[-1]
                keTkp = os.path.join(*tkp[:-1])
                print("Mengecek direktori...")
                if not os.path.isdir(keTkp) :
                    muzekBackground(True, pesan=f"{keTkp} bukanlah direktori yang benar.")
                else :
                    print("Direktori tersedia!")
                    print("Mencari file")
                    items = os.listdir(keTkp)
                    namFile = namFile.split()
                    tesCocok = {}
                    for i in items :
                        value = 0
                        for j in namFile :
                            if j in i :
                                value += 1
                            else :
                                value -= 1
                        tesCocok.update({i:value})
                    max_key = max(tesCocok, key=tesCocok.get)
                    jalur = os.path.join(keTkp, max_key)
                    sound = convert.from_mp3(jalur)
                    print("File ditemukan!")
                    namaLagu = ""
                    iter += 1
                    konst = -1
                    while True :
                        if iter == konst :
                            namaLagu += pilihan[iter]
                            break
                        else :
                            namaLagu += pilihan[iter] + ' '
                        iter += 1
                    print("Mengimpor lagu...")
                    sound.export(loc + f"{namaLagu.replace(' ', '_')}.wav", format="wav")
                    muzekBackground(True, pesan=f"Berhasil mengimpor lagu {capitalize(namaLagu)}")
        elif pilihan[0] == "change" :
            loc = os.getcwd() + "\\bgmusic\\config\\usedBgMusic.txt"
            try :
                pilihan[1] = int(pilihan[1])
                isi = listMusik[pilihan[1] - 1]
            except :
                isi = ""
                iter = 1
                batas = len(pilihan)
                while iter < batas :
                    if iter == batas -1 :
                        isi += pilihan[iter]
                    else :
                        isi += pilihan[iter] + " "
                    iter += 1
                isi = isi.lower()
            for i in listMusik :
                if i == isi :
                    with open(loc, "w+") as file :
                        file.write(isi)
                    file.close()
                    muzekBackground(True, "", f"Berhasil mengubah lagu ke {capitalize(isi)}.")
                else :
                    pass
            muzekBackground(True, pesan = f"Lagu {isi} tidak tersedia.")
        elif pilihan[0] == "on" :
            muzekBackground(False, pilihan[0])
            muzekBackground(True)
        elif pilihan[0] == "off" :
            muzekBackground(False, pilihan[0])
            muzekBackground(True)   
        elif pilihan[0] == "vol" :
            volume = ""
            volume = pilihan[0] + pilihan[1]
            muzekBackground(False, mode=volume)
            muzekBackground(True)
        elif pilihan[0] in ["del", "delete", "hapus"] :
            try :
                try :
                    dariList = int(pilihan[1])
                    dariList = listMusik[dariList - 1]
                    namFile = dariList.replace(' ', '_')
                except ValueError:
                    iter = 1
                    batas = len(pilihan)
                    namFile = ""
                    while iter < batas :
                        if iter == batas -1 :
                            namFile += pilihan[iter]
                        else :
                            namFile += pilihan[iter] + "_"
                        iter += 1
                    namFile = namFile.lower() 
                dis = capitalize(namFile.replace("_", " "))
                namFile = namFile + ".wav"
                loc = os.getcwd() + "\\bgmusic\\"
                target = loc + namFile
                if os.path.isfile(target) :
                    os.remove(target)
                    muzekBackground(True, pesan = f"Berhasil menghapus musik: {dis}")
                else :
                    muzekBackground(True, pesan = f"{dis} bukanlah lagu yang tersedia.")
            except PermissionError:
                muzekBackground(True, pesan=f"Lagu {dis} sedang digunakan, alihkan ke lagu yang lain untuk menghapus.")
        elif pilihan[0] in ["ekspor", "export"] :
            try :
                pilihan[1] = int(pilihan[1])
                try :
                    sound = convert.from_wav(direktori + f"\\{listMusik[pilihan[1] - 1].replace(' ', '_')}.wav")
                    sound.export(direktori + f"\\exported\\{listMusik[pilihan[1] - 1]}.mp3", format="mp3")
                    muzekBackground(True, pesan="Berhasil mengekspor lagu.")
                except IndexError :
                    muzekBackground(True, pesan=f"Lagu pada indeks ke-{pilihan[1]}.")
            except ValueError :
                iter = 1
                nama = ' '.join(pilihan[1:])
                if os.path.isfile(direktori + f"\\{nama}.wav") :
                    print(f"Mengonversi lagu {capitalize(nama)}...")
                    sound = convert.from_wav(direktori + f"\\{nama.replace(' ', '_')}.wav")
                    sound.export(direktori + f"\\exported\\{nama}.mp3", format='mp3')
                    muzekBackground(True, f"Berhasil mengeksport lagu {capitalize(nama)}.")
                else :
                    muzekBackground(True, pesan=f"{capitalize(nama)} bukanlah lagu yang ada dalam daftar.")
        else:
            muzekBackground(True, pesan="Perintah tidak valid.")

def nugas(loc, err="") :
    os.system('cls')
    judulTugas = os.path.splitext(loc)[0]
    judulTugas = judulTugas.split("\\")[-1]
    with open(loc, "r+") as tugasnya :
        isiTugas = tugasnya.read()
        tugasnya.close()
    print(capitalize(judulTugas) + "\n\n" + isiTugas)
    if err != "" :
        print(err)
    else :
        pass
    masukan = input("> ")
    if masukan in ["selesai", "delete"] :
        os.system('cls')
        truKah = input(f"Benarkah ingin menghapus tugas {judulTugas} ? >")
        truKah = truKah.lower()
        if truKah in ["y", "iya", "yes"] :
            os.remove(loc)
            os.system('cls')
            print(f"Berhasil menghapus tugas {judulTugas}")
            time.sleep(2)
            return
        else :
            nugas(loc)
    elif masukan in ["back",] :
        return
    elif masukan in ["menu", "home"] :
        menu()
    else :
        nugas(loc, f"Perintah {masukan} tidak valid.")

def display(pilMapel="", err="") :
    def belajar(loc, namMapel, pesan="") :
        os.system('cls')
        with open(loc, "r") as file :
            counter = int(file.readline())
            file.close()
        bar = counter % 10
        blank = 10 - counter % 10 - 1
        print(f"Belajar {capitalize(namMapel)} :")
        print("[" + "=" * bar + " " * blank + "]" + f" x {counter}")
        print(f"Telah dipelajari sebanyak {counter} kali.")
        if pesan != "" :
            print(pesan)
        start = input("\n> ")
        if start == "mulai" :
            os.system('cls')
            print(f"Belajar {capitalize(namMapel)} :")
            print("[" + "=" * bar + " " * blank + "]" + f" x {counter}")
            print(f"Telah dipelajari sebanyak {counter} kali.")
            startTime = time.time()
            input("\nProses belajar sedang berlangsung...")
            endTime = time.time()
            diffTime = endTime - startTime
            counter += 1
            with open(loc, "w") as file :
                file.write(str(counter))
                file.close()
            belajar(loc, namMapel, f"Proses belajar telah selesai, memakan waktu {diffTime:.2f} detik")
    os.system('cls')
    # here we goh bebeh
    bridge = os.getcwd() + f"\\mapel\\{pilMapel.strip()}"
    if not os.path.isdir(bridge) :
        os.mkdir(bridge)
        with open(bridge + "\\counter.txt", "w") as counter :
            counter.write("0")
            counter.close()
    print(f"Mapel {capitalize(pilMapel)}")
    counter = open(bridge + "\\counter.txt")
    count = int(counter.readline())
    counter.close()
    print(f"telah dipelajari sebanyak {count} kali.")
    bar = count % 10
    blank = 10 - count % 10 - 1
    print("[" + "=" * bar + " " * blank + "]" + f" x {count}")
    print("\nDaftar tugas:")
    daftarIsi = os.listdir(bridge)
    tugas = [os.path.splitext(i)[0] for i in daftarIsi]
    panjang = len(tugas)
    if panjang == 1 :
        print("Tidak ada tugas untuk mapel ini")
    else :
        del tugas[0]
        indeks = 1
        for i in tugas :
            with open(bridge + f"\\{i}.txt") as file :
                judul = file.readline()
                file.close()
            print(f"{indeks}. {capitalize(i)} - {judul.strip()}...")
            indeks += 1
    if err != "" :
        print("\n" + err)
        pilihan = input("> ")
    else :
        pilihan = input("\n> ")
    try :
        pilihan = int(pilihan)
        panjang = len(tugas)
        if pilihan <= 0 or pilihan > panjang:
            display(pilMapel, "Indeks tugas tidak tersedia")
        else :
            nugas(bridge + f"\\{tugas[pilihan - 1]}.txt")
            display(pilMapel)
    except ValueError :
        if pilihan == "belajar" :
            belajar(bridge + "\\counter.txt", pilMapel)
        elif pilihan in ["menu", "home", "back"] :
            menu()
        elif pilihan in ["add", "tambah", "+"] :
            os.system('cls')
            judul = input("Masukkan judul: ")
            print("")
            isi = ""
            baris = 1
            while True :
                temp = input(f"Masukkan isi baris ke-{baris}: ")
                if temp in ["udah", "udahan", "selesai", "done"] :
                    with open(bridge + f"\\{judul}.txt", "x") as penugasan :
                        penugasan.write(isi)
                        penugasan.close()
                    display(pilMapel, f"Berhasil menambahkan tugas {judul}")
                else :
                    isi += temp + "\n"
                    baris += 1
        else :
            display(pilMapel, "Kesalahan input.")

def menu(err = "") :
    # intinya gitu sih, tapi ini ui nya wkokwoak
    os.system('cls')
    print("=====Aplikasi Ngatur Tugas ama Belajar=====")
    sekarang = datetime.datetime.now()
    indeksHari = sekarang.weekday()
    namaNamaHari = ["Senin", "Selasa", "Rabu", "Kamis", "Jum\'at", "Sabtu", "Minggu"]
    try :
        besokHari = namaNamaHari[indeksHari + 1]
        #besokHari = namaNamaHari[6]
    except IndexError :
        besokHari = namaNamaHari[0]
    hariIni = namaNamaHari[indeksHari]
    
    print(f"Sekarang hari {namaNamaHari[indeksHari]}, Besok hari {besokHari} :")
    isiMapel = mapel()
    daftarPilihan = isiMapel.semua_mapel
    sudah_ada_dipilihan = []
    mapelHari = []
    if hariIni == "Minggu" :
        print("Hari ini hari Minggu")
    else:
        print("Jadwal Hari ini:")
        if hariIni == "Senin" :
            mapelHari = isiMapel.senin
        elif hariIni == "Selasa" :
            mapelHari = isiMapel.selasa
        elif hariIni == "Rabu" :
            mapelHari = isiMapel.rabu
        elif hariIni == "Kamis" :
            mapelHari = isiMapel.kamis
        elif hariIni == "Jum\'at" :
            mapelHari = isiMapel.jumat
        elif hariIni == "Sabtu" :
            mapelHari = isiMapel.sabtu
        indeks = 1
        for i in mapelHari :
            print(f"{str(indeks)}. {capitalize(i)}")
            indeks += 1
            sudah_ada_dipilihan.append(i)
    print("\nMata Pelajaran Besok :")
    mapelBesok = []
    if besokHari == "Minggu" :
        print("Besok minggu sih")
    else :
    #    print("\nJadwal besok belajar : ")
    #with open("mapel_pilihan.txt", "r+") as file :
    #    mappil = file.read()
    #    file.close()
        if besokHari == "Senin" :
            mapelBesok = isiMapel.senin
        elif besokHari == "Selasa" :
            mapelBesok = isiMapel.selasa
        elif besokHari == "Rabu" :
            mapelBesok = isiMapel.rabu
        elif besokHari == "Kamis" :
            mapelBesok = isiMapel.kamis
        elif besokHari == "Jum\'at" :
            mapelBesok = isiMapel.jumat
        elif besokHari == "Sabtu" :
            mapelBesok = isiMapel.sabtu
    indeks = 1
    with open("mapel_pilihan.txt", "r") as file :
        mapil = file.read()
    tambahan = mapil.split("\n")

    for i in mapelBesok:
        print(str(indeks) + ". " + capitalize(i))
        indeks += 1
        sudah_ada_dipilihan.append(i)
    #print("\nTambahan Mapel Lain :")
    mapelPilihan = tambahan
    indeks = 1
    indeksI = 0
    del mapelPilihan[-1]
    for i in mapelPilihan :
        for j in sudah_ada_dipilihan :
            if i == j :
                del mapelPilihan[indeksI]
        indeksI += 1
    #for i in mapelPilihan :
    #    for j in mapelHari :
    #        if i == j :
    #            del mapelPilihan[indeksI]
    #    indeksI += 1
    if mapelPilihan != [] :
        print("\nTambahan Mapel Lain :")
        for i in mapelPilihan :
            print(str(indeks) + ". " + capitalize(i))
            indeks += 1
            #daftarPilihan.append(i)
    #===Display tugas tugas
    print('\nTugas-tugas:')
    lokasi_tugas = os.getcwd() + "\\mapel"
    mapel_mapel = os.listdir(lokasi_tugas)
    tugas_tugas =  {}
    indeks = 1
    for i in mapel_mapel :
        try:
            open_dir = lokasi_tugas + f"\\{i}"
            banyak_tugas = os.listdir(open_dir)
            iter = 0
            for count in banyak_tugas :
                if count == 'counter.txt' :
                    iter += 1
                    continue
                nama_tugas = os.path.basename(count)
                print(f"{indeks}. {capitalize(i)} - {nama_tugas}")
                tugas_tugas.update({i:nama_tugas})
                iter += 1
                indeks += 1
        except NotADirectoryError :
            pass


    if err == "" :
        print("\nKetik \"help\" atau \"?\" untuk bantuan")
    else :
        print("\n" + err)
    #print(daftarPilihan)
    print(tugas_tugas)
    pilihan = input(">")
    pilihan = pilihan.split()
    if pilihan[0] == "help" or pilihan[0] == "?" :
        os.system('cls')
        print("help/? : Membuka berbagai macam perintah yang dapat digunakan")
        print("info : Menampilkan informasi dari pembuat dan versi yang digunakan")
        print("bgmusik : Membuka halaman daftar musik dan musik yang sedang diputar")
        print("Ketik nama dari mapel yang ingin dipelajari untuk membuka halaman tersebut")
        print("exit/keluar/cabut : Keluar dari program")
        print("\nKlik enter untuk melanjutkan...")
        input()
        menu()
    elif pilihan[0] == "bgmusik" :
        try :
            if pilihan[1] == "on" :
                muzekBackground(False, "on")
                menu()
            elif pilihan[1] == "off" :
                muzekBackground(False, "off")
                menu()
            elif pilihan[1] == "menu" :
                muzekBackground(True)
            else :
                menu('BGMusik error: Perintah tidak valid.')
        except IndexError :
            menu('BGMusik error: Argumen ke-2 kosong.')
    elif pilihan[0] in ["exit", "keluar", "cabut"] :
        keluar()
    elif pilihan[0] in ["nugas", "tugas"] :
        pass
        #menu(tugas_tugas[pilihan[1]])
    else :
        try :
            pilihan[0] = int(pilihan[0])
            try :
                if pilihan[1] in ["wajib", "besok"] :
                    try :
                        display(mapelBesok[pilihan[0] - 1])
                    except IndexError :
                        menu(f"Tidak tersedia mapel ke {pilihan[0]} pada mapel besok")
                elif pilihan[1] in ["tambahan", "pilihan"] :
                    try :
                        display(mapelPilihan[pilihan[0] - 1])
                    except IndexError :
                        menu(f"Tidak tersedia mapel ke {pilihan[0]} pada mapel tambahan")
                elif pilihan[1] in ["hari", "sekarang", "now"] :
                    try :
                        display(mapelHari[pilihan[0] - 1])
                    except IndexError :
                        menu(f"Tidak tersedia mapel ke {pilihan[0]} pada mapel hari ini.")
                else : 
                    menu("Perintah invalid.")
            except IndexError :
                menu("Silahkan pilih mapel besok atau tambahan.")
        except ValueError :
            if len(pilihan) == 1 :
                mapDipilih = pilihan[0]
            else :
                #indeks = 0
                #batas = len(pilihan)
                #namMap = ""
                #for i in pilihan :
                #    if indeks == batas - 1 :
                #        namMap += i
                #    else :
                #        namMap += i + ' '
                #mapDipilih = namMap
                mapDipilih = pilihan[0] + " " + pilihan[1]
            for i in daftarPilihan :
                if mapDipilih == i :
                    display(mapDipilih)
            menu(f"Perintah tidak tersedia")


# as alweys, djawa adalah koentji
import sys
import subprocess
cekModul()
import pygame
import datetime, yt_dlp
import time
import os, shutil
# import ffmpeg
from pydub import AudioSegment as convert
#ffmpeg = os.getcwd() + "\\lib\\ffmpeg-6.1.1"
#sys.path.append(ffmpeg)

os.system('cls')
fisrtLogin()
doc = open(os.getcwd() + "\\bgmusic\\config\\toggle.txt", "r")
muzekBackground(False, doc.read())
menu()