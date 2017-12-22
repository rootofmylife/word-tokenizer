import word_segment
from pprint import pprint

if __name__ == '__main__':
	with open("./corpus.txt") as fc:
		corpus = fc.read().splitlines()
	gazetteer = ["BCH", "BP", "BM", "CB", "GV", "NV", "CĐCS", "CMHS", "MC", "GD", "GVBM","GVCN", "HĐSP", "HĐ", "HĐQT", "HS", "HT", "KTX", "PC-ĐBCL", "TH", "THCS", "THPT", "ThS", "TS", "UBND", "VNĐ"]

	corpus = ''.join(corpus)
	final = []
	temp = ""
	for i in range(len(corpus)):
		if corpus[i] == '.' or corpus[i] == '!' or corpus[i] == '?' or corpus [i] == ':':
			final.append(temp.strip())
			temp = ""
			continue
		temp = temp + corpus[i]	

	pprint(final)
