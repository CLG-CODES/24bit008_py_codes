#CODE 1: MAKE A CSV FILE WHICH CAN BE OPENED IN EXCEL
import csv
with open("text.csv","w") as f:
    add=csv.writer(f);
    add.writerow(["name","marks","subject"])
    add.writerow(["Parth","20","Maths"])


