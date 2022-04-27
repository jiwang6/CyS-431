#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : C1C Jim Wang
# Created Date: 27 April
# Documentation: none.
# ---------------------------------------------------------------------------

# import modules
from hashpy import hash_str, find_collison, read_bin, cheat_alice


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

random_gen = "y"
reset_val = "y"
max_len = 600000

find_collison(file_bin, tiny_hash, random_gen, hash_len, max_len)

print("\nStarting task 2...\n")
print("Running Hash Collision for file: contract.txt")
cont_hash = hash_str(read_bin('src-files/contract.txt'))
print(f"Full MD5 digest is: {cont_hash}")
print(f"TinyHash digest is: {cont_hash[:5]}")



cheat_alice(cont_hash[:5])