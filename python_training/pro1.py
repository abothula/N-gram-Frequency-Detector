import sys
import glob
import string

l = list()
l = ['Adduser','Hydra_FTP','Hydra_SSH','Java_Meterpreter','Meterpreter','Web_Shell']# list of prefixes for each folder
for prefix in l:
	for i in range(1,8):
		path = '/home/abothula/ADFA-LD/ADFA-LD/Attack_Data_Master/' + prefix + '_' + str(i) + '/*.txt'#the directories we are working with
		files = sorted(glob.glob(path))

		with open('attack_sevengram_' + prefix + '.txt','a') as result:# instead of concatanating i am writing 7 grams just like that without considering occurence or duplication
			for name in files:
				f = open(name,'r')
				numbers = f.readline()
				numbers = string.split(numbers)
				el1 = numbers[0]
				el2 = numbers[1]
				el3 = numbers[2]
				el4 = numbers[3]
				el5 = numbers[4]
				el6 = numbers[5]
				el7 = numbers[6]

				j = 7

				while j < len(numbers):
					result.write(el1+" "+el2+" "+el3+" "+el4+" "+el5+" "+el6+" "+el7+"\n")
					el1 = el2
					el2 = el3
					el3 = el4
					el4 = el5
					el5 = el6
					el6 = el7
					el7 = numbers[j]	
					j = j+1
				result.write(el1+" "+el2+" "+el3+" "+el4+" "+el5+" "+el6+" "+el7+"\n")# writing into attack_sevengram_adduser and so on
				result.write("$ "+el1+" "+el2+" "+el3+" "+el4+" "+el5+" "+el6+" "+el7+"\n")#these are the last 7 gram of each txt file and they are marked using $



path = '/home/abothula/ADFA-LD/ADFA-LD/Training_Data_Master/*.txt'
files = sorted(glob.glob(path))

with open('normal_sevengram.txt','w') as result:
	for name in files:
		f = open(name,'r')
		numbers = f.readline()
		numbers = string.split(numbers)
		el1 = numbers[0]
		el2 = numbers[1]
		el3 = numbers[2]
		el4 = numbers[3]
		el5 = numbers[4]
		el6 = numbers[5]
		el7 = numbers[6]

		i = 7

		while i < len(numbers):
			result.write(el1+" "+el2+" "+el3+" "+el4+" "+el5+" "+el6+" "+el7+"\n")
			el1 = el2
			el2 = el3
			el3 = el4
			el4 = el5
			el5 = el6
			el6 = el7
			el7 = numbers[i]	
			i = i+1
		result.write(el1+" "+el2+" "+el3+" "+el4+" "+el5+" "+el6+" "+el7+"\n")
		result.write("$ "+el1+" "+el2+" "+el3+" "+el4+" "+el5+" "+el6+" "+el7+"\n")
