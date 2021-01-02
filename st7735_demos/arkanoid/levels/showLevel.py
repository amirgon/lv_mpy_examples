#!/opt/bin/lv_micropython
from os import stat
import sys

if len(sys.argv) < 2:
    print("Usage: %s level filename"%sys.argv[0])
    sys.exit()

level_size = stat(sys.argv[1])[6]
level_data = bytearray(level_size)
brick_color=['Red', 'Yellow', 'Blue', 'Pink', 'Green']

try:
    with open(sys.argv[1],'rb') as f:
        f.readinto(level_data)
        print("%s successfully read"%sys.argv[1])
except:
    print("Could not open level file")
    sys.exit()

for i in range(0,level_size,3):
    level_data[i] *=2
    level_data[i+1] *= 2
    print("x: %d, y: %d, color: %s"%(level_data[i],level_data[i+1],
                                     brick_color[level_data[i+2]]))
