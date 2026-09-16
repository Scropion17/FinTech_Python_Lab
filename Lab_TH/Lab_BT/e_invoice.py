# Tính hóa đơn bán lẻ thương mại điện tử
Ten_san_pham = input("Nhập tên sản phẩm: ")
So_Luong_san_pham = int(input("Nhập số lượng sản phẩm: "))
Don_gia = float(input("Nhập đơn giá: "))
# Hiện hóa đơn bán hàng có định dạng các số tiền theo dạng có phân cách hàng nghìn (sử dụng cú pháp:,.0f trong F-string).
print("\n---HOA_DON_BAN_HANG---")
print(f"Ten_san_pham: {Ten_san_pham}")
print(f"So_Luong_san_pham: {So_Luong_san_pham}")
print(f"Don_gia: {Don_gia}")
# Tính Tổng Thanh toán sau khi cộng tổng tiền hàng với thuế VAT
Tong_tien_hang = So_Luong_san_pham * Don_gia
print(f"Tong_tien_hang: {Tong_tien_hang}")
Thue_VAT = 0.08 * Tong_tien_hang    
print(f"Thue_VAT: {Thue_VAT}")
Tong_thanh_toan = Tong_tien_hang + Thue_VAT
print(f"Tong_thanh_toan: {Tong_thanh_toan}")
