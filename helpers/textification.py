import os

def collect_configs(source_dir, output_dir, output_filename, extensions=None):
    """
    Collects all config files from a folder (recursively) into a single text file.

    :param source_dir: Path to the folder containing config files
    :param output_dir: Path to the folder where the output file will be saved
    :param output_filename: Name of the output text file
    :param extensions: List of file extensions to include (e.g. ['.cfg', '.txt'])
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, "w", encoding="utf-8") as outfile:
        for root, _, files in os.walk(source_dir):
            for file in files:
                if extensions is None or any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)

                    # Separator with filename
                    outfile.write("\n" + "="*2 + "\n")
                    outfile.write(f"File: {file}\n")
                    outfile.write("="*2 + "\n\n")

                    try:
                        with open(file_path, "r", encoding="utf-8") as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        outfile.write(f"[Error reading file: {e}]\n")

    print(f"Collected configs saved in: {output_path}")


if __name__ == "__main__":
    # 🔧 Change these variables as needed
    SOURCE_DIR = r"D:\Education\UPB\Courses\APLICACIONES CON REDES\TP\pf\gns3\confs"
    OUTPUT_DIR = r"D:\Education\UPB\Courses\APLICACIONES CON REDES\TP\pf"  # Where you want the text file to be saved
    OUTPUT_FILE = "all_gns3_configs.txt"
    EXTENSIONS = [".cfg", ".txt", ".conf"]  # Allowed file types

    collect_configs(SOURCE_DIR, OUTPUT_DIR, OUTPUT_FILE, EXTENSIONS)
