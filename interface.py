import HDL
def interface():
	while True:
		print("My Program")
		print("Options: ")
		print("9 - Quit")
		print("1 - HDL_Analysis")
		choice = input("Enter your choice: ")
		if choice =='9':
			break
		if choice =='1':
			value, mes = driver()			
			break
interface()
