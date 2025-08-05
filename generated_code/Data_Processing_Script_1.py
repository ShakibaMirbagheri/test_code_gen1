import csv
from collections import Counter
def clean_csv(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None
def main():
    filename = input("Enter the name of the CSV file to read (or 'no' to skip): ")
    if filename.lower() == "no":
        print("No CSV file found.")
        return
    cleaned_data = clean_csv(filename)
    with open('cleaned_data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in cleaned_data:
            writer.writerow([row])
if __name__ == "__main__":
    main()