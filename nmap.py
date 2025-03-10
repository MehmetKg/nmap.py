import nmap

scanner = nmap.PortScanner()


ip = 'target_ip_address'


scanner.scan(ip, '0-100', '-sV')


if ip in scanner.all_hosts():
    print(f"IP Adresi: {ip}")
    print(f"Durum: {scanner[ip].state()}")


    if 'tcp' in scanner[ip]:
        print("Açık TCP Portları ve Bilgileri:")

        for port in scanner[ip]['tcp'].keys():
            state = scanner[ip]['tcp'][port]['state']
            name = scanner[ip]['tcp'][port]['name']
            product = scanner[ip]['tcp'][port]['product']
            version = scanner[ip]['tcp'][port]['version']

            print(f"Port: {port} | Durum: {state} | Servis: {name} | Ürün: {product} | Versiyon: {version}")
    else:
        print("TCP bağlantısı bulunamadı.")

else:
    print("IP adresi tarama sonuçlarında bulunamadı!")
