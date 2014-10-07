from sys import argv
import string

script, filename = argv

def main():
	fin = open(filename)
	content = fin.read().lower()

	print content

if __name__ == "__main__":
	main()

