import os
import csv
import argparse

def combine_sentences(folder):
    base_path = os.path.join('../COMP550_sentiment_project/data', 'English', 'aclImdb', folder)
    neg_path = os.path.join(base_path, 'neg')
    pos_path = os.path.join(base_path, 'pos')

    with open(f'{folder}_sentiments.tsv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['label', 'text_a'])

        for filename in os.listdir(neg_path):
            if filename.endswith('.txt'):
                with open(os.path.join(neg_path, filename), 'r', encoding='utf-8') as f:
                    sentence = f.read().strip()
                    writer.writerow([0, sentence])

        for filename in os.listdir(pos_path):
            if filename.endswith('.txt'):
                with open(os.path.join(pos_path, filename), 'r', encoding='utf-8') as f:
                    sentence = f.read().strip()
                    writer.writerow([1, sentence])

def main():
    parser = argparse.ArgumentParser(description='Combine sentiment sentences into a TSV file.')
    parser.add_argument('folder', choices=['test', 'train'], help='The folder to process (test or train)')
    args = parser.parse_args()

    combine_sentences(args.folder)

if __name__ == '__main__':
    main()
