from sys import argv
from knowledge_base import KnowledgeBase as KB 



kb = KB("clauses.txt")

kb.resolution("~p q")


