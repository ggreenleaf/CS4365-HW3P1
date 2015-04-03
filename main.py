from sys import argv
import knowledge_base as kb

filename = argv[1]

kb = kb.KnowledgeBase(filename) 
valid = kb.resolution()
if valid:
 	kb.display()
else:
 	kb.display()
 	print "Failure"