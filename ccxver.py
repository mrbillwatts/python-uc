import paramiko
from paramiko_expect import SSHClientInteraction
import sys
import csv

def main():
    get_version()
    parse_file()

def get_version():
    success=0
    with open("host_list.csv") as file:
        readrow = csv.reader(file)
        for ip_address, uname, pw in readrow:
            session = paramiko.SSHClient()
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            session.connect(hostname=ip_address, username=uname, password=pw)
            interact = SSHClientInteraction(session, timeout=90, display=True, lines_to_check=5)
            stdoutOrigin=sys.stdout
            sys.stdout = open("Output.txt","a")
            interact.expect('admin:')
            interact.send("show status")
            interact.expect('admin:')
            interact.send("show version active")
            interact.expect('admin:')
            session.close()
            sys.stdout.close()
            sys.stdout=stdoutOrigin
            success+=1
    print(f'Retreived "show version active" from {success} servers.')
    
def parse_file():
    output_servers=0
    ver=False
    with open("Output.txt", "r") as file:
        lines = file.readlines()
    with open("Output.txt", "w") as file:
        for line in lines:
            if ver:
                if line.startswith("admin"):
                    file.write("\n")
                    ver=False
                    continue
                else: file.write(line)
            elif line.startswith("Host Name"):
                file.write(line)
                output_servers+=1
            elif line.startswith("admin:show version active"):
                ver = True
            else: continue
    print(f"Successfully parsed output from {output_servers} servers.")


if __name__ == "__main__":
    main()