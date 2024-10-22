## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys
def main() :
	x = int(sys.argv[1])
	def comptador(x):
		divisorsx = 0
		i = 1
		while i <= x:
			if x % i == 0:
				divisorsx = divisorsx + 1
			i = i + 1
		return divisorsx
	r = comptador(x)

	for i in range (1,x):
		if comptador(i) >= r:
			return ("not anti-prime")
			
	return("anti-prime")



## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())
