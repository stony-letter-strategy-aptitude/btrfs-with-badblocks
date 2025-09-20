import math
import subprocess
from collections.abc import Iterable
from pathlib import Path

from run_badblocks import read_badblocks


def get_max_sector(device: str) -> int:
    max_sector = Path(f"/sys/block/{device[-3:]}/size").read_text()
    return int(max_sector) - 1


def create_partition(device, start_sector, end_sector):
    cmd = (
        "sudo",
        "parted",
        "-s",
        device,
        "unit",
        "s",
        "mkpart",
        "primary",
        f"{start_sector}s",
        f"{end_sector}s",
    )

    input(f"Running: {' '.join(cmd)}. Enter to do.")
    subprocess.run(cmd)

    print("The current partition")
    subprocess.run(["sudo", "parted", "-s", device, "print"])


def excluded_ranges(excluded_sectors: Iterable[int], maximum_value: int):
    MINIMUM_VALUE = 2048
    excluded_sectors = sorted(excluded_sectors)  # ensure sorted and unique
    allowed_ranges = []
    current_start = MINIMUM_VALUE
    alignment = 2048

    for excluded_sector in excluded_sectors:
        if excluded_sector < MINIMUM_VALUE:
            continue  # skip excluded numbers below the minimum

        if current_start < excluded_sector:  # only if there's a gap
            start = math.ceil(current_start / alignment) * alignment
            end = math.floor((excluded_sector - 1) / alignment) * alignment
            if start < end:
                allowed_ranges.append((start, end))
        current_start = excluded_sector + 1  # skip the excluded number

    if current_start <= maximum_value:  # handle the last range up to max
        allowed_ranges.append((current_start, maximum_value - 1000))

    return allowed_ranges


def create_many_partitions(device: str):
    badblocks = read_badblocks()
    if not badblocks:
        print("There is no error.")
        return

    max_sector = get_max_sector(device)
    sector_ranges = excluded_ranges(badblocks, max_sector)
    for start_sector, end_sector in sector_ranges:
        create_partition(device, start_sector, end_sector)


if __name__ == "__main__":
    create_many_partitions("/dev/sda")
