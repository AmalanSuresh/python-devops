line = (
    '2026-11-24T08:45:13Z level=ERROR service=payment-api '
    'host=ip-10-0-3-17.eu-central-1.compute.internal latency_ms=1532 '
    'request_id=7f3a9c msg="db connection timeout after 3 retries"'
)

parts = line.split()
timestamp = parts[0]

date = timestamp.split("T")[0]
time = timestamp.split("T")[1].strip("Z")
level = parts[1].split("=")[1]
service = parts[2].split("=")[1]
request_id = parts[5].split("=")[1]
latency = int(parts[4].split("=")[1])
is_slow = latency > 1000
host = parts[3].split("=")[1]
ip_part = host.split(".")[0]
private_ip = ip_part[3:].replace("-", ".")
region = host.split(".")[1]

print(f"Date       : {date}")
print(f"Time       : {time}")
print(f"Level      : {level}")
print(f"Service    : {service}")
print(f"Request ID : {request_id}")
print(f"Latency    : {latency} ms (slow: {is_slow})")
print(f"Private IP : {private_ip}")
print(f"Region     : {region}")
