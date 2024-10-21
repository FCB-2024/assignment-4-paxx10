## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys
def main() :
	x = int(sys.argv[1])
	def comptadorx() :
		divisorsx = 0
		i = 1
		while i <= x :
			if x % i == 0 :
				divisorsx = divisorsx + 1
			i = i + 1
		return (comptadorx)
	r = comptadorx

	def comptadorpetits() :
		divisorspetits = 0
		i2 = 1
		while i2 < x :
				if divisorspetits % i2 == 0 :
					divisorspetits = divisorspetits + 1
				i2 = i2 + 1
		return comptadorpetits
	j = comptadorpetits
	
	if j > r :
		return ('not anti-prime')
	else :
		return("anti-prime")
	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"


## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())
