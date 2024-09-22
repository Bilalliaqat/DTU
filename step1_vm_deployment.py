from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient

# Azure credentials using Azure CLI
credential = AzureCliCredential()

# Subscription ID and resource group details
subscription_id = "aee8556f-d2fd-4efd-a6bd-f341a90fa76e"
resource_group_name = "Data_Engineer"

# Initialize clients
resource_client = ResourceManagementClient(credential, subscription_id)
network_client = NetworkManagementClient(credential, subscription_id)
compute_client = ComputeManagementClient(credential, subscription_id)

# Define VNet parameters
vnet_name = "BilalLiaqar"
region = "westeurope"  # You can change this to your preferred region

vnet_params = {
    "location": region,
    "address_space": {"address_prefixes": ["10.0.0.0/16"]}
}

# Create the Virtual Network (VNet)
vnet_creation = network_client.virtual_networks.begin_create_or_update(
    resource_group_name,
    vnet_name,
    vnet_params
)
vnet_result = vnet_creation.result()
print(f"Created VNet: {vnet_result.name}")

# Define Subnet parameters
subnet_name = "default"
subnet_params = {
    "address_prefix": "10.0.0.0/24"
}

# Create the Subnet
subnet_creation = network_client.subnets.begin_create_or_update(
    resource_group_name,
    vnet_name,
    subnet_name,
    subnet_params
)
subnet_result = subnet_creation.result()
print(f"Created Subnet: {subnet_result.name}")

# Define Network Interface Card (NIC) parameters
nic_name = "Bilalliaqat"
ip_config_name = "Ipv4config"

ip_params = {
    "location": region,
    "sku": {"name": "Standard"},
    "public_ip_allocation_method": "Dynamic"
}

# Create Public IP
public_ip_creation = network_client.public_ip_addresses.begin_create_or_update(
    resource_group_name,
    f"{nic_name}-PublicIP",
    ip_params
)
public_ip_result = public_ip_creation.result()

# Create NIC
nic_params = {
    "location": region,
    "ip_configurations": [{
        "name": ip_config_name,
        "subnet": {"id": subnet_result.id},
        "public_ip_address": {"id": public_ip_result.id},
        "private_ip_allocation_method": "Dynamic"
    }]
}

nic_creation = network_client.network_interfaces.begin_create_or_update(
    resource_group_name,
    nic_name,
    nic_params
)
nic_result = nic_creation.result()
print(f"Created Network Interface: {nic_result.name}")

# Define VM parameters
vm_name = "VM-Bilalliaqat"
username = "azureuser"
#password = "YourSecurePassword123!"  # Change this to a secure password

with open("/home/azureuser/.ssh/id_rsa.pub", "r") as ssh_file:
    ssh_key = ssh_file.read()

vm_params = {
    "location": region,
    "hardware_profile": {
        "vm_size": "Standard DS2 v3"
    },
    "storage_profile": {
        "image_reference": {
            "publisher": "canonical",
            "offer": "0001-com-ubuntu-server-jammy",
            "sku": "22_04-lts-gen2",
            "version": "latest"
        }
    },
    "os_profile": {
        "computer_name": vm_name,
        "admin_username": username,
        "admin_password": password
    },
    "network_profile": {
        "network_interfaces": [{
            "id": nic_result.id
        }]
    }
}

# Create the Virtual Machine (VM)
vm_creation = compute_client.virtual_machines.begin_create_or_update(
    resource_group_name,
    vm_name,
    vm_params
)
vm_result = vm_creation.result()
print(f"Created Virtual Machine: {vm_result.name}")
