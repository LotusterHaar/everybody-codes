# Import the library
import argparse
import csv


#method that uses Euclidian Algorithm to return the greatest common denominator of two integers int1 and int2
def gcd(a, b):
    while b: 
        a, b = b, a % b
        return abs(a)


# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--name', type=str, required=True)

# Parse the argument
args = parser.parse_args()

#with open(args.inputfile) as f:

#Open the CSV file with locations of the camera, andd find location on name
with open('cameras-defb.csv') as f:
	reader = csv.DictReader(f, delimiter=";")
	for cols in reader:
		if cols.get('Camera'):
			if 'Neude' in cols['Camera']:
				print(cols['Camera'])

print(gcd(55, 5))
print('hoi')





		


