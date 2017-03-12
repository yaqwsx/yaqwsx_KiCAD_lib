import sys
import re

scale = float(sys.argv[1])

def transform(arg):
    parts = arg.group().replace(")", "").split()
    return "(xy {} {})".format(scale * float(parts[1]), scale * float(parts[2]))

with open(sys.argv[2], 'r') as infile, open(sys.argv[3], 'w') as outfile:
    for line in infile:
        line = re.sub(r'\(\s*xy\s*(-?\d*\.?\d*(e-?\d*)?)\s*(-?\d*\.?\d*(e-?\d*)?)\s*\)', transform, line)
        outfile.write(line)

