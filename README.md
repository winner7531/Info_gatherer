# 🕵️‍♂️ Info-Gatherer – Cybersecurity Recon Tool (Python)

A simple but effective information gathering tool built with Python for beginners in cybersecurity. It helps users collect key details about IP addresses and domains, including WHOIS data, public/private IPs, geo-location, and Tor IP—all via a clean command-line interface.

---

## 🚀 Features

🔹 **Get Private IP**  
🔹 **Get Public IP** (directly or via Tor)  
🔹 **Domain to IP Resolver**  
🔹 **WHOIS Lookup for Domains**  
🔹 **Geo-Location Lookup using IP**  
🔹 **Tor IP Check** *(requires Tor running on port 9050)*

---

## 🛠️ Installation & Requirements

### 📁 Clone the repository

```bash
git clone https://github.com/winner7531/Info_gatherer.git
cd Info_gatherer
```

### 📦 Install dependencies
```bash
#Tor installation
sudo apt install tor
sudo service tor start
```

```bash
pip install requests[socks] python-whois
```

### 🎨 For enhanced terminal output

```bash
pip install colorama pyfiglet
```

---

## 🧪 How to Run

```bash
python info_gatherer.py
```

You will see a terminal menu like:

```
🔥 INFO-GATHERING TOOL 🔍 by Panda

1. Get Private IP
2. Get Public IP
3. Get Domain IP
4. Get WHOIS Info
5. Get Geo Info
6. Get Tor IP
7. Exit
```

Enter the number to choose the action.

---

## 📸 Output Preview

Here’s what it looks like in action:

```
Geo IP location...
IP: 8.8.8.8
Country: United States
Region: California
City: Mountain View
ISP: Google LLC
Timezone: America/Los_Angeles
Latitude/Longitude: 37.386 , -122.0838
```

---

## 🔐 Notes

- Tor IP feature works only if **Tor** is running on your system (`127.0.0.1:9050`).
- Geo-location is fetched via `http://ip-api.com` (public API).
- This project is for **educational/research purposes** only.

---

## 🧠 Future Ideas

- Subdomain enumeration
- Port scanning (with socket or `nmap`)
- Result export to `.txt` or `.csv`
- Use `argparse` for CLI automation
- GUI version (Tkinter or PyQt)

---

## ✍️ Author

**Panda** – Aspiring Cybersecurity Analyst  
GitHub: [@winner7531](https://github.com/winner7531)

---

## 📄 License

This project is licensed under the MIT License.
