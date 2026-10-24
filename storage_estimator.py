#storage_estimator.py
storage_gb = float(input("enter storage in GB:"))
storage_mb = storage_gb*1024
print( " total storage needed:", round( storage_mb, 2), "MB")
total_gb = storage_mb/1024
print (" total storage needed :" , round (total_gb, 2), "GB")
