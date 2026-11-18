hostname = "Local-host"
port = 443
cpu_usage = 45.7
is_healthy = True
owner = None
port_text = "8080"
new_port = int(port_text)


print(hostname,type(hostname))
print(port,type(port))
print(cpu_usage,type(cpu_usage))
print(is_healthy,type(is_healthy))
print(owner,type(owner))
print(new_port + 1)

print(f"hostname = {hostname} (type: {type(hostname).__name__})")
print(f"port = {port} (type: {type(port).__name__})")
print(f"cpu_usage = {cpu_usage} (type: {type(cpu_usage).__name__})")
print(f"is_healthy = {is_healthy} (type: {type(is_healthy).__name__})")
print(f"owner = {owner} (type: {type(owner).__name__})")

