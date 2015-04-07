#clause will be a tuple of 3 elements indx, clause, parents
def get_parents(clause):
	'''gets the 2 parents from a clause'''
	parent_string = clause[2]
	if len(parent_string) <= 2: #no parents {}
		return () #return empty tuple
	split = parent_string.split(" ")
	return (int(split[0][1:]),int(split[1][:-1]))
	

