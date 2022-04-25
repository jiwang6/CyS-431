import hashlib as hl
import random

def read_bin(filename):
	with open(filename, 'rb') as file:
		return file.read()

def hash_str(string):
	return hl.md5(string).hexdigest()


def find_collison(test_bin, tiny_val, random_gen = True, 
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

				if test_tiny == tiny_val:
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
			
			random_byte = bytes([random.randint(0, 255)])
			
			test_bin += random_byte if random_gen else append_val

def cheat_alice(tiny_val, price):
	
	byte_str = ("This is a contract between Alice and Bob. Alice agrees "
		+ "to sell to Bob her NFT art for a price of: $" + str(price))
	byte_str = bytes(byte_str, "utf-8")
	
	print(byte_str)

	print(tiny_val)

	original_bin = byte_str


	num_col = 0
	bytes_tried = 0
	successful_try = 0

	while True:
		for i in range(0xff):
			append_val = bytes([i])
			for j in range(0xff):
				test_val = bytes([j])
				temp_bin = byte_str + test_val
				test_tiny = hash_str(temp_bin)[:5]
				bytes_tried += 1

				if test_tiny == tiny_val:
					print(f"Collision #{num_col+1} found after {bytes_tried} " + 
						f"bytes (size: {bytes_tried-successful_try} bytes)")
					successful_try = bytes_tried
					num_col += 1

					with open(f"col/contract{num_col}.txt", 'wb') as file:
						file.write(temp_bin)
					print(f"Collision saved as file: contract{num_col}.txt")
					if num_col == 1:
						return
					byte_str = original_bin

			if bytes_tried - successful_try > 600000:
				byte_str = original_bin
				print(("No hash found for 600000 hashes, resetting binary"))
				successful_try = bytes_tried

			random_byte = bytes([random.randint(0, 255)])

			byte_str += random_byte
		



if __name__ == "__main__":
	# load files in and init vars
	filename = "src-files/samplefile.txt"
	file_bin = read_bin(filename)
	md5_full = hash_str(file_bin)
	tiny_hash = md5_full[:5]

	find_collison(file_bin, tiny_hash)


	filename = "src-files/contract.txt"
	file_bin = read_bin(filename)
	md5_full = hash_str(file_bin)
	tiny_hash = md5_full[:5]

	cheat_alice(tiny_hash, 1)
	
