import sys
import os
cwd = os.getcwd()

sys.path.append()

from generate_list import printIt

count = 0
while (count <= 1000):
    print (printIt(), count)
    count = (count + 1)
    