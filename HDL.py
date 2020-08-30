def user_input():
	HDL_val = input("Please enter your HDl value here: ")
	HDL_num = float(HDL_val)
	return HDL_num
def check_HDL(HDL_num):
	if HDL_num >= 60:
		mes = "Normal"
	elif 40 <= HDL_num < 60:
		mes = "Borderline Low"	
	else: 
		mes = "Low"
	return HDL_num, mes
def HDL_output(HDL_num, mes):
	print("HDL value is {}, it is {}".format(HDL_num, mes)) 
def driver():
	HDL_num = user_input()
	value, mes = check_HDL(HDL_num)
	HDL_output(value, mes)
	return value, mes
value, mes = driver()
