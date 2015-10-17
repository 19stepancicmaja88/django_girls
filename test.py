
imena = [("maja", "z"), ("zan", "m"), ("ana", "z")]

skupina = {"ime_skupine": "profici", "mentor": "zan", "ucenki": ["maja", "ana"]}



for sklop in imena:
	if sklop[1] == "m":
		pozdrav = "pozdravljen "
	else:
		pozdrav = "pozdravljena "

	print(pozdrav+sklop[0])

print("udelezenki " + str(skupina ["ucenki"]) + "sta del skupine " + skupina ["ime_skupine"])


def kvadriraj(x):
	return x**2

def pozdravi(ime, spol):
	if spol == "m":
		pozdrav = "pozdravljen"
	else:
		pozdrav = "pozdravljena"
	return pozdrav + ime 

