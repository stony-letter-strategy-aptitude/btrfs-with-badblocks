
A Python utility to **scan for bad blocks** and **create safe partitions** on a storage device. This tool automates low-level disk preparation, ensuring partitions are free from damaged sectors, making them suitable for subsequent Btrfs filesystem creation.

## Features

* Detects the device's **hardware sector size**.
* Scans for **bad blocks** using `badblocks`.
* Creates multiple partitions that avoid bad blocks.
* Prepares the disk for a **manual Btrfs filesystem** creation.


**⚠️ Warning:**

* This tool is **not meant for production use**.
* Running this script **will delete all data on the target disk**. Use only on non-critical drives and make backups first.

## Prerequisites

Ensure the following tools are available on your system:

* `badblocks`
* `parted`
  
These tools are typically pre-installed on most Linux distributions. If not, they can be installed via your package manager.

## Usage

**⚠️ Warning:** Running this tool **will erase all data on your disk**.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/stony-letter-strategy-aptitude/btrfs-with-badblocks.git
   cd btrfs-with-badblocks
   ```

2. **Run the script:**

   ```bash
   python src/main.py
   ```

   The script will:

   * Detect the device's hardware sector size.
   * Scan for bad blocks and save them to `badblocks.txt`.
   * Create partitions that avoid the bad blocks.

3. **Manually create a Btrfs filesystem:**

   After partitioning, you can create a Btrfs filesystem on the new partitions:

   ```bash
   sudo mkfs.btrfs -L my_btrfs /dev/sdX1 /dev/sdX2 /dev/sdX3
   ```

   Replace `/dev/sdX1`, `/dev/sdX2`, and `/dev/sdX3` with your actual partition names.

## License

This project is licensed under the **GPLv2** License. See [LICENSE](LICENSE) for details.


