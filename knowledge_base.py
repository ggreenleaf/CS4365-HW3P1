class KnowledgeBase:
	def __init__(self,filename):
		with open(filename) as f:
			data = f.read()
		
		self.kb = []
		i = 1
		for line in data.split("\n"):
			self.kb.append((i,line,"{}"))
			i += 1

	def display(self):
		for num,clause,parents in self.kb:
			print num,clause,parents

	def negate_literal(self,lit):
		'''negates a single literal ~p ==> p or p ==> ~p''' 
		return lit[-1] if lit[0] == "~" else "~%s"%lit
	
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
		union_set = ci[1].split(" ") + cj[1].split(" ")
		literals = union_set[:]
		# print clauses
		for i in union_set:
			negated = self.negate_literal(i)
			if negated in literals:
				literals.remove(negated)
				literals.remove(i)

		new_clause = (len(self.kb) + 1, " ".join(literals),"{%s %s}"%(str(cj[0]),str(ci[0])))
		return new_clause

	def resolution(self,a):
		'''use resolution principle to test validy of clause'''
		
		if a not in [x[1] for x in self.kb]:
			return "Clause not in Knowledge Base"


		self.negate_clause(a) #negate a then put in kb
		for num, clause, parents in self.kb:
			print num, clause, parents
		
		while True:
			cur_clause = self.kb[-1] #get last clause
			#find clause containing a negated literal in cur clause
			new_clause = self.resolve(cur_clause,self.find_clause(cur_clause))
			print new_clause[0], new_clause[1], new_clause[2]
			if new_clause[1] == '': 
				print "False"
				break
			elif new_clause == "Failure":
				print "Failure"
				break
			else:
				self.kb.append(new_clause)

	def find_clause(self,clause):
		'''finds a clause in knowledge base that contains a negated literal in clause'''		
		for l1 in clause[1].split(" "):
			for ci in self.kb:
				for l2 in ci[1].split(" "):
					if self.negate_literal(l1) == l2 :
						return ci
		return "Failure" 