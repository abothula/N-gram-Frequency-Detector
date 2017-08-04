# this code is all about finding the occurence of the feature set in our training set(70% of each adduser , hydra ftp and so on) 
import sys
import string

l = list()
l = ['Adduser','Hydra_FTP','Hydra_SSH','Java_Meterpreter','Meterpreter','Web_Shell']
output = open('match7.txt','w')
read_file = open('data_feature_set.txt','r')
data_list = list()
dic = dict()
for line in read_file:
	line = line.rstrip('\n')
	data_list.append(line)
read_file.close()

for prefix in l:
	print("running for "+prefix)
	read_file = open('attack_sevengram_'+prefix+'.txt','r')
	for line in read_file:
		if line[0] != '$':
			line = line.rstrip('\n')
			if line not in dic:
				dic[line] = 1
			else:
				dic[line] += 1		
		else:
			for i in range(0,len(data_list)):
				if data_list[i] in dic:
					output.write(str(dic[data_list[i]])+" ")
				else:	
					output.write('0 ')	
			output.write(prefix+'\n')
			dic.clear()	



read_file = open('normal_sevengram.txt','r')
i = 1
print("running for validation")
for line in read_file:
	if line[0] != '$':
		line = line.rstrip('\n')
		if line not in dic:
			dic[line] = 1
		else:
			dic[line] += 1	
	else:	
		for i in range(0,len(data_list)):
			if data_list[i] in dic:
				output.write(str(dic[data_list[i]])+' ')
			else:
				output.write('0 ')	
		output.write('normal\n')
		dic.clear()


#print("completed file no "+str(i))	
#i = i+1	