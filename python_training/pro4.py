import sys
import string
import operator
import collections

l = list()
l = ['Adduser','Hydra_FTP','Hydra_SSH','Java_Meterpreter','Meterpreter','Web_Shell']
output = open('data_feature_set.txt','w')
f = 1
fdic = dict()
fdic.clear()
for prefix in l:
	dic = dict()
	dic.clear()
	file = open(prefix+'_final_7gram.txt','r')
	for line in file:
		words = line.split()
		s = str(words[0]+" "+words[1]+" "+words[2]+" "+words[3]+" "+words[4]+" "+words[5]+" "+words[6])
		k = int(words[8])
		if not s in dic:
			dic[s] = k
	n = len(dic)
	n = int(n*0.3)# n is updated to 30% of n
	#sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
	for (keys,value) in collections.Counter(dic).most_common(n):# top 30% of n
		#print(str(keys))
		if not keys in fdic:# this is to remove duplications -- you need not worry about this
			fdic[keys] = 1
			output.write(str(keys)+'\n')
			f = f+1

dic.clear()	
file = open('normal_final_7gram.txt','r')
for line in file:
	words = line.split()
	s = str(words[0]+" "+words[1]+" "+words[2]+" "+words[3]+" "+words[4]+" "+words[5]+" "+words[6])
	k = int(words[8])
	if not s in dic:
		dic[s] = k
n = len(dic)
n = int(n*0.3)# n is updated to 30% of n
#sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
for (keys,value) in collections.Counter(dic).most_common(n):# top 30% of n
	#print(str(keys))
	if not keys in fdic:# this is to remove duplications -- you need not worry about this
		fdic[keys] = 1
		output.write(str(keys)+'\n')		