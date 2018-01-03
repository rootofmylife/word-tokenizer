from pprint import pprint
import sys

def word_tokenize(corpus, file_dict):
	rs = ""
	sym = r"~`!@#$%^&*()_-+=[]{}|;':\"”“,./<>?–"
	corpus = [s.translate({ord(c): "" for c in sym}) for s in corpus]	
	corpus = [s.lower() for s in corpus]
	#key_search = sys.argv[1]
	file_dict.remove(file_dict[0])
	file_dict = [x.split('\t') for x in file_dict]
	vdic = []
	for i in range(len(file_dict) - 1):
		vdic.append(file_dict[i][0])
	corpus = [s.split() for s in corpus]
	corpus = corpus[0]
	temp = ""
	
	vt = -1
	for j in range(len(corpus)):
		if j <= vt:
			continue
		temp = corpus[j]
		index = j + 1
		check = 0
		while(index < j + 3):
			if index >= len(corpus) - 1:
				break
			temp2 = temp + " " + corpus[index]
			if temp2 in vdic:
				vt = index
				check = 1
				#output.write(temp2.replace(' ', '_') + " ")
				rs = rs + temp2.replace(' ', '_') + " "
				break
			index = index + 1
		if check == 0:
			rs = rs + temp + " "
			#output.write(temp + " ")	
	return rs

if __name__ == '__main__':
	with open("./VDic.txt") as f:
		file_dict = f.read().splitlines()
	with open("./corpus.txt") as fc:
		corpus = fc.read().splitlines()

	print(word_tokenize(corpus, file_dict))
	#output = open("corpus_out.txt", "w")

	#output.close()
			
