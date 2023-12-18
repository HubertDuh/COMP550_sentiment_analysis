import argparse
import jsonlines

def jsonl_to_tsv(input_file, output_file):
    with jsonlines.open(input_file, 'r') as reader, open(output_file, 'w', encoding='utf-8') as writer:
        writer.write("label\ttext_a\n")
        for line in reader:
            label = line.get("polarity", "")
            review = line.get("review", "")
            writer.write(f"{label}\t{review}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSONL file to TSV format.")
    parser.add_argument("input_file", help="Input JSONL file path")
    parser.add_argument("output_file", help="Output TSV file path")
    args = parser.parse_args()

    jsonl_to_tsv(args.input_file, args.output_file)
