no_alias = df_2['Gene Symbol']

what_i_want = []


for id in no_alias:
	#Split on Space. Turns 'AA1 AA11' into ['AA1','AA11']
	temp = id.split(' ')
	
	#Add the string object of form ['AA1','AA11'] to the list what_i_want
	what_i_want.append(temp)
	
#list comprehension to select only first elements
what_i_actually_want = [id_pair[0] for id_pair in what_i_want]
	