from azure.identity import AzureCliCredential
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

# Azure Storage account and container details
storage_account_url = "https://dataengineerv1.blob.core.windows.net"  # Storage account URL
container_name = "raw"  # Name of the container
blob_name = "tourism_dataset.csv"  # Name of the CSV file in the container

# Create a BlobServiceClient using AzureCliCredential for authentication
credential = AzureCliCredential()
blob_service_client = BlobServiceClient(account_url=storage_account_url, credential=credential)

# Get the BlobClient for the specific blob (CSV file)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download the blob (CSV file) content as a stream
blob_data = blob_client.download_blob().readall()

# Load the CSV content into a Pandas DataFrame
df = pd.read_csv(io.BytesIO(blob_data))

# Display the DataFrame
print(df.head())
