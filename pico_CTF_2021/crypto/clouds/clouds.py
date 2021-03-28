#!/usr/bin/python2 -u
import binascii

ROUNDS = 5
BLOCK_LEN = 8
HEX_BLOCK_LEN = BLOCK_LEN * 2
MAX_NOTES = 2048
MAX_NOTE_LEN = 512


def pad(p):
	if len(p) % BLOCK_LEN != 0:
		return p + "\0" * (BLOCK_LEN - (len(p) % BLOCK_LEN))
	else:
		return p

def g(i):
	b = bin(i).lstrip("0b").rstrip("L").rjust(BLOCK_LEN * 8, "0")
	return int(b[::-1], 2)

def encrypt_block(b):
	k = open("./key").read().rstrip()
	assert (len(b) * ROUNDS) == len(k)
	result = int(binascii.hexlify(b), 16)
	for i in range(ROUNDS):
		key = int(binascii.hexlify(k[i * BLOCK_LEN:(i + 1) * BLOCK_LEN]), 16)
		key_odd = key | 1
		result ^= key
		result = g(result)
		result = (result * key_odd) % (1 << 64)
	return hex(result).lstrip("0x").rstrip("L").rjust(HEX_BLOCK_LEN, "0")

def encrypt(msg):
	plain = pad(msg)
	result = ""
	for i in range(0, len(plain), BLOCK_LEN):
		result += encrypt_block(plain[i:i + BLOCK_LEN])
	return result

def menu(n):
	notes = n
	print("""
1) Store
2) Retrieve
Anything else to quit
""")
	ui = raw_input("Selection? ").rstrip()
	if ui == "1":
		if len(notes) >= MAX_NOTES:
			print("Max capacity")
			return notes
		ui = raw_input("Give me a note to encrypt: ").rstrip()
		try:
			msg = binascii.unhexlify(ui)
		except:
			print("Invalid input.")
			return notes
		if len(msg) > MAX_NOTE_LEN:
			print("Invalid input.")
		else:
			notes.append(encrypt(msg))
	elif ui == "2":
		ui = raw_input("What index would you like to read? ").rstrip()
		try:
			index = int(ui)
		except:
			print("Invalid index.")
			return notes
		if index >= 0 and index < len(notes):
			print(notes[index])
		else:
			print("Invalid index.")
	else:
		return None
	return notes


art = """
		      .

		      |
	     .               /
	      \       I
			  /
		\  ,g88R_
		  d888(`  ).                   _
	 -  --==  888(     ).=--           .+(`  )`.
	)         Y8P(       '`.          :(   .    )
		.+(`(      .   )     .--  `.  (    ) )
	       ((    (..__.:'-'   .=(   )   ` _`  ) )
	`.     `(       ) )       (   .  )     (   )  ._
	  )      ` __.:'   )     (   (   ))     `-'.:(`  )
	)  )  ( )       --'       `- __.'         :(      ))
	.-'  (_.'          .')                    `(    )  ))
			  (_  )                     ` __.:'

	--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.

"""

print(art)
print("I love cloud watching, so I made a place to store all my notes about them.")

flag = open("./flag").read().rstrip()
notes = [encrypt(flag)]
notes = menu(notes)
while notes:
	notes = menu(notes)
