#Network_Security_Project3

## Router ID range
350 router ID - 400 router ID

## Router IDs that are removed - 
R_360, R_370, R_380, R_390

## Configuartion Instructions
1. Download the Ubuntu 20.04.4 from ubunutu.com/download/desktop 
2. Boot into ubuntu in VMware & follow Installation Instructions
3. Naviagate into mininet using the command "sudo mn"


## Installation Instructions
1. We installed VMware Virtual Machine
2. Update to the latest version with the command "sudo apt-get update" || "sudo apt-get upgrade"
3. Install mininet in ubuntu using "sudo apt-get install mininet"
4. Install python in ubuntu using "sudo apt-get install python"
5. Install python manager to install python packages in ubuntu by "sudo pip install manager" 
6. Install python pandas package by "sudo apt install python3-pandas"
7. “sudo apt-install wireshark”


## Operating Instructions
1. We import the dataset[routers_data_undirected.txt] into our code.
2. To execute our code we use the command "sudo mn --custom test.py --test=mytopo" & when we are navigate to mininet run command "pingall"
3. By using wireshark, we capture data packets of each host.
4. Later, we will be merging all individual data packet files.
5. We will clean dataset file by removing duplicates.
6. Later, we do the visualization of dataset as Project 1.


## DOS Attack
1. When DOS attack happens to the network topology, we disconnect the attached connections.


## Contact for Authors
| Name | Rid | Section |
| --- | --- | --- |
|Lohith Bhargav Doppalapudi | R11786637 |  003 |
|Deepika Duttaluru Muralidhar | R11798788 | 002 |
|Bala Naga Sai Chandu Thutupalli | R11800450 | 003 |
|Dharani Kumar Vemuri | R11804262 | 003 |
|Rajani Priya Danda | R11800015 | 003 |
|Harshini Vemula | R11800661 | 003 |

