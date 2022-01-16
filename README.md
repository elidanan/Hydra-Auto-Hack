# Hydra-Auto-Hack

## A python script that will use hydra to get user and password to login to ssh, ftp, and telnet

### Project Description

This python script was created to use when first entering a network to try and get user and password to login to any computer in the network with ssh, ftp, or telnet open. It can be used for pentesting and while playing CTF's. This script was created running against a docker network for testing purposes.

### ProofOfConcept

- Pull three docker ubuntu images 
- Create three docker containers running ubuntu image
- For every container install ftp, ssh, or telnet
- Change password for user to password that will be in password file you will use for hydra for each container
- For ssh you need to uncomment #PermitRootLogin yes in /etc/ssh/sshd_config file
- Check if these docker ips are coming up when running arp, if not ping the ip
- Download python script 
- Change variables in lines 19-22 in main.py for specific configuration
- Run script

### Script Description

- The script uses an important module call subprocess which lets us run command in a terminal from the script
- You can change the variables in lines 19-22 to configure how the script should run
- An arp scan is run which will take each found in the arp table, get just the ip numbers and convert from bytes to utf-8 and then add it to a new list of ips
- Using the list of ips and nmap scan is run against each ip. It takes the ouput,splits each line and looks for the word "open" in the line. If the word "open" is written in the line then it gets the service and port from that line, converts from bytes to utf-8 and creates a list of open ports, which contains ip, port, service.
- For every ip with a port open hydra is run against it using a user list and password list. It then checks if the word "host" and the ip is in the line. If it is, it               ad password from that line 



