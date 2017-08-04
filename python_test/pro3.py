import sys
import string

dic3 = dict()
dic5 = dict()
l = list()
l = ['Adduser','Hydra_FTP','Hydra_SSH','Java_Meterpreter','Meterpreter','Web_Shell']
for prefix in l:

	file1 = open(prefix+'_final_7gram.txt','r')
	file2 = open(prefix+'_end_7gram.txt','r')

	dic3.clear()
	dic5.clear()

	for line in file1:
		words = line.split()
		var = str(words[0]+" "+words[1]+" "+words[2])#the first 3 or 5 elements in 7 grma are also present in 5 gram and 3 gram so they are added to dic3 and dic5
		if not var in dic3:
			dic3[var] = int(words[8])# word[8] contains the count of each 7 gram as [0]-[6] are the grams and [7] is the --> symbol and [8] is the count
		else:
			dic3[var] += int(words[8])	

		var2 = str(words[0]+" "+words[1]+" "+words[2]+" "+words[3]+" "+words[4])
		if not var2 in dic5:
			dic5[var2] = int(words[8])
		else:
			dic5[var2] += int(words[8])	

	for line2 in file2:  #for the last line alone we have to consider the 3 and 5 grams occuring inside it apart from the starting grams of a 7 gram
		words = line2.split()
		for i in range(1,5):# if any doubt here call me @8876577559
			var3 = str(words[i]+" "+words[i+1]+" "+words[i+2])
			if var3 in dic3:
				dic3[var3] += int(words[8])
			else:
				dic3[var3] = int(words[8])		

		for j in range(1,3):
			var4 = str(words[j]+" "+words[j+1]+" "+words[j+2]+" "+words[j+3]+" "+words[j+4])
			if var4 in dic5:
				dic5[var4] += int(words[8])
			else:
				dic5[var4] = int(words[8])

	with open(prefix+'_final_3gram.txt','w') as m:
		for keys in dic3:
			m.write(str(keys)+" --> "+str(dic3[keys])+'\n')		

	with open(prefix+'_final_5gram.txt','w') as n:
		for keys1 in dic5:
			n.write(str(keys1)+" --> "+str(dic5[keys1])+'\n')

dic3.clear()
dic5.clear()	

file1 = open('normal_final_7gram.txt','r')

file2 = open('normal_end_7gram.txt','r')

for line in file1:
	words = line.split()
	#print(words[7])
	var = str(words[0]+" "+words[1]+" "+words[2])
	if not var in dic3:
		dic3[var] = int(words[8])
	else:
		dic3[var] += int(words[8])

	var2 = str(words[0]+" "+words[1]+" "+words[2]+" "+words[3]+" "+words[4])
	if not var2 in dic5:
		dic5[var2] = int(words[8])
	else:
		dic5[var2] += int(words[8])

for line2 in file2:
	words = line2.split()
	for i in range(1,5):
		var3 = str(words[i]+" "+words[i+1]+" "+words[i+2])
		if var3 in dic3:
			dic3[var3] += int(words[8])
		else:
			dic3[var3] = int(words[8])
			
	for j in range(1,3):
		var4 = str(words[j]+" "+words[j+1]+" "+words[j+2]+" "+words[j+3]+" "+words[j+4])
		if var4 in dic5:
			dic5[var4] += int(words[8])
		else:
			dic5[var4] = int(words[8])

with open('normal_final_3gram.txt','w') as m:
	for keys in dic3:
		m.write(str(keys)+" --> "+str(dic3[keys])+'\n')		

with open('normal_final_5gram.txt','w') as n:
	for keys1 in dic5:
		n.write(str(keys1)+" --> "+str(dic5[keys1])+'\n')		