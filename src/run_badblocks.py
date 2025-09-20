import subprocess
from pathlib import Path

OUTPUT_FILE = "badblocks.txt"


def run_badblocks(device):
    # Build the badblocks command
    cmd = ["sudo", "badblocks", "-sv", "-b", "512", "-o", OUTPUT_FILE, device]

    subprocess.run(cmd)


def read_badblocks():
    # Read the badblocks output file
    badblocks_results = tuple(map(int, Path(OUTPUT_FILE).read_text().split()))
    print("Bad blocks found:")
    print(badblocks_results)

    return badblocks_results


if __name__ == "__main__":
    run_badblocks("/dev/sda")
    read_badblocks()
