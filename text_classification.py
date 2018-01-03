from nltk import sent_tokenize
from pprint import pprint

if __name__ == '__main__':
	with open('./data/class1.txt') as f1:
		class_1 = f1.read().splitlines()
	with open('./data/class2.txt') as f2:
		class_2 = f2.read().splitlines()
	#with open('./data/class3.txt') as f3:
	#	class_3 = f3.read().splitlines()
	#with open('./data/class4.txt') as f4:
	#	class_4 = f4.read().splitlines()
	with open('./data/test.txt') as ft:
		test = ft.read().splitlines()
	
	#priors
	class_1_prior = len(class_1)
	class_2_prior = len(class_2)
	
	p_class_1_prior = class_1_prior / (class_1_prior + class_2_prior)
	p_class_2_prior = class_2_prior / (class_1_prior + class_2_prior)
	
	vob_class_1 = ' '.join(class_1)
	vob_class_2 = ' '.join(class_2)
	vob_class_1 = vob_class_1.split()
	vob_class_2 = vob_class_2.split()
	#so tu cua moi class
	vob_class_1_not_set = len(vob_class_1)
	vob_class_2_not_set = len(vob_class_2)
	#tu vung chung
	vob_class_1_set = set(vob_class_1)
	vob_class_2_set = set(vob_class_2)
	vob = vob_class_1 + vob_class_2
	vob = set(vob) #tu vung
	vob_count = len(vob) #so tu vung 
	
	#dem lan xuat hien cua 1 tu trong doc
	dic_vob_class_1 = {}
	dic_vob_class_2 = {}
	
	for i in vob_class_1:
		dic_vob_class_1[i] = 0

	for j in vob_class_2:
		dic_vob_class_2[j] = 0
	
	for i in vob_class_1:
		dic_vob_class_1[i] = dic_vob_class_1[i] + 1

	for j in vob_class_2:
		dic_vob_class_2[j] = dic_vob_class_2[j] + 1

	for i in dic_vob_class_1:
		dic_vob_class_1[i] = (dic_vob_class_1[i] + 1) / (vob_class_1_not_set + vob_count)

	for j in dic_vob_class_2:
		dic_vob_class_2[j] = (dic_vob_class_2[j] + 1) / (vob_class_2_not_set + vob_count)
	#pprint(dic_vob_class_1)
	#pprint(dic_vob_class_2)
		
	#choose class
	test = ''.join(test)
	test = test.split()
	for u in test:
		if u not in vob:
			dic_vob_class_1[u] = 1 / (vob_class_1_not_set + vob_count)
			dic_vob_class_2[u] = 1 / (vob_class_2_not_set + vob_count)
		else:
			if u not in vob_class_1:
				dic_vob_class_1[u] = 1 / (vob_class_1_not_set + vob_count)
			elif u not in vob_class_2:
				dic_vob_class_2[u] = 1 / (vob_class_2_not_set + vob_count)

	prob_class_1 = p_class_1_prior
	prob_class_2 = p_class_2_prior
	for k in test:
		prob_class_1 = prob_class_1 * dic_vob_class_1[k]
		prob_class_2 = prob_class_2 * dic_vob_class_2[k]

	#print(prob_class_1)
	#print(prob_class_2)
	if prob_class_1 > prob_class_2:
		print('china')
	else:
		print('japan')
	
