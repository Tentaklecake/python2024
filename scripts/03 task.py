ip_mask = '192.168.43.54 / 255.255.254.0'
slash = ip_mask.find('/')
ip = ip_mask[:slash-1]
mask = ip_mask[slash+2:]
sep_ip = ip.split('.')
sep_mask = mask.split('.')

#network
a = int(sep_ip[0]) & int(sep_mask[0])
b = int(sep_ip[1]) & int(sep_mask[1])
c = int(sep_ip[2]) & int(sep_mask[2])
d = int(sep_ip[3]) & int(sep_mask[3])

#wildcard
wild_fi_octet = 255 - int(sep_mask[0])
wild_se_octet = 255 - int(sep_mask[1])
wild_th_octet = 255 - int(sep_mask[2])
wild_fo_octet = 255 - int(sep_mask[3])

#broadcast
broad_fi_octet = a + wild_fi_octet
broad_se_octet = b + wild_se_octet
broad_th_octet = c + wild_th_octet
broad_fo_octet = d + wild_fo_octet

#min_host
min_host = d + 1

#max_host
max_host = broad_fo_octet - 1

print (str(a) + '.' +str(b) + '.' + str(c) + '.' + str(d))
print (str(wild_fi_octet)+ '.' +str(wild_se_octet) + '.' + str(wild_th_octet) + '.' + str(wild_fo_octet))
print (str(broad_fi_octet) + '.' +str(broad_se_octet) + '.' + str(broad_th_octet) + '.' + str(broad_fo_octet))
print (str(a) + '.' +str(b) + '.' + str(c) + '.' + str(min_host))
print (str(broad_fi_octet) + '.' +str(broad_se_octet) + '.' + str(broad_th_octet) + '.' + str(max_host))