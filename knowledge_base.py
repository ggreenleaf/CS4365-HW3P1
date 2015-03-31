

class KnowledgeBase:
	def __init__(self,filename):
		with open(filename) as f:
			data = f.read()
		
		self.kb = data.split("\n")

	def display(self):
		for clause in self.kb:
			print clause

	def negate_literal(self,lit):
		'''negates a single literal ~p ==> p or p ==> ~p''' 
		return lit[1] if lit[0] == "~" else "~%s"%lit
	
	def negate_clause(self, clause):
		'''negates a clause and inserts into kb'''
		for literal in clause.split(" "):
			negated = self.negate_literal(literal)
			if negated not in self.kb:
				self.kb.append(negated)

