from sys import argv

class ClauseSet:
	def __init__(self,filename):
		with open(filename) as f:
			data = f.read()
		
		self.clause_set = data.split("\n")

	def display(self):
		for clause in self.clause_set:
			print clause
	
	def negate_clause(self,clause):
		'''negates a clause and inserts into clause_set'''
		negate_literal = lambda x: x[1] if x[0] == "~" else "~"+x

		for literal in clause.split(" "):
			negated = negate_literal(literal)
			if negated not in self.clause_set:
				self.clause_set.append(negated)
		
if __name__ == "__main__":

	clauses = ClauseSet(argv[1])
	print "before negation of clause 0"
	clauses.display()

	clauses.negate_clause(clauses.clause_set[0])
	print "after negation of clause 0"
	clauses.display()