import argparse
from tqdm import tqdm
from pathlib import Path
from markitdown import MarkItDown


def convert_file_to_md(file_path: Path, delete_source: bool = False):
    """Convert one file to markdown next to the source file."""
    if file_path.name.startswith('.') or file_path.suffix.lower() == '.md':
        print(f"Skipping conversion of {file_path.name}")
        return

    md = MarkItDown(enable_plugins=False)
    output_path = file_path.with_suffix(".md")
    result = md.convert(str(file_path))
    output_path.write_text(result.text_content, encoding="utf-8")
    if delete_source:
        file_path.unlink()
    print(f"Converted: {file_path.name} -> {output_path.name}")


def convert_directory_to_md(input_dir: Path, delete_source: bool = False):
    """
    Converts all files in a dictory to a Markdown format. Original files in the folder will be deleted.
    :param input_dir: str
        The Path object pointing to the directory to process.
    :param delete_source: bool = False
        Whether to delete the original source files. Defaults to False.
    """

    # get list of files to convert
    files_to_process = [f for f in input_dir.rglob('*') if f.is_file()]

    if not files_to_process:
        print(f"No files found in {input_dir}!")
        return

    for file_path in tqdm(files_to_process, desc="Converting Files"):
        # skip hidden files and existing markdown files
        if file_path.name.startswith('.') or file_path.suffix.lower() == '.md':
            print(f"Skipping conversion of {file_path.name}")
            continue

        try:
            convert_file_to_md(file_path, delete_source)
        except Exception as e:
            tqdm.write(f"FAILED: Could not convert '{file_path.name}'. Reason: {e}")


def main(args):
    # set Paths
    source_arg = args.path or args.input_dir
    if not source_arg:
        raise ValueError("请提供要转换的文件或目录路径")

    input_path = Path(source_arg).resolve()
    print("-" * 40)
    print(f"Input Path: {input_path}")
    print("-" * 40)

    # execute
    try:
        if input_path.is_file():
            convert_file_to_md(input_path, args.delete_source)
        else:
            convert_directory_to_md(input_path, args.delete_source)
        print("\nConversion process complete.")
    except FileNotFoundError:
        print(f"\nError: Input directory not found at {input_path}")
    except Exception as e:
        print(f"\nAn unexpected error occurred during execution: {e}")


if __name__ == "__main__":
    """Command-line arguments."""
    parser = argparse.ArgumentParser(description="Convert one file or all files in a directory to Markdown.")
    parser.add_argument(
        "path",
        nargs="?",
        help="The file or directory to convert."
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        default=None,
        help="The path to the directory containing files to convert."
    )
    parser.add_argument(
        "--delete_source",
        action="store_true",
        help="Whether to delete the original source files."
    )
    args = parser.parse_args()

    main(args)
