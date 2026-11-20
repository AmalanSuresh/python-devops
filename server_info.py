# --- Server details ---
hostname = "Local-host"
port = 443
cpu_usage = 45.7
is_healthy = True
owner = None

# --- Print each value with its type ---
print(f"hostname = {hostname} (type: {type(hostname).__name__})")
print(f"port = {port} (type: {type(port).__name__})")
print(f"cpu_usage = {cpu_usage} (type: {type(cpu_usage).__name__})")
print(f"is_healthy = {is_healthy} (type: {type(is_healthy).__name__})")
print(f"owner = {owner} (type: {type(owner).__name__})")

# --- Converting text to a number ---
port_text = "8080"
new_port = int(port_text)
print(new_port + 1)