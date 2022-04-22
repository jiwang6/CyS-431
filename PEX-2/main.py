#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : C1C Jim Wang
# Created Date: 21 April
# Documentation:
# ---------------------------------------------------------------------------

# import modules
from hashpy import hash_str, find_collison, read_bin


print("CyS 431 PEX2 - Hash Collider - by C/Wang")

print("\nStarting Task 1...\n")

hash_len = 5

filename = "src-files/samplefile.txt"	
file_bin = read_bin(filename)
md5_full = hash_str(file_bin)
tiny_hash = md5_full[:hash_len]

print(f"Running hash collision for file: {filename}")
print(f"Full MD5 digest is: {md5_full}")
print(f"TinyHash digest is: {tiny_hash}")

settings_bool = input("Settings? (y/n): ")
settings_bool = settings_bool == "y"

random_gen = "y"
reset_val = "y"
max_len = 600000

if settings_bool:
	random_gen = input("Random gen? (y/n): ")
	random_gen = random_gen == "y"

	reset_val = input("Reset file after every collision? (y/n): ")
	reset_val = reset_val == "y"


find_collison(file_bin, tiny_hash, random_gen, reset_val, hash_len, max_len)
