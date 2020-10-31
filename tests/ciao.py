import sys
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file")
ap.add_argument("args", nargs="*")
ap.add_argument("further_args", nargs="*")

print(ap.parse_args())
print(sys.argv)
