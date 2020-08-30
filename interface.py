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
		elif choice =='1':
			value, mes = HDL.driver()			
			break
if __name__=="__main__":
	interface()
