import sys
import string
import operator
import collections

l = list()
l = ['Adduser','Hydra_FTP','Hydra_SSH','Java_Meterpreter','Meterpreter','Web_Shell']
output = open('data_feature_set_for_5gram.txt','w')
f = 1
fdic = dict()
for prefix in l:
	dic = dict()
	dic.clear()
	file = open(prefix+'_final_5gram.txt','r')
	for line in file:
		words = line.split()
		s = str(words[0]+" "+words[1]+" "+words[2]+" "+words[3]+" "+words[4])
		k = int(words[6])
		if not s in dic:
			dic[s] = k
	n = len(dic)
	n = int(n*0.3)
	#sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
	for (keys,value) in collections.Counter(dic).most_common(n):
		#print(str(keys))
		if not keys in fdic:
			fdic[keys] = 1#distinct feature keys
			output.write(str(keys)+'\n')
			f = f+1#no of features in the feature set

dic = dict()
dic.clear()
file = open('normal_final_5gram.txt','r')
for line in file:
	words = line.split()
	s = str(words[0]+" "+words[1]+" "+words[2]+" "+words[3]+" "+words[4])
	k = int(words[6])
	if not s in dic:
		dic[s] = k
n = len(dic)
n = int(n*0.3)
#sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
for (keys,value) in collections.Counter(dic).most_common(n):
	#print(str(keys))
	if not keys in fdic:
		fdic[keys] = 1#distinct feature keys
		output.write(str(keys)+'\n')
		f = f+1#no of features in the feature set			