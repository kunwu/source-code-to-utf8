# Source Code Encoding Converter

This project is a Python script that recursively traverses a specified folder, detects the encoding of source code files, and converts them to UTF-8 if they are not already in that encoding. The script uses a configuration file for runtime settings and supports various command-line arguments.

## Project Structure

```
my_python_project/
├── main.py
├── config.json
├── utils.py
└── generate_test_files.py
```

## Configuration File

The `config.json` file contains the configuration for the script:

```json
{
    "source_folder": "test",
    "file_suffixes": [".c", ".cpp", ".h", ".hpp"]
}
```

- `source_folder`: The folder to be processed.
- `file_suffixes`: The list of file suffixes to be considered as source code files.

## Usage

### Running the Script

To run the script, use the following command:

```sh
python main.py
```

### Command-Line Arguments

- `--dryrun`: Show files in hierarchical mode with encodings without changing them.
- `--path`: Specify the path to the folder to process.

#### Examples

- Run the script with the default configuration:

    ```sh
    python main.py
    ```

- Run the script with a custom path:

    ```sh
    python main.py --path /custom/path
    ```

- Run the script in dry-run mode:

    ```sh
    python main.py --dryrun
    ```

- Display the help message:

    ```sh
    python main.py --help
    ```

## Generating Test Files

The `generate_test_files.py` script can be used to generate test files for the project. It creates a two-level recursive sub-folder structure under the `test` folder, with two UTF-8 files and two non-UTF-8 files (GB2312 encoded) in each folder.

### Command-Line Arguments

- `--purge`: Purge the test folder before generating files.

#### Examples

- Generate test files:

    ```sh
    python generate_test_files.py
    ```

- Purge the test folder before generating files:

    ```sh
    python generate_test_files.py --purge
    ```

## License

This project is licensed under the GPL License.
