cat /sys/block/sdb/queue/hw_sector_size
sudo badblocks -sv -b 512 -o badblocks.txt /dev/sdX
sudo parted /dev/sdX
(parted) unit s                   # sectors
(parted) mkpart primary 2048s 40959s   # raw partition with no filesystem type
(parted) print
(parted) quit
ls /dev/sdX* #Shows device nodes, e.g. /dev/sda1, /dev/sda2.
sudo mkfs.btrfs -L my_btrfs /dev/sdX1 /dev/sdX2 /dev/sdX3