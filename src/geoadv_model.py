class GeoAdvModel:
	'''This is where the state of the game exists as well as
	any interaction with the database.'''
			'''initializes the model with the specified database'''
	
	old_questions = {}	#old questions
	connection	#	connection to DB
	r	#random number
	current_answer
	profession
	current_country

	def __init__(self, database):
		'''initializes the model with the specified database'''
	
		old_questions = {}	#old questions
		connection	#	connection to DB
		r	#random number
		current_answer
		profession
	
	
	def nextQuestion(self):
		countries = connection.cursor()
		question = connection.cursor()	


		symbol1 = (country,)
		symbol2 = (profession,)
		table.execute('select * from questions where cid = (select cid from countries where name = ?) AND qid in (select qid from questions_tags where tid in (select tid from proftags where pid = (select pid from profession where name = ?)))',symbol1,symbol2)
		
		#need to fix
		possible_question = {}
		for row in table:
			if row[0] not in old_questions:
				possiblequestion.append(row)
		b = r.randint(0,possible_question.length())
		return_row = possible_question[b]	
		old_question.append(return_row[0])
		return return_row
	
	def is_correct(self):
		corrected = spell_correction(current_answer)
		if corrected == answer and corrected == current_answer:
			print 'Perfect, you are right'
			choose_next_country(self)
			nextQuestion(self)
		elif corrected == answer and corrected != current_answer:
			print 'You are right but notice the correct spell for word' + current_answer + " is" + corrected
		else:
			print 'You are wrong'
			#repeat question? or next? not sure.  
		
	#return the answer parsed through spell correction	
	def spell_correction(self):
		parsed
		#current answer processed here.				
		return parsed
	
	#reset random number from 0 to n
	def resetR(n):
	
	#Choose next country(May or may not happen when called based on current gaming state)
	def choose_next_country(self):
			

