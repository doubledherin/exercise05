from sys import argv
import string

script, filename = argv

def main():

	# Initialize a list letters in the alphabet
	letters = []
	alphabet = string.lowercase
	for letter in alphabet:
		letters.append(letter)
	print letters

	# Initialize a list of 26 zeros to align with letter_list
	counts = [0] * 26
	print counts


	fin = open(filename)
	content = fin.read().lower()
	for char in content:
		pass



if __name__ == "__main__":
	main()

