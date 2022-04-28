import hashlib as hl
import random

def read_bin(filename):
	with open(filename, 'rb') as file:
		return file.read()

def hash_str(string):
	return hl.md5(string).hexdigest()


def find_collison(test_bin, tiny_val, reset = True, hash_len = 5, 
					max_length = 600000):
	
	# save original binary
	original_bin = test_bin

	# init params
	num_col = 0
	bytes_tried = 0
	successful_try = 0

	# main driver loop
	while True:
		for j in range(0xff): # try every binary value from 0 to 255
			test_val = bytes([j])
			temp_bin = test_bin + test_val # append bin
			test_tiny = hash_str(temp_bin)[:hash_len] # hash
			bytes_tried += 1

			#print(test_tiny)

			if test_tiny == tiny_val: # if collision, save to files, set params
				print(f"Collision #{num_col+1} found after {bytes_tried} " + 
					f"bytes (size: {bytes_tried-successful_try} bytes)")
	
				successful_try = bytes_tried
				num_col += 1

				with open(f"collisions/collision{num_col}.txt", 'wb') as file:
					file.write(temp_bin)
				print(f"Collision saved as file: collision{num_col}.txt")
				if num_col == 5:
					return
				if reset: # reset search
					test_bin = original_bin

		if bytes_tried - successful_try > max_length: # reset if too many tries
			test_bin = original_bin
			print(f"No hash found for {max_length} hashes,"
				+ " resetting binary")
			successful_try = bytes_tried
		
		test_bin += bytes([random.randint(0, 255)]) # add random after iters

def cheat_alice(tiny_val): 
	alt_contents = ("This is a contract between Alice and Bob. Alice agrees "
		+ "to sell to Bob her NFT art for a price of: $")

	alt_contents = bytes(alt_contents, "utf-8")

	orig = alt_contents # save original

	for price in range(100000): # try all prices
		alt_contents += bytes(str(price), "utf-8")

		alt_hash = hash_str(alt_contents)[:5]

		if alt_hash[:5] == tiny_val: # if match collision, save to file
			# alt_contents to file
			print(f"Found TinyHash Collision using this number: {price}")
			print("New contract saved to file: newcontract.txt")
			with open("collisions/newcontract.txt", "wb") as file:
				file.write(alt_contents)
			return

		alt_contents = orig
		
	return -1 # fail


if __name__ == "__main__":
	# init vars for textbook task
	filename = "src-files/samplefile.txt"
	file_bin = read_bin(filename)
	md5_full = hash_str(file_bin)
	tiny_hash = md5_full[:5]
	print(tiny_hash)
	find_collison(file_bin, tiny_hash)

	# init vars for NFT task
	filename = "src-files/contract.txt"
	file_bin = read_bin(filename)
	md5_full = hash_str(file_bin)
	tiny_hash = md5_full[:5]
	print(tiny_hash)

	cheat_alice(tiny_hash)


