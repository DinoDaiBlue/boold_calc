def user_input():
	HDL_val = input("Please enter your HDl value here: ")
	HDL_num = float(HDL_val)
	return HDL_num
def check_HDL(HDL_num):
	if HDL_num >= 60:
		mes = "Normal"
		print("HDL value is {}, it is {}".format(HDL_num, mes))
	elif 40 <= HDL_num < 60:
		mes = "Borderline Low"
		print("HDL value is {}, it is {}".format(HDL_num, mes))
	else: 
		mes = "Low"
		print("HDL value is {}, it is {}".format(HDL_num, mes))
	return HDL_num, mes 
def driver():
	HDL_num = user_input()
	value, mes = check_HDL(HDL_num)
	return value, mes
value, mes = driver()
