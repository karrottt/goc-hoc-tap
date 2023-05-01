def ThapHaNoi(n, from_rod, to_rod, aux_rod):
	if n == 0:
		return
	ThapHaNoi(n-1, from_rod, aux_rod, to_rod)
	print("Đĩa", n, "chuyển từ", from_rod, "sang", to_rod)
	ThapHaNoi(n-1, aux_rod, to_rod, from_rod)

n = abs(int(input("Nhập số đĩa: ")))

ThapHaNoi(n, 'A', 'C', 'B')