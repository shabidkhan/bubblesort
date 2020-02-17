list1=[11,2,3,4,4,786,2,2,122,27]
i=0
while (i<len(list1)-1):
	if list1[i]>list1[i+1]:
		list1[i],list1[i+1]=list1[i+1],list1[i]
		i=0
	else:
		i+=1
print(list1)
	
