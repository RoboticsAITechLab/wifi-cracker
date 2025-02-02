# WiFi Cracker Tool

> **WARNING:**  
> This tool is intended **ONLY** for educational and ethical penetration testing purposes.  
> **USE AT YOUR OWN RISK!**  
> Unauthorized use of this tool on networks without explicit permission is illegal and unethical.

---

## Overview

The **WiFi Cracker Tool** is a Python-based tool designed to perform the following tasks:

- **Enable Monitor Mode:** Switch your wireless interface (e.g., `wlan0`) to monitor mode.
- **Capture Packets:** Use `airodump-ng` to capture packets on a specific channel for a target network identified by its BSSID.
- **Deauthenticate Clients:** Send deauthentication packets with `aireplay-ng` to force clients off the network, increasing the chance of capturing a WPA handshake.
- **Crack Password:** Use `aircrack-ng` along with a user-provided wordlist to attempt to crack the Wi-Fi password.
- **Cleanup:** Disable monitor mode and restore the network interface to its managed state.

The tool also features a **stylish ASCII art banner** with a "dangerous" look and uses the `colorama` module to output colored messages in the terminal. It also employs Python's `subprocess`, `os`, `signal`, and `sys` modules for process management and graceful handling of interrupts.

---

## Features

- **Advanced Banner:**  
  Displays an intense ASCII art banner along with a warning message and developer credit.

- **Dependency Check:**  
  Verifies that all required tools (`airmon-ng`, `airodump-ng`, `aireplay-ng`, and `aircrack-ng`) are installed.

- **Process & Signal Handling:**  
  Gracefully handles keyboard interrupts (Ctrl+C) to terminate any running processes and disable monitor mode.

- **Monitor Mode & Packet Capture:**  
  Automatically switches to monitor mode and captures packets on the specified channel for the target network.

- **Deauthentication Attack:**  
  Sends deauth packets to force clients to disconnect, aiding in capturing the WPA handshake.

- **Password Cracking:**  
  Attempts to crack the Wi-Fi password using a specified wordlist file.

---

## Requirements

- **Linux Distribution:**  
  This tool is designed for Debian-based systems (e.g., Kali Linux).

- **Aircrack-ng Suite:**  
  - `airmon-ng`
  - `airodump-ng`
  - `aireplay-ng`
  - `aircrack-ng`  

  Install them via:
  ```bash
  sudo apt update
  sudo apt install aircrack-ng
