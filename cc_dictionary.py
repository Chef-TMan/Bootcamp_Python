inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}
total_inches = 0
for inches in inches_snow.values():
    total_inches += inches
    print("Total snowfall inches: ", total_inches)
inches_snow.update({"Thursday": 8})
user = input("How many inches of snow fell on Thursday? ")
print("Total snowfall inches: ", total_inches)
