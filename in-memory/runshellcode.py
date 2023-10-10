import ctypes
import mmap

# This shellcode will print "Hello World from shellcode!"
shellcode = b"hed \x0b\x814$\x01\x01\x01\x01H\xb8 shellcoPH\xb8rld fromPH\xb8Hello WoPj\x01Xj\x01_j\x1cZH\x89\xe6\x0f\x05XXXX\xc3"

# Allocate an executable memory and write shellcode to it
mem = mmap.mmap(
    -1,
    mmap.PAGESIZE,
    mmap.MAP_SHARED,
    mmap.PROT_READ | mmap.PROT_WRITE | mmap.PROT_EXEC,
)
mem.write(shellcode)

# Get actuall mmap address
# Assuming x64
addr = int.from_bytes(ctypes.string_at(id(mem) + 16, 8), "little")

# Create the function
functype = ctypes.CFUNCTYPE(ctypes.c_void_p)
fn = functype(addr)

# Run shellcode
fn()

