from sys import argv
from knowledge_base import KnowledgeBase as KB 

filename = argv[1]


kb = KB(filename) 

valid = kb.resolution()
# print valid
# if valid:
# 	kb.display()
# else:
# 	kb.display()
# 	print "Failure"