
	T = float(input("Input T: "))
	V = float(input("Input V: "))

	powV = V**0.16
	print("Ts = {0}".format(round(13.12 + 0.6215*T - 11.37*(powV) + 0.3965*T*powV, 2)))