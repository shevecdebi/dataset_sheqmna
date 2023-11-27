import os
import csv

def create_csv(folder_path='ALL', csv_filename='metadata.csv', threshold_index=1010):
    # Get a list of all files in the folder and sort them naturally
    files = sorted(os.listdir(folder_path), key=lambda x: int(x.split('.')[0]))

    # csv ფაილის გახსნა ჩასაწერად
    with open(csv_filename, 'w', newline='') as csvfile:
        # CSV writer ის შექმნა
        csv_writer = csv.writer(csvfile)

        # თავსართები
        csv_writer.writerow(['ImageName', 'Label'])

        # ყველა ფაილზე ჩამოვლა
        for i, filename in enumerate(files, start=0):
            # Determine the label based on the threshold index
            label = 0 if i <= threshold_index else 1

            # სტრიქონის შევსება
            csv_writer.writerow([filename, label])

    print(f"CSV file '{csv_filename}' შეიქმნა წარმატებით.")

create_csv()
