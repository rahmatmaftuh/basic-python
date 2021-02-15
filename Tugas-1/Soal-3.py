ujian_praktek = float(input("Masukkan nilai ujian praktek anda ="))
ujian_teori = float(input("Masukkan nilai ujian teori anda = "))

if ujian_teori>=70 and ujian_praktek>=70:
	print("Selamat, anda lulus!")
elif ujian_teori>=70 and ujian_praktek<70:
	print("Anda harus mengulang ujian praktek")
elif ujian_teori<70 and ujian_praktek>=70:
	print("Anda harus mengulang ujian teori")
else:
	print("Anda harus mengulang ujian teori dan praktek")