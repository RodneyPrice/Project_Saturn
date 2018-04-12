#!/usr/bin/python3
#Author rodney_price():



from tkinter import *

master = Tk()

master.iconbitmap('cipher_gui.ico')

master.title("Cipher")


Label(master, text="Plain Text").grid(row=0)
Label(master, text="Shift Key").grid(row=1)
Label(master, text="Cipher Message").grid(row=2)

fire = Entry(master)
fire.grid(row = 2, column = 1)
p_textl = Entry(master)
shift_key = Entry(master)

p_textl.grid(row=0, column=1)
shift_key.grid(row=1, column=1)

def sentence_encode_withpun():
	fire.delete(0, END)
	lstc = []
	p_text = str(p_textl.get())
	p_text = p_text.replace(" ", "")
	p_text = p_text.upper()
	lst = list(p_text)
	for letter in lst:
		letter = ord(letter) - ord('A')
		if (letter >= 0 and letter <= 26):
			letter = (letter + int(shift_key.get())) % 26
		letter = chr(int(letter + ord('A')))
		lstc.append(letter)
	cmessage = "".join(lstc)
	fire.insert(0, cmessage)

Button(master, text='Hide Data', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Encipher', command=sentence_encode_withpun).grid(row=3, column=1, sticky=W, pady=4)



mainloop( )