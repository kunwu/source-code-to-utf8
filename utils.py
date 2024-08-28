import os
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def convert_to_utf8(file_path, original_encoding):
    with open(file_path, 'r', encoding=original_encoding) as f:
        content = f.read()
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def process_files(folder, suffixes, dryrun=False):
    for root, _, files in os.walk(folder):
        for file in files:
            if any(file.endswith(suffix) for suffix in suffixes):
                file_path = os.path.join(root, file)
                encoding = detect_encoding(file_path)
                if dryrun:
                    print(f"{file_path} (encoding: {encoding})")
                else:
                    if encoding.lower() != 'utf-8':
                        convert_to_utf8(file_path, encoding)
                        print(f"Converted {file_path} from {encoding} to UTF-8")