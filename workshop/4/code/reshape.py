import csv

with open("../../assets/data/soars_demo_trap_data.csv") as fi, \
     open("../data/soars_demo_trap_data_reshaped.csv", "w") as fo:
    csv_in  = csv.DictReader(fi)

    csv_out_fieldnames = list(csv_in.fieldnames)
    csv_out_fieldnames.remove('date')
    csv_out_fieldnames.extend(['month', 'day', 'year'])

    csv_out = csv.DictWriter(fo, csv_out_fieldnames, lineterminator='\n')
    csv_out.writeheader()

    for l in csv_in:
        old_date = l['date'].split()[0]
        l['month'], l['day'], l['year'] = old_date.split('/')
        del l['date']
        csv_out.writerow(l)

