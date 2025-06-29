# 🔍 Python Port Scanner (Multithreaded)

A fast, simple TCP port scanner written in Python.  
Scans ports using multithreading and a queue-based system to identify open ports on a target device.

> ⚠️ **For educational purposes only.** Only scan devices you own or have **explicit permission** to test.



## 📦 Features

- ✅ Scans TCP ports from 1 to 1023 (well-known ports)
- 🚀 Multithreaded (~500–2000 ports/sec depending on system)
- 📥 Uses `Queue` to prevent duplicate scans
- 🧵 Adjustable number of threads (default: 500)
- 🔧 Clean and readable code with comments



## 🧠 How It Works

- Each port is added to a shared `Queue`
- Multiple threads pull ports from the queue and attempt TCP connections
- Successful connections = open ports, added to a list
- Closed ports are skipped for performance



## 🛠️ Usage

1. **Clone the repo**:
   
   ```bash
   git clone https://github.com/tktony/Port-Scanner.git
   cd Port-Scanner
   ```

2. **Edit the target IP inside `portscanner.py`**:
   
   ```bash
   target = "192.168.0.1"  # Example: your router or localhost
   ```

3. **Run the script**:
   
   ```bash
   python portscanner.py
   ```

## 🎓 Notes
- Adjust `thread_count` or `port_list` as needed.
- You can scan local devices like your router (e.g., 192.168.0.1) or localhost (127.0.0.1).
- Don’t scan public IPs without permission.

## 📌 Understanding Ports (Analogy)
Think of ports like doors or windows on a house. An open port is like an unlocked window where a specific service (e.g., HTTP on port 80) is accessible.
Closed ports are like shut windows - less risky, but still visible. Port scanning is like walking around the house and checking which windows respond when knocked on.


