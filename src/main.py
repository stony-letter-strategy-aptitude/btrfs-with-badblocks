from create_partition import create_many_partitions
from run_badblocks import run_badblocks


def main():
    device = input("Enter device like /dev/sda:").strip()

    run_badblocks(device)

    create_many_partitions(device)


if __name__ == "__main__":
    main()
