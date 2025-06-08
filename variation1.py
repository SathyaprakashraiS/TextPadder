menuflag=True
chosen=1 #num->message 2 message->number=1

keypairs={1:"`",2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],
8:["t","u","v"],9:["w","x","y","z"],0:[" "]}

def encode(w):
	encodedvalue=""
	q=w.split()
	for i in q:
		for j in i:
			val=next((i for i in keypairs.values() if j in i), None)
			key=next((i for i in keypairs.keys() if val == keypairs[i]), None)
			if ((key==None) or (val==None)):
				raise Exception("Unknown input identified Exiting program...")
			index=val.index(j)
			encodedvalue+=(index+1)*str(key)
		encodedvalue+=" "

	return encodedvalue

def decode(w):
	message=""
	contents=w.split()
	for i in contents:
		repeated=1
		for j in range(len(i)-1):
			if j=="0":
				message+=" "
			elif i[j]==i[j+1]:
				repeated+=1
				if j+1==len(i)-1:
					letters=keypairs[int(i[j+1])]
					message+=letters[repeated-1] 
			else:
				letters=keypairs[int(i[j])]
				if repeated<=len(letters):
					message+=letters[repeated-1]
				else:
					repeated=repeated%len(letters)
					message+=letters[repeated-1]
				repeated=1
				if j+1==len(i)-1:
					letters=keypairs[int(i[j+1])]
					message+=letters[repeated-1]
		message+=" "
	return message

code1="99966688 277733 7777446667778"

print("This program is to give number codes for message that needs to be sent via numberpad mobiles and can also decode the message sent using the numberpad")
print("what do you want to do?")
print("enter 1 to pass a message and get the encoded number pattern")
print("enter 2 to pass the number pattern to decode the message in it")

while menuflag:
	q=int(input("enter 1 or 2: "))
	if q not in [1,2]:
		print("identified invalid input... please only input either 1 or 2")
	else:
		menuflag=False
		chosen=q

if chosen==1:
	codedmsg=""
	print("any numbers in the message will also be removed from the message")
	w=input("enter you message that you want to convert to number pattern: ")
	w=w.lower()
	codedmsg=encode(w)
	print(f"user entered message: {w}")
	print(f"the encoded message is: {codedmsg}")
else:
	decodedmsg=""
	w=input("enter the number pattern you have to decode the message: ")
	decodedmsg=decode(code1)
	print(f"the decoded message: {decodedmsg}")
print("testing")