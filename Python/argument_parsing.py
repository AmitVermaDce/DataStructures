import sys
import getopt

# print("file name:",sys.argv[0])
# print("Message:", sys.argv[1])

opts, args = getopt.getopt(sys.argv[1:], "f:m:")
print(opts)
print(args)
