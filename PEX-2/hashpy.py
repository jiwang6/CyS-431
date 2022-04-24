import hashlib as hl
import random

def read_bin(filename):
	with open(filename, 'rb') as file:
		return file.read()

def hash_str(string):
	return hl.md5(string).hexdigest()


def find_collison(test_bin, hash, random_gen = True, 
					reset = True, hash_len = 5, max_length = 600000):
	original_bin = test_bin

	num_col = 0
	bytes_tried = 0
	successful_try = 0

	while True:
		for i in range(0xff):
			append_val = bytes([i])

			for j in range(0xff):
				test_val = bytes([j])
				temp_bin = test_bin + test_val
				test_tiny = hash_str(temp_bin)[:hash_len]
				bytes_tried += 1

				if test_tiny == hash:
					print(f"Collision #{num_col+1} found after {bytes_tried} " + 
						f"bytes (size: {bytes_tried-successful_try} bytes)")
					successful_try = bytes_tried
					num_col += 1

					with open(f"col/collision{num_col}.txt", 'wb') as file:
						file.write(temp_bin)
					print(f"Collision saved as file: collision{num_col}.txt")
					if num_col == 5:
						return
					if reset:
						test_bin = original_bin
			
			if bytes_tried - successful_try > max_length:
				test_bin = original_bin
				print(f"No hash found for {max_length} hashes,"
					+ " resetting binary")
				successful_try = bytes_tried

			if random_gen:
				test_bin += bytes([random.randint(0, 255)])
			else:
				test_bin += append_val

def cheat_alice(hash, price):
	byte_str = ("This is a contract between Alice and Bob. Alice agrees "
		+ "to sell to Bob her NFT art for a price of: $" + str(price))
	byte_str = bytes(byte_str, "utf-8")
	print(byte_str)

	invisible_arry = [chr(2000), chr(2001), chr(2002),
		chr(2003), chr(2004), chr(2005), chr(2006),
		chr(2007), chr(2008), chr(2009)]

	while True:
		#select random from invisible_arry
		rand_char = random.choice(invisible_arry)
		print(f"appending{rand_char}")
		byte_str += bytes(rand_char, "utf-8")
		test_tiny = hash_str(byte_str)[:5]
		#print(f"Trying: {test_tiny}")
		if test_tiny == hash:
			print("collision found")
			with open("col/collisionNFT.txt", 'wb') as file:
				file.write(byte_str)
		



if __name__ == "__main__":
	filename = "src-files/samplefile.txt"
	file_bin = read_bin(filename)
	md5_full = hash_str(file_bin)
	tiny_hash = md5_full[:5]

	#find_collison(file_bin, tiny_hash)
	cheat_alice(tiny_hash, 1)
	
