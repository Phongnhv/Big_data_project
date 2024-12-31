import pandas as pd

# Danh sách tên cột
colnames = [
    'Transaction_unique_identifier', 'price', 'Date_of_Transfer',
    'postcode', 'Property_Type', 'Old/New',
    'Duration', 'PAON', 'SAON',
    'Street', 'Locality', 'Town/City',
    'District', 'County', 'PPDCategory_Type',
    'Record_Status - monthly_file_only'
]

# Đọc file CSV theo từng chunk có kích thước 100,000 dòng và chỉ định tiêu đề
chunk_size = 100000
chunks = pd.read_csv('data.csv', chunksize=chunk_size, names=colnames, header=None)  # Đặt header=None để không dùng dòng đầu làm tiêu đề

# Lấy 100,000 dòng đầu tiên
first_100k_rows = next(chunks)

# Ghi 100,000 dòng đầu tiên vào một file CSV mới
output_file = 'first_100k_rows.csv'
first_100k_rows.to_csv(output_file, index=False, header=True)  # Ghi tiêu đề vào file

print(f"100,000 dòng đầu tiên đã được ghi vào file {output_file} với tiêu đề chính xác.")
