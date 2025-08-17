#Start Multiple Virtual Machines


def start_vms(*vm_names):
    for vm in vm_names:
        print(f"Starting VM: {vm}")

start_vms("VM1", "VM2", "VM3")
