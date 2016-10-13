import subprocess
import socket
from timeit import default_timer as timer
import ping_with_sys

# TODO: ping 10 times and create time out based on that

start = timer()

# remote_ip = "192.168.0.114"
# remote_ip = "192.241.215.29"
remote_ip = '192.241.215.29'




max_port = 65535 #65535
port_range = [x for x in range(1, max_port + 1)]

max_timeout = ping_with_sys.get_ping(remote_ip, "max", "Windows", "5")
if max_timeout <= 0:
	print "going with default max_timeout."
	max_timeout = 10
max_timeout = max_timeout * .001 # convert to sec

print "max_timeout: {}".format(max_timeout)




i = 1
for port in port_range:
    if i % 100 == 0:
        print "Working...Checking Port:{}".format(port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(max_timeout)
    # print "Trying to connect to Host: {} on port: {}".format(remote_ip, port)
    result = sock.connect_ex((remote_ip, port))
    if result == 0:
        print "{}'s port {} is open".format(remote_ip, port)
        # sock.sendall('GET / HTTP/1.1')
        # data = sock.recv(1024)
        # print data
    sock.close()
    i += 1




end = timer()
print "Execution time: {}".format(end - start)

    # for port in range(1, 1025):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result = sock.connect_ex((remote_ip, port))
#     print result
#     if result == 0:
#         print "Port {}:\t Open".format(port)
#     sock.close()