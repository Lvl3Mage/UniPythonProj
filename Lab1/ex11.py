weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

IMC = weight/(height**2)

status = ''
if(IMC < 18.5):
	status = 'bajo peso'
elif(IMC < 25):
	status = 'peso normal'
elif(IMC < 30):
	status = 'sobrepeso'
elif(IMC < 40):
	status = 'obesidad'
else: 
	status = 'obesidad morbida'

print("IMC: {0} kg/m² => {1}".format(round(IMC,2), status))