file_mb = input('How many MBs is the file? ')
internet_velocity = input('How fast is your internet? ')
download_in_mbps = float(file_mb) / float(internet_velocity)
MINUTE = 60
download_in_mbpm = download_in_mbps // MINUTE
download_in_mbpm_rest = download_in_mbps % MINUTE

print(f'The download will be completed in {download_in_mbpm} minutes and {download_in_mbpm_rest} seconds approximately')
