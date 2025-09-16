from faker import Faker
import csv
fake = Faker()

with open("esers.cvs", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email", "Job"])
    for i in range(10):
        writer.writerow([fake.name(), fake.email(), fake.job()])