# hw1_email_masking.py
print("--- MASKING EMAIL KHÁCH HÀNG ---")

# 1. Nhập địa chỉ email
email = input("Nhập địa chỉ email: ")

# 2. Tách tên đăng nhập và tên miền bằng split("@")
parts = email.split("@")
username = parts[0]   # VD: nguyenvana
domain = parts[1]     # VD: gmail.com

# 3. Trích xuất 3 ký tự đầu tiên của tên đăng nhập (Slicing)
first_three = username[0:3]

# 4. Ghép 3 ký tự đầu + "***@" + tên miền
masked_email = first_three + "***@" + domain

print(f"Email gốc     : {email}")
print(f"Email đã che  : {masked_email}")