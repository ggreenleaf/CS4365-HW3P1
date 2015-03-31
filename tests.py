from knowledge_base import KnowledgeBase

class Test:
	def __init__(self):
		self.kb = KnowledgeBase("tests.txt")

	def test_literal_negation(self):
		assert self.kb.negate_literal("~s") == "s"
		assert self.kb.negate_literal("s") == "~s"

	def test_clause_negation(self):
		new_kb = self.kb.kb[:].extend(["c","~d"])
		assert self.kb.negate_clause(self.kb.kb[2]) == new_kb



if __name__ == "__main__":
	tests = Test()
	tests.test_literal_negation()
	tests.test_clause_negation()