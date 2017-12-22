import word_segment
from pprint import pprint

if __name__ == '__main__':
	with open("./corpus.txt") as fc:
		corpus = fc.read().splitlines()

	gazetteer = ["BCH", "BP", "BM", "CB", "GV", "NV", "CĐCS", "CMHS", "MC", "GD", "GVBM","GVCN", "HĐSP", "HĐ", "HĐQT", "HS", "HT", "KTX", "PC-ĐBCL", "TH", "THCS", "THPT", "ThS", "TS", "UBND", "VNĐ"]

	gazetteer_lower = [x.lower() for x in gazetteer]	

	corpus = ''.join(corpus)
	length = len(corpus)
	final = []
	temp = ""
	for i in range(length):
		check = 0
		if corpus[i] == '.' or corpus[i] == '!' or corpus[i] == '?' or corpus [i] == ':':
			sent = temp.split()
			if sent[len(sent) - 1] in gazetteer or sent[len(sent) - 1] in gazetteer_lower:
				check = 1
			if check == 0:
				final.append(temp.strip())
				temp = ""
				continue
		temp = temp + corpus[i]	
		if i + 1 == length:
			final.append(temp.strip())

	pprint(final)
