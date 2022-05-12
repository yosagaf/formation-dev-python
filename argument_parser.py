import argparse
from ast import arg

parser = argparse.ArgumentParser(
    description="Exemple d'utilisation d'argument parser.")
parser.add_argument("-f", "--file", dest="filename", default="mon_fichier.txt")
parser.add_argument("-v", "--verbosity", action="store_true",
                    help="increase outpout verbosity")
parser.add_argument("-i", "--image", default="mon_image.jpg")


args = parser.parse_args()
print(args)
print(args.filename)
print(args.verbosity)
print(args.image)

print("Done")
