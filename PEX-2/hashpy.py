import hashlib as hl
import random

def read_file(filename):
	with open(filename, 'rb') as file:
		return file.read()

def hash_str(string):
	return hl.md5(string).hexdigest()


def find_collison(test_bin, hash, random_gen = True, reset = True, hash_len = 5, max_length = 600000):
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
					print(f"collision #{num_col} found after {bytes_tried} bytes (size: {bytes_tried-successful_try} bytes)")
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
				print(f"No hash found for {max_length} hashes, resetting binary")
				successful_try = bytes_tried

			test_bin += bytes([random.randint(0, 255)]) if random_gen else append_val

if __name__ == "__main__":
	
	filename = "samplefile.txt"
	file_bin = read_file(filename)
	md5_full = hash_str(file_bin)
	tiny_hash = md5_full[:5]

	find_collison(file_bin, tiny_hash)