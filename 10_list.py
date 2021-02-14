daftar_belanja = ["Sabun", "gayung", "sikat", "lipstick"]
print(daftar_belanja)
print(daftar_belanja[0:2])
print(daftar_belanja[0][3])
daftar_belanja.append("Deterjen")
daftar_belanja.append("Shampoo")
print(daftar_belanja)
daftar_belanja[0],daftar_belanja[1] = daftar_belanja[1], daftar_belanja
print(daftar_belanja)