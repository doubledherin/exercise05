from sys import argv
import string

script, filename = argv

def main():
	fin = open(filename)
	content = fin.read().lower()

	letter_list = []
	alphabet = string.lowercase
	for letter in alphabet:
		letter_list.append((letter, 0))
	print letter_list

if __name__ == "__main__":
	main()

