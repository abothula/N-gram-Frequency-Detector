import sys
import string

dic = dict()
pic = dict()
l = list()
l = ['Adduser','Hydra_FTP','Hydra_SSH','Java_Meterpreter','Meterpreter','Web_Shell']#same as before
for prefix in l:
	dic.clear()
	pic.clear()
	file = open('attack_sevengram_'+prefix+'.txt','r')
	for line in file:
		line = line.rstrip('\n')
		if line[0]!="$":# if $ not seen its a normal sevengram and its added to diictionary .... dictionary stores the occurence of each 7gram present
			if line in dic:
				dic[line] += 1
			else:
				dic[line] = 1
		else:
			line = line[2:]
			if line in pic:
				pic[line] += 1
			else:
				pic[line] = 1

	with open(prefix+'_final_7gram.txt','w') as m:
		for keys in dic:
			m.write(str(keys)+" --> "+str(dic[keys])+'\n')# writing dictionary keys along with its occurence to the final 7 gram.txt for each type

	with open(prefix+'_end_7gram.txt','w') as n:
		for keys in pic:
			n.write(str(keys)+" --> "+str(pic[keys])+'\n')# these are the exclusively the last lines of each text files

dic.clear()
pic.clear()

file = open('normal_sevengram.txt','r')

for line in file:
	line = line.rstrip('\n')
	if line[0]!="$":
		if line in dic:
			dic[line] += 1
		else:
			dic[line] = 1
	else:
		line = line[2:]
		if line in pic:
			pic[line] += 1
		else:
			pic[line] = 1

with open('normal_final_7gram.txt','w') as m:
	for keys in dic:
		m.write(str(keys)+" --> "+str(dic[keys])+'\n')

with open('normal_end_7gram.txt','w') as n:
	for keys in pic:
		n.write(str(keys)+" --> "+str(pic[keys])+'\n')