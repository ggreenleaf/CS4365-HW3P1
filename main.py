from sys import argv
import knowledge_base as kb

filename = argv[1]

kb = kb.KnowledgeBase(filename) 

valid = kb.resolution()
if valid:
 	#kb.display() 
	kb.display_solution() #will only run if you uncomment the right line from knowledge_base init
else:
 	kb.display()
 	print "Failure"