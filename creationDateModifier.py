import filedate
from datetime import datetime

# Function that takes date from CSV, and modifies the original file to have creation date from CSV

def creationDateModifier(originalDate, file):

  # Formats date from CSV to match fildata.File().set() syntax
  formattedDate = datetime.strptime(originalDate.replace(",", " "), '%A %B %d %Y %I:%M %p %Z').strftime('%Y.%m.%d %I:%M:00 %p GMT')

  a_file = filedate.File(file)
  a_file.set(
    created = formattedDate,
    modified = formattedDate
  )

  # after = filedate.File(file)