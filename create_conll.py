import numpy as np
import pickle
import collections


# x = pickle.load(open("../../conll2012/review_train_token.pkl", "rb"))
# y = pickle.load(open("../../conll2012/review_val_token.pkl", "rb"))
# z = pickle.load(open("../../conll2012/review_test_token.pkl", "rb"))

x = pickle.load(open("../../german_small_updated/german_train2_token.pkl", "rb"))
y = pickle.load(open("../../german_small_updated/german_val2_token.pkl", "rb"))
z = pickle.load(open("../../german_small_updated/german_test2_token.pkl", "rb"))

pred_path = 'german/sents/train.txt'

fc = 0
with open(pred_path, 'a') as fp:
	#for data_kind in [x,y,z]:
	for data_kind in [x]:

		for p in range(len(data_kind)):
			fc+=1
			#if p % 50 == 0:	
				# data_kind[p].insert(0, 'SOS')
				# data_kind[p].append('EOS')
				# data_kind[p].append('PAD')
			
			sent = ' '.join(word for word in data_kind[p])
			fp.write(sent)
			fp.write("\n")