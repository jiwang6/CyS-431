#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : C1C Jim Wang
# Created Date: 21 April
# Documentation:
# ---------------------------------------------------------------------------

# import modules
from hashpy import hash_str, find_collison, read_file


print("CyS 431 PEX2 - Hash Collider - by C/Wang")

print("\nStarting Task 1...\n")

hash_len = 5

filename = "samplefile.txt"
file_bin = read_file(filename)
md5_full = hash_str(file_bin)
tiny_hash = md5_full[:hash_len]

print(f"Running hash collision for file: {filename}")
print(f"Full MD5 digest is: {md5_full}")
print(f"TinyHash digest is: {tiny_hash}")

random_gen = input("Random gen? (y/n): ")
random_gen = random_gen == "y"

reset_val = input("Reset file after every collision? (y/n): ")
reset_val = reset_val == "y"
find_collison(file_bin, tiny_hash, random_gen)
