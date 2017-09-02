import fnmatch
import os

images = ['*.jpg', '*.jpeg', '*.log', '*.tif', '*.dat']
matches = []

for root, dirnames, filenames in os.walk("R:\\"):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))
            print("root=", root, "  dirname=", dirnames, "  filename=", filename)