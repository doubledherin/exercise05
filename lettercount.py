from sys import argv
import string

script, filename = argv

def main():

	# Initialize a list letters in the alphabet
	letters = []
	alphabet = string.lowercase
	for letter in alphabet:
		letters.append(letter)

	# Initialize a list of 26 zeros to align with letter_list
	counts = [0] * 26

	fin = open(filename)
	content = fin.read().lower()
	for char in content:
		if char in letters:
			count = letters.index(char)
			counts[count] += 1

	for i in range(26):
		print letters[i], counts[i]




if __name__ == "__main__":
	main()

