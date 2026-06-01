import socket
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = [
    21,
    22,
    25,
    53,
    80,
    110,
    143,
    443,
    3306,
    8080
]

SERVICES = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}


def banner_grab(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((host, port))

        try:
            banner = sock.recv(1024).decode(errors="ignore").strip()

            if banner:
                return banner
        except:
            pass

        if port in [80, 8080]:
            request = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {host}\r\n"
                f"Connection: close\r\n\r\n"
            )

            sock.send(request.encode())

            response = sock.recv(1024).decode(errors="ignore")
            return response.split("\n")[0].strip()

        return "No banner returned"

    except:
        return None

    finally:
        sock.close()


def scan_port(host, port):
    banner = banner_grab(host, port)

    if banner:
        service = SERVICES.get(port, "Unknown")

        print(f"[+] Port {port} OPEN ({service})")
        print(f"    Banner: {banner}\n")


def main():
    host = input("target IP or hostname: ").strip()

    print(f"\nScanning {host}...\n")

    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in COMMON_PORTS:
            executor.submit(scan_port, host, port)


if __name__ == "__main__":
    main()