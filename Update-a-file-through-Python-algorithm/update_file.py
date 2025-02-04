import_file = "allow_list.txt"

remove_list = ["192.168.128.44", "192.168.16.87", "192.168.188.75", "192.168.5.36"]

def update_file(import_file, remove_list):
    
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    ip_addresses = ip_addresses.split()
    
    for ip in remove_list:
        if ip in ip_addresses:
            ip_addresses.remove(ip)

    ip_addresses = "\n".join(ip_addresses)

    with open("updated_allow_list.txt", "w") as file:
        file.write(ip_addresses)
    
update_file(import_file, remove_list)