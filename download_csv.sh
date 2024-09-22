#Azure CLI Authentication
!az login


#Download the CSV File to the VM Using Azure CLI
az vm ssh --resource-group Data_Engineer --name VM-BilalLiaqat

#Use Azure CLI to Download the File
az storage blob download \
  --account-name dataengineerv1 \
  --container-name raw \
  --name "Bilal-Liaqat/<Bilal-Liaqat.csv>" \
  --file result-Bilal.csv \
  --account-key "ieLmjePYNxBcajmfHvX8TsMXa3bn8nkH3MCuaWTsA/E+G56z3KRYSPO1M5MaHNds5FhE37PsZwYm+AStsnl/lg=="

#This will download the CSV file from the Azure Storage account to your VM's home directory, saving it as result-Bilal.csv