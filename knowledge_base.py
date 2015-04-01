class KnowledgeBase:
	def __init__(self,filename):
		with open(filename) as f:
			data = f.read()
		
		self.kb = []
		i = 1
		for line in data.split("\n"):
			line_list = line.split(" ")
			line_list.sort()
			line = " ".join(line_list)
			self.kb.append((i,line,"{}"))
			i += 1

	def display(self):
		for num,clause,parents in self.kb:
			print num,clause,parents
		print "Size of final clause set: %i"%len(self.kb)
	
	def negate_literal(self,lit):
		'''negates a single literal ~p ==> p or p ==> ~p''' 
		return lit[1:] if lit[0] == "~" else "~%s"%lit
			  
	def negate_clause(self, clause):
		'''negates a clause and inserts into kb'''
		length = len(self.kb) + 1
		for literal in clause.split(" "):
			negated = self.negate_literal(literal)
			if negated not in [i[1] for i in self.kb]: 
				self.kb.append((length,negated, "{}"))
				length += 1
	
	def resolve(self,ci,cj):
		'''removes contradictions in two clauses and returns new clause'''
		#only resolve clauses if clause not already in kb
		union_set = ci[1].split(" ") + cj[1].split(" ")
		literals = list(set(union_set[:]))
		# print clauses
		# print literals
		# print "ci:", ci[1]
		# print "cj:",  cj[1]
		# print "literals:",literals
		for i in union_set:
			negated = self.negate_literal(i)
			if negated in literals:	
				literals.remove(negated)
				literals.remove(i)
		literals.sort()
		new_clause = (len(self.kb) + 1, " ".join(literals),"{%s %s}"%(str(cj[0]),str(ci[0])))
		if new_clause[1] not in [x[1] for x in self.kb]:
			if new_clause[1] == "":
				new_clause = (new_clause[0],"False",new_clause[2])

			self.kb.append(new_clause)
		
		return new_clause 

	def resolution(self,a):
		'''use resolution principle to test validy of clause a'''

		self.negate_clause(a) #start of algorithm will negate clause then instert into kb
		kb_indx = len(self.kb) - 1
		resolved_clauses = [] #list of parents who have already been resolved
		while True:
				# while kb_indx >= 0:
					
					cur_clause = self.kb[-1] #get last clause
			#find clause containing a negated literal in cur_clause
			#and remove contradictions
			#for example if kb contains p ~q and ~p this is a contradiction
					self.resolve(cur_clause,self.find_clause(cur_clause))
					if self.kb[-1][1] == "False":
						break
						# if resolved_clause[1] == '': #found final contradiction
							# resolved_clause = (resolved_clause[0], "False", resolved_clause[2])
						
						# resolved_clauses.append(resolved_clause)
						# kb_indx = len(self.kb) - 1 #resolved new clause re-set index to grab last clause
					last_clause = self.kb[-1]

					if last_clause == cur_clause: #if no new clause was added by resolve
						self.kb.append((len(self.kb) + 1,"Failure","{}"))
						break
					# else: #if no contradiction found for cur_clause look for contradiction of previous clause
					# 	kb_indx -= 1
					

					# if cur_clause[1] == "False":
					# 	self.kb.append((resolved_clause[0], "False", resolved_clause[2]))
					# 	break;

					# if resolved_clause[1] == '': 
				 # 	#	new_clause[1] = "False"
				 # 		
					# 	break
					# elif "Failure" in resolved_clause[1]:
					# 	print "Failure"
					# 	break
					# else:
					# 	if not resolved_clause in resolved_clauses:
					# 		self.kb.append(resolved_clause)				
					# 		kb_indx = len(self.kb) - 1
					# 	else:
					# 		kb_indx -= 1





				# if self.kb[-1][1] == "False" or kb_indx == 0:
				# 	break



	def find_clause(self,clause):
		'''finds a clause in knowledge base that contains a negated literal in clause'''		
		for atom1 in clause[1].split(" "):
			for ci in self.kb:
				for atom2 in ci[1].split(" "):
					if self.negate_literal(atom1) == atom2 :
						return ci
		

		# return ((len(self.kb) + 1, "Failure","{}"))
		return False
