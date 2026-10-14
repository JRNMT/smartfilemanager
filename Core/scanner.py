from pathlib import Path

def scan_folder(folder_path):

    map_pad = Path(folder_path)
    for file in map_pad.rglob('*'):
        if file.is_file():
            filename = file.name
            filestem = file.stem
            fileextention = file.suffix
            filesize = file.stat().st_size
            