#!/opt/bin/lv_micropython
import sys

if len(sys.argv) < 2:
    print("Usage: %s level filename"%sys.argv[0])
    sys.exit()

brick_color=['Red', 'Yellow', 'Blue', 'Pink', 'Green']

try:
    f = open(sys.argv[1],'r')
    print("%s successfully read"%sys.argv[1])
except:
    print("Could not open level file")
    sys.exit()

lines = f.readlines()

for i in range(len(lines)):
    line = lines[i].split()
    for i in range(len(brick_color)):
        if line[2] == brick_color[i]:
            break
    print("x: %d, y: %d, color_index: %d"%(int(line[0]),int(line[1]),i))

f.close()
