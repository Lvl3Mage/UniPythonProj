def EvalGrade(grade):

	if(grade < 0 or grade > 10):
		print('Grade {0} cannot exist'.format(grade))
		return None

	if(grade < 5):
		print('Suspenso')

	elif(grade < 7):
		print('Aprobado')

	elif(grade < 9):
		print('Notable')

	elif(grade < 10):
		print('Sobresaliente')

	else:
		print('Matricula de Honor')

EvalGrade(float(input("Input your grade: ")))
