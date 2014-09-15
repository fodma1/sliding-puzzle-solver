import sys


def change(_str,x,y):
	if (x>y):
		return change(_str,y,x)	
	#x=x-1
	#y=y-1
	first=_str[:x]
	middle=_str[x+1:y]
	if y<8:
		_end=_str[y+1:]
	else:
		_end=''
	return first+_str[y]+middle+_str[x]+_end

def variations(element,checked):
	_str=element[0]
	pos=_str.find('f')
	results=[]
	#print str(pos/3)+'\t'+str(pos%3)
	if pos/3>0:
		res=[change(_str,3*(pos/3)+pos%3,3*(pos/3-1)+pos%3),element[1]+'d',_str]
		if element[2]!=res and (not res in checked):
			results.append(res)
	if pos/3<2:
		res=[change(_str,3*(pos/3)+pos%3,3*(pos/3+1)+pos%3),element[1]+'u',_str]
		if element[2]!=res and (not res in checked):
			results.append(res)
	if pos%3>0:
		res=[change(_str,3*(pos/3)+pos%3-1,3*(pos/3)+pos%3),element[1]+'r',_str]
		if element[2]!=res and (not res in checked):
			results.append(res)
	if pos%3<2:
		res=[change(_str,3*(pos/3)+pos%3+1,3*(pos/3)+pos%3),element[1]+'l',_str]
		if element[2]!=res and (not res in checked):
			results.append(res)
	return results

def kiFile(_str):
	of=open('log.txt','a')
	of.write(_str+'\n')
	of.close()
	
def main():
	aim='12345678f'
	inpt=sys.argv[1]
	#1234567f8
	checked=[inpt]
	result=''
	tocheck=[[inpt,' ','']]
	ok=False
	_len=len(tocheck)

	pathlen=0

	while (_len>0) and (not ok):
		temp=variations(tocheck[0],checked)
		for i in temp:
			if pathlen<len(i[1]):
				pathlen=len(i[1])
				print pathlen
			if aim==i[0]:
				result=i[1]
				print i
				ok=True
			tocheck.append(i)
			kiFile(i[0])
			checked.append(i[0])
		#print tocheck[0:1]
		tocheck.pop(0)
	print result
	return 0

if __name__=='__main__':
	main()
