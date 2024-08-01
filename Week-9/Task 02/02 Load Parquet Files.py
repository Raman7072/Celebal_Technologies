# Load Parquet Files into Folders in ADLS

import shutil

# Organize files into year-month folders

for date in dates:
    year_month = date.strftime('%Y%m')
    dest_dir = os.path.join(output_dir, year_month)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    file_name = f'TSK_{date.strftime("%Y%m%d")}.parquet'
    file_path = os.path.join(output_dir, file_name)
    shutil.move(file_path, os.path.join(dest_dir, file_name))

# Upload to ADLS
# Note:- Ensure that you replace placeholders with your actual values

account_name = 'your_adls_account'
container_name = 'your_container'
file_system = f'https://{account_name}.dfs.core.windows.net/{container_name}'

for root, dirs, files in os.walk(output_dir):
    for file in files:
        local_file_path = os.path.join(root, file)
        relative_path = os.path.relpath(local_file_path, output_dir)
        adls_path = os.path.join(file_system, relative_path)
        os.system(f'az storage fs file upload -s {local_file_path} -p {adls_path} --account-name {account_name}')
