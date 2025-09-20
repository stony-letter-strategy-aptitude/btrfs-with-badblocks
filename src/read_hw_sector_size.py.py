from pathlib import Path
def read_sector_size(device: str) -> int:
    # Read hardware sector size directly from the sysfs file
    file_path = f"/sys/block/{device[-3:]}/queue/hw_sector_size"
    print(f"Reading {file_path}")

    hw_sector_size=int(Path(file_path).read_text().strip())
    print(f"Hardware sector size: {hw_sector_size}")
    return hw_sector_size


if __name__ == "__main__":
    read_sector_size("/dev/sda")
