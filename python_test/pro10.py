import sys
import string

data_list = list()
output = open('test.txt','w') 
read_file = open('data_feature_set_for_3gram.txt','r')
for line in read_file:
	line = line.rstrip('\n')
	data_list.append(line)	
read_file.close()
for elem in data_list:
	print(elem)	
dic = dict()
read_file = open('normal_sevengram.txt','r')
for line in read_file:
	if line[0]!='$':
		line = line.rstrip('\n')
		word = line.split()
		gram = word[0]+" "+word[1]+" "+word[2]
		if gram not in dic:
			dic[gram] = 1
		else:
			dic[gram] += 1
	else:
		line = line[2:]
		line = line.rstrip('\n')
		words = line.split()
		for i in range(1,5):
			var = str(words[i]+" "+words[i+1]+" "+words[i+2])
			if var in dic:
				dic[var] += 1
			else:
				dic[var] = 1	
		for i in range(0,len(data_list)):
			if data_list[i] in dic:
				output.write(str(dic[data_list[i]])+" ")
			else:
				output.write("0 ")
		output.write("normal\n")
		dic.clear()			
"""for keys in dic:
	print(keys+" "+str(dic[keys]))
"""