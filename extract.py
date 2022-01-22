import csv
import os
import sys

SAVE_FOLDER = 'saves'
SKIP = 2
TICKER_COLUMN_INDEX = 2
BAD_FILENAMES = ('PRN', 'LPT', 'AUX', 'CON', 'NUL')

def extract(filename: str):
    with open(filename, newline='') as in_file:
        reader = csv.reader(in_file)
        headers = next(reader)        
        for row in reader:
            ticker = row[TICKER_COLUMN_INDEX]
            is_bad_name = ticker.upper() in BAD_FILENAMES
            save_filename = os.path.join(
                SAVE_FOLDER,
                f'{ticker}{"_" if is_bad_name else ""}.csv'
            )
            file_exists = os.path.isfile(save_filename)
            with open(save_filename, 'a', newline='') as out_file:
                writer = csv.writer(out_file)
                if not file_exists:
                    writer.writerow(('File name', *headers[SKIP:]))
                writer.writerow((filename, *row[SKIP:]))

if __name__ == '__main__':
    extract(sys.argv[1])