from sys import argv
from knowledge_base import KnowledgeBase as KB 

filename = argv[1]
clause = argv[2]

kb = KB(filename)

valid = kb.resolution(clause)
if valid:
	kb.display()
else:
	kb.display()
	print "Failure"