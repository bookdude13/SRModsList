import argparse
import json
import os
from pathlib import Path
from zipfile import ZipFile

# Assuming that the mod zip file has everything within the Mods/ subdirectory
# (So xyz.zip/Mods/something.dll )
# Then this script can turn that extracted zip file into a synthmod file
# TODO maybe just take a zip and add in the localitem.json, call it good? No, needs dependency info.
# TODO How does this work with the sound mod?
# TODO maybe just use these easy scripts for mine, then custom scripts for automating the rest, and
# then each mod has its own script to use within its Downloads folder?

def create_archive(mod_name, version_str):
    mod_name = str(mod_name)
    version_str = str(version_str)
    print(f"{mod_name} version {version_str}")

    print("Creating LocalItem.json")    
    local_item_contents = {
        "hash": mod_name
    }
    local_item_json = json.dumps(local_item_contents, indent=2)
    local_item_path = Path("LocalItem.json")
    with open(local_item_path, "w") as local_item_file:
        local_item_file.write(local_item_json)
    
    print("Setting up output dir")
    root_output_dir = Path("..", "Downloads")
    output_dir = Path(root_output_dir, mod_name)
    output_dir.mkdir(parents=True, exist_ok=True)

    mods_dir = Path("Mods")

    output_name_zip = f"{mod_name}_{version_str}.zip"
    output_path = Path(output_dir, output_name_zip)
    print(f"Creating zip file {output_path}")
    with ZipFile(output_path, "w") as zip_file:
        zip_file.write(local_item_path)

        # Add everything in the mods dir
        for folder_name, sub_folders, file_names in os.walk(mods_dir):
            for filename in file_names:
                file_path = Path(folder_name, filename)
                zip_file.write(file_path, folder_name)

    if output_path.exists():
        print(f"Zip file created at {output_path}")
    else:
        print(f"Failed to create zip file {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='synthmod_util',
        description='Helper functions for building synthmod files')
    parser.add_argument(
        "-v",
        "--version",
        required=True,
        help="Mod version being built"
    )
    parser.add_argument(
        "-n",
        "--name",
        required=True,
        help="Mod name"
    )
    args = parser.parse_args()

    create_archive(args.name, args.version)
