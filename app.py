from calcipv4 import CalcIPv4


calc_ipv4 = CalcIPv4(ip='192.168.0.1', mascara='255.255.255.0')  # Deve ser informado o IP, e ou a Mascara ou CIDR

print(f'IP: {calc_ipv4.ip}')
print(f'Máscara da rede: {calc_ipv4.mascara}')
print(f'Ip da Rede: {calc_ipv4.rede}')
print(f'Broadcast: {calc_ipv4.brodcast}')
print(f'CIDR: {calc_ipv4.prefixo}')
print(f'Número de IPs suportados na rede: {calc_ipv4.numero_ips}')
