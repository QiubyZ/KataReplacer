#from os import system

default = {
	"a":"4",
	"i":"1",
	"t":"7",
	"g":"9",
	"e":"3"
	}
		
def main():
	kata = input("Kata:\n")
#	system("clear")
	print("Result: \n" + generator(kata, ganti_huruf=default))
	
def generator(kata:str, ganti_huruf:dict) -> str:
	for huruf in kata:
		if huruf in ganti_huruf.keys():
			kata = kata.replace(huruf, ganti_huruf.get(huruf))
	return kata + " 🥴 "
	
main()