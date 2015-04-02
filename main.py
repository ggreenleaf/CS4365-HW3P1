from sys import argv
from knowledge_base import KnowledgeBase as KB 

filename = argv[1]
clause = argv[2]
# kb = KB("clauses.txt")

# # kb.resolution("~z y")
# # kb.display()

# kb = KB("task1.in")
# kb.resolution("LowTemp")
# kb.display()

kb = KB(filename)
kb.resolution(clause)
kb.display()
