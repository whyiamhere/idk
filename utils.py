#!/usr/bin/env python3
# Description: Common helper functions

import hashlib
import pathlib
import shutil
import subprocess


def create_gitignore(folder):
    """
    Create a gitignore that ignores all files in a folder. Some folders are not
    known until the script is run so they can't be added to the root .gitignore
    :param folder: Folder to create the gitignore in
    """
    with folder.joinpath(".gitignore").open("w") as gitignore:
        gitignore.write("*")


def fetch_binutils(folder, update=True, shallow=False):
    """
    Clones/updates the binutils repo
    :param folder: Directory to download binutils to
    """
    binutils_folder = folder.joinpath("binutils")
    if binutils_folder.is_dir():
        if update:
            print_header("Updating binutils")
            subprocess.run(
                ["git", "-C",
                 binutils_folder.as_posix(), "pull", "--rebase"],
                check=True)
    else:
        extra_args = ("--depth", "1") if shallow else ()
        print_header("Downloading binutils")
        subprocess.run([
            "git", "clone", *extra_args, "git://sourceware.org/git/binutils-gdb.git",
            binutils_folder.as_posix()
        ],
                       check=True)

def print_header(string):
    """
    Prints a fancy header
    :param string: String to print inside the header
    """
    # Use bold red for the header
    print("\033[01;31m")
    for x in range(0, len(string) + 6):
        print("=", end="")
    print("\n== %s ==" % string)
    for x in range(0, len(string) + 6):
        print("=", end="")
    # \033[0m resets the color back to the user's default
    print("\n\033[0m")
