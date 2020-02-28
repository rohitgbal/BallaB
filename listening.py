import socket, struct, textwrap, time, binascii

#Main Program    
def main():
	con=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
	while True:
		rdata,addr=con.recvfrom(65535)
		dmac, smac, pcol, edata = eth_pack(rdata)
		if pcol == 8:
			ver,header_len, ttl, ptcl, sip, dip, idata = ip_pack(edata)
			if ptcl ==  6:
				(s_port, d_port, seq, ack, u_flag,a_flag, p_flag, r_flag, s_flag, f_flag, hdata) = tcp_seg(idata)
				if d_port == 80 or s_port == 80:
					print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$IPv4 Packet$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
					print('Version {} Header Len {} TTL {}'.format(ver,header_len, ttl))
					print('Protocol {} Src IPv4 {} Dest IPv4 {}'.format(ptcl,sip, dip))
					print('$$TCP Packets$$')
					print('Dest_Port {} Src Port {}'.format(d_port,s_port))
					print('Seq No {} Ack No {}'.format(seq,ack))
					print('$$$$$$$$$$$$$$$$$')
					s=hdata.decode('utf-8')
					ws=s.split(' ',len(s))
					print(ws[0])
					print(str(ws[1:2]).replace('[','').replace(']','').replace("'",''))
#unpack Ethernet frame
def eth_pack(data):
    d_mac,s_mac,pcol=struct.unpack('! 6s 6s H',data[:14])
    return get_mac(d_mac),get_mac(s_mac),socket.htons(pcol),data[14:]

#Formatting into Standard mac address format
def get_mac(baddr):
    saddr=map('{:02x}'.format,baddr)
    maddr=':'.join(saddr).upper()
    return maddr
    
#unpack IPv4 Packet
def ip_pack(data):
    ver_header_len=data[0]
    ver=ver_header_len>>4
    header_len=(ver_header_len & 15)*4
    ttl,ptcl,sip,dip = struct.unpack('! 8x B B 2x 4s 4s',data[:20])
    return ver,header_len,ttl,ptcl,get_ip(sip), get_ip(dip), data[header_len:]

#Formatting into Standard IPv4 (Dotted Decimal) Format
def get_ip(ip):
    ipv4='.'.join(map(str,ip))
    return ipv4
    

#Unpack TCP Segments
def tcp_seg(data):
    (s_port, d_port, seq, ack, off_resv_flags ) = struct.unpack('! H H L L H', data[:14])
    offset = (off_resv_flags >> 12) * 4
    flag = (off_resv_flags & 32)
    return s_port, d_port, seq, ack, flag, data[offset:]


main()
