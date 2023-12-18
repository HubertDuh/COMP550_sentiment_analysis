import csv
from snownlp import SnowNLP
import sys

def convert_to_pinyin(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile, delimiter='\t')
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')

        writer.writeheader()
        for row in reader:
            try:
                text = row['text_a']
                pinyin = ' '.join(SnowNLP(text).pinyin)
                row['text_a'] = pinyin
                writer.writerow(row)
            except Exception as e:
                print(f"Error processing row: {row['text_a']}")
                print(f"Error message: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    convert_to_pinyin(input_file_path, output_file_path)
