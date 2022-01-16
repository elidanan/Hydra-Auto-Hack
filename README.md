# Hydra-Auto-Hack

## A python script that will use hydra to auto login to ssh, ftp, and telnet

### Description

This python script was created to use when first entering a network to try and login to any computer in the network with ssh, ftp, or telnet open. It can be used for pentesting and while playing CTF's. This script was created running against a docker network for testing.

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



