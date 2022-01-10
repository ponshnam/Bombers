from numspy import Way2sms

try:
	w2s = Way2sms()

	mobile_number= int(input("+380684428743: "))
	message= input("Коля бот: ")
	n = int(input("10 (limit is 1000/day): "))

	username = input("Петя: ")
	password = input("Katess: ")
	w2s.login(username,password)

	for i in range(0,n):
		w2s.send(mobile_number,message)
		print(str(i+1)+" messages sent!")

	w2s.logout()
except Exception as e: 
	print("Something is wrong try again!")
