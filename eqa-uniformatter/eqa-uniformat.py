from sys import argv
import json
from readers.mctest import mctest_format


def main():
	corpus = mctest_format(argv[1], argv[2])
	with open('out.json', 'w') as outfile:
		json.dump(corpus, outfile, indent=2)


if __name__ == "__main__": main()