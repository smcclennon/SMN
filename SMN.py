#SMN
ver='2.2.0'
proj='SMN'
#github.com/smcclennon/SMN

online = False



# -==========[ Update code ]==========-
# Updater: Used to check for new releases on GitHub
# github.com/smcclennon/Updater
import os  # detecting OS type (nt, posix, java), clearing console window, restart the script
from distutils.version import LooseVersion as semver  # as semver for readability
import urllib.request, json  # load and parse the GitHub API
import platform  # Consistantly detect MacOS

# Disable SSL certificate verification for MacOS (very bad practice, I know)
# https://stackoverflow.com/a/55320961
if platform.system() == 'Darwin':  # If MacOS
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

if os.name == 'nt':
    import ctypes  # set Windows console window title
    ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Checking for updates...')

updateAttempt = 0  # Keep track of failed attempts
print('Checking for updates...', end='\r')
while updateAttempt < 3:  # Try to retry the update up to 3 times if an error occurs
    updateAttempt = updateAttempt+1
    try:
        with urllib.request.urlopen("https://smcclennon.github.io/update/api/2") as internalAPI:
            online = True
            repo = []
            for line in internalAPI.readlines():
                repo.append(line.decode().strip())
            apiLatest = repo[0]  # Latest release details
            proj = repo[1]  # Project name
            ddl = repo[2]  # Direct download link
            apiReleases = repo[3]  # List of patch notes
        with urllib.request.urlopen(apiLatest) as githubAPILatest:
            data = json.loads(githubAPILatest.read().decode())
            latest = data['tag_name'][1:]  # remove 'v' from version number (v1.2.3 -> 1.2.3)
        del data  # Prevent overlapping variable data
        release = json.loads(urllib.request.urlopen(  # Get latest patch notes
            apiReleases).read().decode())
        releases = [  # Store latest patch notes in a list
            (data['tag_name'], data['body'])
            for data in release
            if semver(data['tag_name'][1:]) > semver(ver)]
        updateAttempt = 3
    except:  # If updating fails 3 times
        latest = '0'
if semver(latest) > semver(ver):
    if os.name == 'nt': ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Update available: {ver} -> {latest}')
    print('Update available!      ')
    print(f'Latest Version: v{latest}\n')
    for release in releases:
        print(f'{release[0]}:\n{release[1]}\n')
    confirm = input(str('Update now? [Y/n] ')).upper()
    if confirm != 'N':
        if os.name == 'nt': ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Installing updates...')
        print(f'Downloading {proj} v{latest}...')
        urllib.request.urlretrieve(ddl, os.path.basename(__file__))  # download the latest version to cwd
        import sys; sys.stdout.flush()  # flush any prints still in the buffer
        os.system('cls||clear')  # Clear console window
        os.system(f'"{__file__}"' if os.name == 'nt' else f'python3 "{__file__}"')
        import time; time.sleep(0.2)
        quit()
if os.name == 'nt': ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==')
# -==========[ Update code ]==========-


import os
if os.name != 'nt':
    print(f'{proj} currently only supports Windows, and we have no plans to expand support to Unix any time soon\ndue to our reliance on Windows-specific commands and features')
    print('\nHowever, this script will continue to recieve updates,\nincluding the possibility for Unix support in the future :)')
    print(f'\nhttps://github.com/smcclennon/{proj}')
    print('\nPress enter to exit')
    input()
    quit()




#m1: import
print("Importing required libraries...")
import time
importstart=time.time()
try:
    import os, datetime, socket, sys, platform
except:
    print('\nError: unable to import one or more libraries\nVisit: github.com/smcclennon/SMN for support\n\nPress enter to exit...')
    input()
    exit()
try:
    import psutil
except:
    print('\nError: unable to import "psutil"')
    confirm=input(str('Attempt to install "psutil"? [Y/n] ')).upper()
    if confirm!='N':
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
appid='Scan Me Now'
appname=appid+"  v"+ver
def appjob(job):
    if online:
        wtitle(appname+' [Online] - '+str(job))
    else:
        wtitle(appname+' [Offline] - '+str(job))


#configure scan
appjob("Choose scan type")
print('\nS: Full System Scan\nN: Full Network Scan\nP: System & Network Scan (without current TCP/IP network connections)\nA: Full System & Network Scan')
logtype=input(str('What would you like to log? [S/N/P/A] ')).upper()
globalstart=time.time()
if logtype in ('S', 'N', 'P', 'A'):
    if logtype=='P':
        full=0
    elif logtype in ('N', 'A'):
        full=1
else:
    logtype='P'
    full=0
    print('Invalid scan-type. Defaulting to P')

hostname=str(socket.gethostname()) #computer name, used for filenames

#system info scan
colour('3f')
if logtype in ('S', 'P', 'A'):
    appjob('Performing System Info Scan...')
    print("\nPerforming System Info Scan...")
    sysinfostart=time.time()
    print("[Preparing to log]")
    sysinfo='System Info Logs'
    sysinfodir=sysinfo+'\\'
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

if logtype in ('N', 'P', 'A'):
    #network scan
    appjob('Performing Network Scan...')
    print("\nPerforming Network Scan...")
    netmapstart=time.time()
    print("[Preparing to log]")
    netmap='Network Logs'
    netmapdir=netmap+'\\'
    netip=socket.gethostbyname(socket.gethostname()) #ipv4 network IP
    try:
        pubip=urllib.request.urlopen('https://ident.me').read().decode('utf8') #public IP
        online = True
    except:
        print('[Error: No internet connection - Results will be limited]')
        pubip='[Error: No internet connection]'
        online = False
    if not os.path.exists(netmap):
        os.makedirs(netmap)
    if online:
        filename=str(hostname+" ["+netip+"]")
    else:
        filename=str(hostname+" ["+netip+"] [OFFLINE]")
    print("[Logging: Summary]")
    file=open(netmapdir+filename+".log","w")
    file.write("=Log Generated By ["+appname+"]=\n")
    file.write(datetime.datetime.now().strftime("[%d/%m/%Y] - [%H:%M:%S]"))
    if full==1:
        file.write('\nScan Type: Full')
    elif full==0:
        file.write('\nScan Type: Partial')
    if not online:
        file.write('\n\nError: No internet connection\nResults will be limited')
    file.write("\n\n===Summary===")
    file.write("\nHost Name: "+hostname)
    file.write("\nNetwork IP: "+netip)
    file.write("\nPublic IP: "+pubip)
    file.close()
    file=open(netmapdir+filename+".log","a")
    print("[Logging: Windows IP Configuration]")
    file.write("\n\n===Windows IP Configuration===")
    cmd('ipconfig /all >"'+netmapdir+filename+'.log.tmp"')
    file.writelines(open(netmapdir+filename+".log.tmp").readlines())
    os.remove(netmapdir+filename+".log.tmp")
    file.flush()
    print("[Logging: Routing Table]")
    file.write("\n\n==Routing Table==")
    cmd('netstat -r >"'+netmapdir+filename+'.log.tmp"')
    file.writelines(open(netmapdir+filename+".log.tmp").readlines())
    os.remove(netmapdir+filename+".log.tmp")
    file.flush()
    print("[Logging: IP-to-Physical address translation tables used by address resolution protocol (ARP)]")
    file.write("\n\n==IP-to-Physical address translation tables used by address resolution protocol (ARP)==")
    cmd('arp -a >"'+netmapdir+filename+'.log.tmp"')
    file.writelines(open(netmapdir+filename+".log.tmp").readlines())
    os.remove(netmapdir+filename+".log.tmp")
    file.flush()
if logtype in ('N', 'A'):
    print("[Logging: Protocol statistics and current TCP/IP network connections] [This might take a while!]")
    file.write("\n\n==Protocol statistics and current TCP/IP network connections==")
    cmd('netstat >"'+netmapdir+filename+'.log.tmp"')
    file.writelines(open(netmapdir+filename+".log.tmp").readlines())
    os.remove(netmapdir+filename+".log.tmp")
    file.flush()
    netmapend=time.time()
    netmapduration=netmapend-netmapstart
    file=open(netmapdir+filename+".log","a")
    file.write("\n\n===================\nLog completed in "+str(round(netmapduration, 2))+" seconds")
    print("Log completed in "+str(round(netmapduration, 2))+" seconds")


#m5: stats
file.close()
globalend=time.time()
globalduration=globalend-globalstart+importduration
appjob('Complete!')
print("\n\nAll "+proj+" Logging Jobs Completed In "+str(round(globalduration, 2))+" seconds")
cmd('timeout 5')
