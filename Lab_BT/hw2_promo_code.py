# hw2_promo_code.py
print("--- MÁY PHÁT SINH MÃ ƯU ĐÃI ---")

# 1. Nhập họ tên đầy đủ và năm sinh
full_name = input("Nhập họ tên đầy đủ: ").strip()
birth_year = input("Nhập năm sinh: ").strip()

# 2. Lấy phần Tên (từ cuối cùng trong họ tên đầy đủ)
# VD: "Lê Văn Mẹo" -> ["Lê", "Văn", "Mẹo"] -> "Mẹo"
first_name = full_name.split()[-1]

# 3. Lấy 3 ký tự đầu của Tên và viết hoa
# Slicing [0:3] tự động lấy toàn bộ nếu tên ngắn hơn 3 ký tự (VD: "An")
name_part = first_name[0:3].upper()

# 4. Ghép mã ưu đãi theo quy tắc: [TÊN]-[Năm sinh]-[VIP]
promo_code = f"{name_part}-{birth_year}-VIP"

print(f"Mã ưu đãi của bạn: {promo_code}")