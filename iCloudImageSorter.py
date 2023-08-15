import os
import csv
from creationDateModifier import creationDateModifier 

os.system("cls")
os.system("clear")

print(f"""\033[95m\033[1m{"iCloud Image Sorter".upper()}\033[0m\033[0m\n
This program is used to extract data from iCloud photos, and format it to be able to be pushed to Google Drive.
""")

directory = input(f"{'Enter Root Directory':30} : ")

if directory[-1] == "/" or "\\":
  directory = directory[:-1]

destination = input(f"{'Enter Destination Directory':30} : ")


with open(f"{directory}/Photos/Photo Details.csv", "r") as csv_file:
  csv_reader = csv.reader(csv_file)

  next(csv_reader)

  print("\n")
  x = 0
  for line in csv_reader: 
    if not os.path.isdir(f"{destination}"):
      os.mkdir(f"{destination}")
      
    if (line[3] == "yes") and (os.path.isfile(f"{directory}/Photos/{line[0]}")):
      os.replace(f"{directory}/Photos/{line[0]}", f"{destination}/{line[0]}")
      creationDateModifier(line[5], f"{destination}/{line[0]}")
      print(f"\033[92m{line[0].split('.')[0]:25}.{line[0].split('.')[1]:5}\033[0m was exported")
      x += 1
    
  print(f"\n{'Totel Files Exported':30} : {x}\n")

