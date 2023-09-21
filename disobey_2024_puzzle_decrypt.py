# This script decrypts .enc files found in Disobey 2024 Puzzle

import sys

hardcoded_key = b"\x55\x48\x89\xe5\x48\x81\xec\xe0\x00\x00\x00\x89\xbd\x2c\xff\xff"

user_key = b"\xb5\x75\x41\xdb\x1d\xd0\x6c\x03\x50\x16\xa2\x59\xd9\x7b\x68\x7d"

file_data = bytearray()

with open(sys.argv[1], 'rb') as file:
	file_data = bytearray(file.read())


def remove_trailing_zeros(byte_array):
    i = len(byte_array) - 1
    while i >= 0 and byte_array[i] == 0x30:
        i -= 1
    trimmed_byte_array = byte_array[:i+1]
    return trimmed_byte_array

def calculate_key(br1, br2):
	new_key = bytearray(a ^ b for a, b in zip(br1, br2))
	return new_key

def decode_file(byte_array):
	first_key = calculate_key(hardcoded_key, user_key)
	new_key = bytearray()
	row = bytearray(16)
	result = bytearray()
	for i in range(0, len(byte_array), 16):
		chars = byte_array[i:i + 16]
		if not new_key:
			row = bytearray(a ^ b for a, b in zip(chars, first_key))
		else:
			row = bytearray(a ^ b for a, b in zip(chars, new_key))
		new_key = calculate_key(user_key, chars)
		result.extend(row)
	return result

def main():
	
	decoded_file = decode_file(file_data)
	untrailed_file = remove_trailing_zeros(decoded_file)
	output = untrailed_file[1:]
	with open('decrypted.bin', 'wb') as file:
		file.write(output)

if __name__ == "__main__":
    main()
