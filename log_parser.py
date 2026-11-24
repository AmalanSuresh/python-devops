line     = '192.168.1.10 - - [18/Nov/2026:17:45:12 +0100] "GET /api/health HTTP/1.1" 200 512 "-" "curl/8.5.0"'
raw_host = "  WEB-01.prod.example.com \n"

parts    = line.split()
ip       = parts[0]
status   = int(parts[8])
is_error = status >= 400
host     = raw_host.strip().lower().split(".")[0]

path   = parts[6]
size   = int(parts[9])
method = parts[5].strip('"')


print(f"IP     :{ip}")
print(f"status :{status}")
print(f"path   :{path}")
print(f"method :{method}")
print(f"Status :{status} (error: {is_error})")
print(f"Size : {size / 1024:.1f} KB")
print(f"Host   : {host}")