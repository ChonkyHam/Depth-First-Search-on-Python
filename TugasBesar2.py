monas = {
    "Universitas Mercu Buana": {"Jln. H. Kasam": 3, "Halte Universitas Mercubuana": 2},
    "Jln. H. Kasam": {"Universitas Mercu Buana": 3, "Apartemen Kedoya Elok 2": 35, "Term. Grogol": 68},
    "Apartemen Kedoya Elok 2": {"Jln. H. Kasam": 35, "Tol Kb. Jeruk 2": 5},
    "Tol Kb. Jeruk 2": {"Apartemen Kedoya Elok 2": 5, "Juanda": 37},
    "Juanda": {"Tol Kb. Jeruk 2": 37, "Kedoya Green Garden": 48, "Monas": 14},
    "Monas": {"Juanda": 14, "Taman Kota": 40},
    "Taman Kota": {"Monas": 40, "Komplek Green Garden": 12},
    "Komplek Green Garden": {"Taman Kota": 12, "Halte Universitas Mercubuana": 40},
    "Halte Universitas Mercubuana": {"Komplek Green Garden": 40, "Kedoya Green Garden 1": 35, "Universitas Mercu Buana": 2},
    "Kedoya Green Garden 1": {"Halte Universitas Mercubuana": 35, "Kedoya Green Garden": 1},
    "Kedoya Green Garden": {"Kedoya Green Garden 1": 1, "Juanda": 48},
    "Term. Grogol": {"Jln. H. Kasam": 68, "Grogol 1": 2},
    "Grogol 1": {"Term. Grogol": 2, "Gambir 2": 34},
    "Gambir 2": {"Grogol 1": 34, "Monas": 12}
}
array = ["Universitas Mercu Buana", "Jln. H. Kasam", "Apartemen Kedoya Elok 2", "Tol Kb. Jeruk 2", "Juanda", "Monas", "Taman Kota", "Komplek Green Garden", "Halte Universitas Mercubuana", "Kedoya Green Garden 1", "Kedoya Green Garden", "Term. Grogol", "Grogol 1", "Gambir 2"]

def cari_jarak_terpendek(graph, start, end, path=[], bobot=0):
    path = path + [start]
    if start == end:
        return path, bobot
    if start not in graph:
        return None
    pendek = None
    bobot_pendek = None
    for node, bobot_node in graph[start].items():
        if node not in path:
            j_baru,b_baru = cari_jarak_terpendek(graph, node, end, path, bobot + bobot_node)
            if j_baru:
                if not pendek or len(j_baru) < len(pendek):
                    pendek = j_baru
                    bobot_pendek = b_baru
    return pendek, bobot_pendek

print("\t\tKelompok 7")
print("===========================================")
graph = monas
print("Rute Yang Tersedia :")
print(array)
dari = input("Masukan Lokasi Anda Sekarang : ")
ke = input("Masukan Tujuan Anda : ")
path, bobot = cari_jarak_terpendek(graph, dari, ke)
print(f"Jarak Terpendek Yang Memungkinkan dari {dari} ke {ke} Adalah :")
print(path)
print(f"Total Bobot Dari Semua Yang Dilalui Adalah : {bobot}")