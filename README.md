Homework 3 programming assignment

The Resolution Principle in Python
Geoffrey Greenleaf
Sebastian Young

<h1>Project Overview</h1>
The Project is an implementation of the resolution algorithm given in the book on page 255. The project was devolped using python2.7 on OSX 10.10 and Windows 7. Any computer running python2.7 should be able to run the program. 

<h2>Running the program</h2>
After unzipping the project folder to run the program type the command
	
	python main.py [file]. 

The file is the list of clauses seperated by new lines with the last clause being the negated clause you are testing.
Before running a example from the homework you will need to uncomment a line and comment one. 
Since the negated clause for testing is already inputed into the file the knowledgebase can not determine which clause it is testing
It only resolves the clauses read from the file. 
	
To fix this uncomment the line 

	in main.py
		kb.display_solution() and comment the line above it kb.display()
	in knowledge_base.py
		add this line to the __init__ function at the end
		self.test_clause = "<clause for testing and negated literals in clause>"

		For example if you wanted to test the validity of ~z y like in the first example

		your __init__ function would look similiar to this

		def __init__(self,filename):
			...
			self.test_clause = "~z y ~y z"

		after these changes you can run the program as told above	


