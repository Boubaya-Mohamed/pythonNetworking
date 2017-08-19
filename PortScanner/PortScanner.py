import socket 
import sys ,time,os
import threading 
import ConfigParser
import signal

#import queue with six.moves.queue  because join() it's not define in Queue
from six.moves.queue import Queue #https://docs.python.org/3.4/library/queue.html#module-queue
os.system("clear")
hostsacaner = []
data = open('listhost.txt').readlines() 
for i in data:
	hostsacaner.append(str(i.replace('\n','')))
name_ports = {
	21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    194: "IRC",
    443: "HTTPS",
    3306: "MySQL",
    25565: "Minecraft"
}
def sigint_hundle(sigum ,frame):
	print '\033[91m user interrupt ! shutting down \033[0m '
	print "\033[91m [info] shutting down PortScanner \033[0m \n\n"
	sys.exit()
signal.signal(signal.SIGINT ,sigint_hundle)
def checkPort(host , port) : 
	try : 
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		s.settimeout(0.5)
		s.connect((host,port))
	except socket.error :
		return False 
	return True 
port_queue = Queue()
def scanner_worker(host):
	while True : 
		port = port_queue.get()
		if checkPort(host,port): 
			if port in name_ports : 
				print '=============== [ ' + name_ports[port] +' ]'+  " | " "\033[34m"+host +"\033[0m"+': '+format(port) +' ]' + " is open "
			else:
			    print'=============== [ '+"\033[34m"+host +"\033[0m"+': '+format(port) +' ]' + " is open "
		port_queue.task_done()
def startScanner() :
	if open('listhost.txt')== -1 :
		print 'Usage : please insert a host name a list'
		sys.exit()

	print """.__          __ /\                  __                 __                                       .__                 
|  |   _____/  |)/ ______   _______/  |______ ________/  |_    ______ ____ _____    ____   ____ |__| ____    ____   
|  | _/ __ \   __\/  ___/  /  ___/\   __\__  \\_  __ \   __\  /  ___// ___\\__  \  /    \ /    \|  |/    \  / ___\  
|  |_\  ___/|  |  \___ \   \___ \  |  |  / __ \|  | \/|  |    \___ \\  \___ / __ \|   |  \   |  \  |   |  \/ /_/  > 
|____/\___  >__| /____  > /____  > |__| (____  /__|   |__|   /____  >\___  >____  /___|  /___|  /__|___|  /\___  /  
          \/          \/       \/            \/                   \/     \/     \/     \/     \/        \//_____/   """
	for host in hostsacaner:
	

		print ' \n \n [-] ============================================================ [-]\n '
		print '              [-] we are waiting for scanning  \n \n'
		for _ in range(10):
		    t = threading.Thread(target=scanner_worker,kwargs={"host" :host})
		    t.daemon = True
		    t. start()
		    start_time = time.time() 
		for port in range (1024):
			port_queue.put(port)
		port_queue.join()
		end_time = time.time()
	print "scanning took {:5.2f} ".format(end_time - start_time) + " s"		
startScanner()
print "              Done scanning  :D  "


