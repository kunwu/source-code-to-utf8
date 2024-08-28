import json
import os
import argparse
from utils import process_files

def main():
    parser = argparse.ArgumentParser(description="Process some files.")
    parser.add_argument('--dryrun', action='store_true', help="Show files in hierarchical mode with encodings without changing them")
    parser.add_argument('--path', type=str, help="Specify the path to the folder to process")
    args = parser.parse_args()

    with open('config.json', 'r') as f:
        config = json.load(f)
    
    source_folder = args.path if args.path else config['source_folder']
    file_suffixes = config['file_suffixes']
    
    if not os.path.exists(source_folder):
        print(f"Source folder {source_folder} does not exist.")
        return
    
    process_files(source_folder, file_suffixes, dryrun=args.dryrun)

if __name__ == "__main__":
    main()