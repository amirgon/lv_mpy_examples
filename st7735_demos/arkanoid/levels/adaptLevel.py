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


ascii_filename=sys.argv[1].replace('bin','asc')
print(ascii_filename)

try:
    outfile = open(ascii_filename,'w')
    print(ascii_filename + " successfully opened for writing")
except:
    print("Could not open new level file for writing")
    sys.exit()
    
for i in range(0,level_size,3):
    outstring = "%04d %04d %s\r\n"%(2*level_data[i]-8,2*level_data[i+1],
                                  brick_color[level_data[i+2]])
    print(outstring,end="")
    outfile.write(outstring)
    
print("%s successfully written"%ascii_filename)
outfile.close()

