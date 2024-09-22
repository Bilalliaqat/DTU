# Replace with your first and last name
first_name = "Bilal-"
last_name = "Liaqat"

# Filename for the CSV
csv_filename = f"{first_name}-{last_name}.csv"

# Write the DataFrame to a CSV file
country_avg_rate.to_csv(csv_filename, index=False)

print(f"CSV file saved as {csv_filename}")


from azure.identity import AzureCliCredential
from azure.storage.blob import BlobServiceClient

# Azure Storage account and container details
storage_account_url = "https://dataengineerv1.blob.core.windows.net"
container_name = "raw"
directory_name = f"{first_name}-{last_name}"

# Authenticate using Azure CLI
credential = AzureCliCredential()
blob_service_client = BlobServiceClient(account_url=storage_account_url, credential=credential)

# Create a BlobClient to upload the CSV file to the new directory
blob_client = blob_service_client.get_blob_client(container=container_name, blob=f"{directory_name}/{csv_filename}")

# Open the CSV file and upload it
with open(csv_filename, "rb") as data:
    blob_client.upload_blob(data)

print(f"CSV file {csv_filename} uploaded to Azure Storage in directory {directory_name}.")
