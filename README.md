# SecToolkit

A lightweight Python toolkit for network reconnaissance and service enumeration.

## Features

- TCP port scanning
- Banner grabbing
- Basic service fingerprinting
- Multi-threaded scanning for faster execution

## Modules

### Port Scanner
Scans common TCP ports on a target host and identifies which ones are open.

Example:

```bash
[+] Port 22 OPEN
[+] Port 80 OPEN
```

---

### Grabber
Attempts to retrieve banners from open services for identification and version fingerprinting.

Example:

```bash
22/tcp → SSH-2.0-OpenSSH_9.7
80/tcp → HTTP/1.1 200 OK
```

Useful for identifying:

- SSH servers
- Web servers
- FTP services
- Mail services

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-user/sec-toolkit.git
cd sec-toolkit
```

No external dependencies are required.

---

## Usage

Run:

```bash
python main.py
```

Then provide a target:

```bash
Target IP or hostname: scanme.nmap.org
```

Example output:

```bash
Scanning scanme.nmap.org...

[+] Port 22 OPEN (SSH)
    Banner: SSH-2.0-OpenSSH_9.7

[+] Port 80 OPEN (HTTP)
    Banner: HTTP/1.1 200 OK
```

---

## Project Structure

```bash
sec-toolkit/
├── main.py
├── portscan.py
├── banner_grabber.py
└── README.md
```

---

## Disclaimer

This project was built for educational purposes and authorized security testing only.

Use only on systems you own or have explicit permission to assess.

---

## Roadmap

Future additions:

- DNS enumeration
- WHOIS lookup
- HTTP security header analysis
- Subdomain enumeration
- JSON/CSV export
- CLI arguments with argparse

---

## Author

Built by Patrícia Ferreira.
