from difflib import SequenceMatcher
from time import sleep
import selectors, sys

class Phrase():
	phrase = ""
	answer = ""
	phraseMeaning = ""
	answerMeaning = ""
	msg1 = ""
	msg2 = ""
	congrats = ""	

current_id = 0
lesson_PhraseList = []
error = 0

def StartLesson(lesson_number = 1):	
	#We create the objects of the lesson
	global current_id, lesson_PhraseList
	current_id = 0
	lesson_PhraseList = getLesson(lesson_number)
	return lesson_PhraseList[current_id].phrase


def getLesson(lesson_number):
	global lesson_PhraseList
	#In this part, we read and create the objects for the lesson
	lesson_file = open ("Marcus_Lessons/Lesson"+str(lesson_number)+".txt",'r')
	lesson_phrases = (lesson_file.read()).split("\n")
	lesson_file.close()
	for x in range(0, len(lesson_phrases), 7):
		lesson_PhraseList.append(Phrase())
		lesson_PhraseList[-1].phrase = lesson_phrases[x]
		lesson_PhraseList[-1].answer = lesson_phrases[x+1]
		lesson_PhraseList[-1].phraseMeaning = lesson_phrases[x+2]
		lesson_PhraseList[-1].answerMeaning = lesson_phrases[x+3]
		lesson_PhraseList[-1].msg1 = lesson_phrases[x+4]
		lesson_PhraseList[-1].msg2 = lesson_phrases[x+5]
		lesson_PhraseList[-1].congrats = lesson_phrases[x+6]

	return lesson_PhraseList


def CheckAnswer(user_answer):
	global current_id, lesson_PhraseList, error
	match = CompareAnswer(user_answer)
	Server_Answer = ""

	##If it's a good answer
	if match > 0.85:
		error = 0
		if current_id >= len(lesson_PhraseList)-1:
			current_id = current_id		
		else:
			current_id = current_id + 1
		Server_Answer = lesson_PhraseList[current_id].phrase
	else:
		if error > 1 :
			print("El error es mayor a 1")
			error = 0
		if error == 0:
			Server_Answer = "It is '" + lesson_PhraseList[current_id].answer + "', not '" +  user_answer +"'. Try again."
		else:
			print(lesson_PhraseList[current_id].msg2)
			Server_Answer = lesson_PhraseList[current_id].msg2
		error = error+1
	return	Server_Answer
	


	##else

def CompareAnswer(us_input):
	if len(us_input)>len(lesson_PhraseList[current_id].answer):
		us_input = us_input[0:len(lesson_PhraseList[current_id].answer)]
	return SequenceMatcher(a=lesson_PhraseList[current_id].answer.lower(),b=us_input.lower()).ratio()