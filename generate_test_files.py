import os
import shutil
import argparse

def create_test_files(base_path):
    os.makedirs(base_path, exist_ok=True)
    subfolders = ['subfolder1', 'subfolder2']
    utf8_content = "这是一个UTF-8编码的文件。"
    gb2312_content = "这是一个GB2312编码的文件。".encode('gb2312')

    for subfolder in subfolders:
        folder_path = os.path.join(base_path, subfolder)
        os.makedirs(folder_path, exist_ok=True)
        
        # Create UTF-8 files
        for i in range(2):
            file_path = os.path.join(folder_path, f"utf8_file_{i}.txt")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(utf8_content)
        
        # Create GB2312 files
        for i in range(2):
            file_path = os.path.join(folder_path, f"gb2312_file_{i}.txt")
            with open(file_path, 'wb') as f:
                f.write(gb2312_content)

    # Create files in the base test folder
    for i in range(2):
        file_path = os.path.join(base_path, f"utf8_file_{i}.txt")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(utf8_content)
    
    for i in range(2):
        file_path = os.path.join(base_path, f"gb2312_file_{i}.txt")
        with open(file_path, 'wb') as f:
            f.write(gb2312_content)

def print_hierarchy(base_path):
    for root, dirs, files in os.walk(base_path):
        level = root.replace(base_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

def purge_folder(base_path):
    if os.path.exists(base_path):
        shutil.rmtree(base_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate test files.")
    parser.add_argument('--purge', action='store_true', help="Purge the test folder before generating files")
    args = parser.parse_args()

    if args.purge:
        purge_folder('test')
    
    create_test_files('test')
    print("Generated test files in hierarchical mode:")
    print_hierarchy('test')