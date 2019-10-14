#AIO-AL
ver='1.2.1'
#github.com/smcclennon/AIO-AL


#m1: import
print("Importing required libraries...")
import time
globalstart=time.time(); importstart=time.time()
try:
    import os,datetime,socket,urllib.request,sys,platform,json
except:
    print('\nError: unable to import one or more libraries\nVisit: github.com/smcclennon/AIO-AL for support\n\nPress enter to exit...')
    input()
    exit()
try:
    import psutil
except:
    print('\nError: unable to import "psutil"')
    confirm=input(str('Attempt to install "psutil"? [Y/n] ')).upper()
    if confirm=='Y':
        try:
            os.system('pip install psutil --user')
            os.system('cls')
            os.system('"'+str(os.path.basename(__file__))+'"')
            exit()
        except:
            print('Failed to install "psutil"\nPress enter to exit...')
        input()
        exit()
    exit()
importend=time.time()
importduration=importend-importstart
print("Import completed in "+str(round(importduration, 2))+" seconds")



#m2: rules
def cmd(cmd):
    os.system(cmd)
def cls():
    cmd('cls')
def colour(var):
    cmd('color '+str(var))
def wtitle(var):
    cmd('title '+str(var))
appid='A I O - A L'
appname=appid+"  v"+ver
wtitle(appname+" - Checking for updates...")
colour('3f')

#update
try: #remove previous version if just updated
    with open('AIOAL.tmp', 'r') as content_file:
        os.remove(str(content_file.read()))
    os.remove('AIOAL.tmp')
except:
    pass
try: #Get latest version number (2.0.0)
    with urllib.request.urlopen("https://api.github.com/repos/smcclennon/AIO-AL/releases/latest") as url:
        data = json.loads(url.read().decode())
        latest=data['tag_name'][1:]
        patchNotes=data['body']
except:
    latest='0'
if latest>ver:
    wtitle(appname+" - Update available!")
    print('\nUpdate available!')
    print('Latest Version: v'+latest)
    print('\n'+str(patchNotes)+'\n')
    confirm=input(str('Update now? [Y/n] ')).upper()
    if confirm=='Y':
        latestFilename='AIOAL v'+str(latest)+'.py'
        wtitle(appname+" - Downloading updates...")
        print('Downloading '+latestFilename+'...') #Download latest version to cwd
        urllib.request.urlretrieve('https://github.com/smcclennon/AIO-AL/releases/latest/download/AIOAL.py', latestFilename)
        f=open('AIOAL.tmp', 'w') #write the current filename to AIOAL.tmp
        f.write(str(os.path.basename(__file__)))
        f.close()
        os.system('cls')
        os.system('"'+latestFilename+'"') #open latest version
        exit()


#m3/mm1: sysinfo
wtitle(appname+" - Performing System Info Scan...")
print("\nPerforming System Info Scan...")
sysinfostart=time.time()
print("[Preparing to log]")
sysinfo='System Info Logs'
sysinfodir=sysinfo+'\\'
hostname=str(socket.gethostname())
if not os.path.exists(sysinfo):
    os.makedirs(sysinfo)
print("[Logging: Summary]")
file=open(sysinfodir+hostname+".log","w")
file.write("=Log Generated By ["+appname+"]=\n")
file.write(datetime.datetime.now().strftime("[%d/%m/%Y] - [%H:%M:%S]"))
file.write("\n\n===Summary===")
file.write("\nName: "+socket.gethostname())
file.write("\nFQDN: "+socket.getfqdn())
file.write("\nSystem Platform: "+sys.platform)
file.write("\nMachine: "+platform.machine())
file.write("\nNode: "+platform.node())
file.write("\nPlatform: "+platform.platform())
file.write("\nProcessor: "+platform.processor())
file.write("\nSystem OS: "+platform.system())
file.write("\nRelease: "+platform.release())
file.write("\nVersion: "+platform.version())
file.write("\nNumber of CPUs: "+str(psutil.cpu_count()))
file.write("\nNumber of Physical CPUs: "+str(psutil.cpu_count(logical=False)))
file.write("\n\n===OS Generated Info===")
file.close()
print("[Logging: OS Generated Info]")
cmd('systeminfo >"'+sysinfodir+hostname+'.log.tmp"')
open(sysinfodir+hostname+".log", "a").writelines(open(sysinfodir+hostname+".log.tmp").readlines())
os.remove(sysinfodir+hostname+".log.tmp")
sysinfoend=time.time()
sysinfoduration=sysinfoend-sysinfostart
file=open(sysinfodir+hostname+".log","a")
file.write("\n\n===================\nLog completed in "+str(round(sysinfoduration, 2))+" seconds")
file.close()
print("Log completed in "+str(round(sysinfoduration, 2))+" seconds")


#m4/mm2: nmap
wtitle(appname+" - Performing Network Scan...")
print("\nPerforming Network Scan...")
netmapstart=time.time()
print("[Preparing to log]")
netmap='Network Logs'
netmapdir=netmap+'\\'
netip=socket.gethostbyname(socket.gethostname())
try:
    pubip=urllib.request.urlopen('https://ident.me').read().decode('utf8')
    internet=1
except:
    print('[Error: No internet connection - Results will be limited]')
    pubip='[Error: No internet connection]'
    internet=0
if not os.path.exists(netmap):
    os.makedirs(netmap)
filename=str(hostname+" ["+netip+"]")
print("[Logging: Summary]")
file=open(netmapdir+filename+".log","w")
file.write("=Log Generated By ["+appname+"]=\n")
file.write(datetime.datetime.now().strftime("[%d/%m/%Y] - [%H:%M:%S]"))
file.write('\n\nError: No internet connection\nResults will be limited')
file.write("\n\n===Summary===")
file.write("\nHost Name: "+hostname)
file.write("\nNetwork IP: "+netip)
file.write("\nPublic IP: "+pubip)
file.write("\n\n===Windows IP Configuration===")
file.close()
file=open(netmapdir+filename+".log","a")
print("[Logging: Windows IP Configuration]")
cmd('ipconfig /all >"'+netmapdir+filename+'.log.tmp"')
file.writelines(open(netmapdir+filename+".log.tmp").readlines())
os.remove(netmapdir+filename+".log.tmp")
file.write("\n\n==Protocol statistics and current TCP/IP network connections==")
file.flush()
print("[Logging: Protocol statistics and current TCP/IP network connections]")
cmd('netstat >"'+netmapdir+filename+'.log.tmp"')
file.writelines(open(netmapdir+filename+".log.tmp").readlines())
os.remove(netmapdir+filename+".log.tmp")
file.write("\n\n==Routing Table==")
file.flush()
print("[Logging: Routing Table]")
cmd('netstat -r >"'+netmapdir+filename+'.log.tmp"')
file.writelines(open(netmapdir+filename+".log.tmp").readlines())
os.remove(netmapdir+filename+".log.tmp")
file.write("\n\n==IP-to-Physical address translation tables used by address resolution protocol (ARP)==")
file.flush()
print("[Logging: IP-to-Physical address translation tables used by address resolution protocol (ARP)]")
cmd('arp -a >"'+netmapdir+filename+'.log.tmp"')
file.writelines(open(netmapdir+filename+".log.tmp").readlines())
os.remove(netmapdir+filename+".log.tmp")
netmapend=time.time()
netmapduration=netmapend-netmapstart
file=open(netmapdir+filename+".log","a")
file.write("\n\n===================\nLog completed in "+str(round(netmapduration, 2))+" seconds")
file.close()
print("Log completed in "+str(round(netmapduration, 2))+" seconds")


#m5: stats
globalend=time.time()
globalduration=globalend-globalstart
wtitle(appname+" - Complete!")
print("\n\nAll AIO-AL Logging Jobs Completed In "+str(round(globalduration, 2))+" seconds")
cmd('timeout 5')
