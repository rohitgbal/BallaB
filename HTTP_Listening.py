import socket, struct, textwrap, time, binascii, mysql.connector
#Main Program    
def main():
	con=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
	while True:
		rdata,addr=con.recvfrom(65535)
		dmac, smac, pcol, edata = eth_pack(rdata)
		if pcol == 8:
			ver, header_len, t_len, flw, ttl, ptcl, sip, dip, idata = ip_pack(edata)
			if ptcl ==  6633:
				s_port, d_port, seq, ack, offset, flag, hdata = tcp_seg(idata)
				print('\n ##############################START########################')
				print('Dest Mac : {} *** Src Mac : {} *** Prot {}'.format(dmac,smac,pcol))
				print('Dest IP : {} *** Src IP : {} *** Ptcl : {}'.format(sip,dip,ptcl))
				print('Dest Port : {} *** Src Port : {} *** Seq : {}*** Acq : {}'.format(s_port,d_port,seq,ack))
				
				#if d_port == 6633:
					#http_req(hdata)
				#if s_port == 6633:
					#http_res(hdata)

#					try:
#						db=mysql.connector.connect(host="localhost",user="root",passwd="RohitGBal@99",database="packets")
#						cursor=db.cursor()
#						sql="""INSERT INTO packet1 (hlen,ttl,sip,dip,ptcl,sport,dport,seq,ack,method,link) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#						val=(header_len,ttl,sip,dip,ptcl,s_port,d_port,seq,ack,method,link)
#						cursor.execute(sql,val)
#						db.commit();
#					except mysql.connector.Error as error:
#						db.rollback()
#						print("Failed {}".format(error))
					
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
    t_len, flw, ttl, ptcl,sip,dip = struct.unpack('! 3x H H x B B 2x 4s 4s',data[:20])
    return ver, header_len, t_len, flw, ttl, ptcl, get_ip(sip), get_ip(dip), data[header_len:]

#Formatting into Standard IPv4 (Dotted Decimal) Format
def get_ip(ip):
    ipv4='.'.join(map(str,ip))
    return ipv4
    

#Unpack TCP Segments
def tcp_seg(data):
    (s_port, d_port, seq, ack, off_resv_flags ) = struct.unpack('! H H L L H', data[:14])
    offset = (off_resv_flags >> 12) * 4
    flag = (off_resv_flags & 32)
    return s_port, d_port, seq, ack, offset,flag, data[offset:]

def http_req(data):
	try:
		s=data.decode("utf-8")
		ws=s.split(' ',len(s))
		print(ws)
	except UnicodeDecodeError:
		pass
	
def http_res(data):
	try:
		s=data.decode("utf-8")
		ws=s.split(' ',len(s))
		print (ws)
	except UnicodeDecodeError:
		pass

main()