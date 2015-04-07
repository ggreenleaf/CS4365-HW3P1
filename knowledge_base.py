from utils import get_parents

class KnowledgeBase:
	def __init__(self,filename):
		with open(filename) as f:
			lines = list(line for line in (l.strip() for l in f) if line) #need to ignore blank lines in file when reading
		
		self.kb = []
		i = 1
		for line in lines:
			self.kb.append((i," ".join(sorted(line.split(" "))),"{}"))
			i += 1
		
		

	def display(self):
		for num,clause,parents in self.kb:
			print "%i."%num,clause,parents
				
		print "Size of final clause set: %i"%len(self.kb)
	
	def display_solution(self):
		'''displays solution after testing validity of a clase'''

		solution_set = self.get_solution(get_parents(self.kb[-1]))
		solution_set.append(self.kb[-1]) #add False clause to solution set
		for i,clause,parents in sorted(set(solution_set), key=lambda x: x[0]):
			print i, clause, parents

		print "Size of final clause set: %i"%len(self.kb)
	


	def get_solution(self,parents):
		if not parents:
			return [] 
		else:
			clause1 = self.kb[parents[0] - 1]
			clause2 = self.kb[parents[1] - 1]
			return [clause1,clause2]+self.get_solution(get_parents(clause1)) + self.get_solution(get_parents(clause2))


	def negate_literal(self,lit):
		'''negates a single literal ~p ==> p or p ==> ~p''' 
		return lit[1:] if lit[0] == "~" else "~%s"%lit
	

	def resolve(self,c1,c2):
		'''removes contradictions in two clauses and returns list of clauses created'''
		clauses = []
		for a1 in c1[1].split(" "):
			for a2 in c2[1].split(" "):
				if a1 == self.negate_literal(a2) or a2 == self.negate_literal(a1):
					# new_clause = " ".join(set(self.remove(a1,c1) + self.remove(a2,c2) + self.remove(a2,c1)+ self.remove(a1,c2))) #remove repated literals 
					new_clause = " ".join(self.remove(c1,c2,a1,a2)) #create new clause removing instances of a1 and a2
					if not new_clause: #empty clause after remove means contradiction found
						new_clause = "False"
					
					clauses.append(new_clause)
		return clauses

		# return list of literals for new_clause 
	def remove(self,c1,c2,a1,a2):
		'''remove all instances of a1 and a2 from merged c1 and c2'''
		merged = filter(lambda x: x != a1 and x != a2, c1[1].split(" ") + c2[1].split(" "))

		# merged = self.resolve_contradictions(merged) #need to remove contradictions in merged clause
		return sorted(list(set(merged))) #sort merged to avoid adding multiple orders of the same literal (need combinations not permunations of clauses)
	
	def add_parents_to_clauses(self,clauses,p1,p2):
		return 	set([(clause, "{%i %i}"%(p1,p2))  for clause in clauses])			

	def get_kb_set(self):
		'''returns the set of the knowledge base where each element is a clause)'''
		return set([x[1] for x in self.kb]) 
	
	def are_clauses_subset(self,clauses):
		'''Returns True if the list of clauses is a subset of the knowledge base'''
		return set([x[0] for x in clauses]).issubset(self.get_kb_set())

	def add_to_kb(self,clauses):
		for c in clauses:
			if c[0] not in self.get_kb_set():
				self.kb.append((len(self.kb)+1, c[0],c[1]))

	def resolution(self):
		'''use resolution principle to test validity of clause a'''
		new_clauses = set() #set of tuples generated by resolve each element is clause,{parents_num}

		while True:
				n = len(self.kb)
				pairs = [(self.kb[i],self.kb[j]) for i in xrange(n) for j in xrange(i+1,n)] #generate pairs of clauses in kb to resolve contradictions
				for (c1,c2) in pairs: 
					resolvents = self.resolve(c1,c2) #list of clauses created by merging c1 and c2

					if "False" in resolvents: #if False is in resolvents then final contradiction has been found
						self.kb.append((len(self.kb) +  1, "False","{%i %i}"%(c1[0],c2[0]))) #adds False clause to knowldge base for displaying
						return True #Clause testing for validity is true
					
					#resolve_parents = [(clause, "{%i %i}"%(c1[0],c2[0]))  for clause in resolvents] #add parents to resolvents before adding to KB
					new_clauses.update(self.add_parents_to_clauses(resolvents,c1[0],c2[0])) #update new_clauses without adding repeated clauses

				if self.are_clauses_subset(new_clauses):#set([x[0] for x in new_clauses]).issubset(self.get_kb_set()): #if no new clauses have been added then clause tested is not valid
					return False

				self.add_to_kb(new_clauses) #added new clauses to knowledge base





