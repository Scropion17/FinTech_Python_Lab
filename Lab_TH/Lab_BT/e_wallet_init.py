# Mở ví điện tử ban đầu 
Ho_va_ten = input(" Nhập họ và tên của bạn: ")
So_dien_thoai = input("Nhập số điện thoại của bạn: ")
So_can_cuoc_cong_dan = input("Nhập số căn cước công dân của bạn: ")
So_tien_khoi_tao = int(input("Nhập số tiền khởi tạo cho ví của bạn: "))
# Hiện thị biên lai giao dich sử dụng f-string 
print("\n--- Bien_LAI_GIAO_DICH---")
print(f"Ho_ten_khach_hang: {Ho_va_ten}")
print(f"So_dien_thoai: {So_dien_thoai}")
print(f"So_can_cuoc_cong_dan: {So_can_cuoc_cong_dan}")
print(f"so_tien_nap_ban_dau_vao_vi: {So_tien_khoi_tao:,} VND")
# Hệ thống sẽ tự động trừ 50,000 VND phí mở tài khoản
Phí_mở_tài_khoản = 50000
print(f"Phí_mở_tài_khoản: {Phí_mở_tài_khoản:,} VND")
print("-" * 25) # In ra 25 dấu gạch ngang để trang trí
# Tính số tiền còn lại trong ví sau khi trừ phí
So_tien_con_lai = So_tien_khoi_tao - Phí_mở_tài_khoản
print(f"so_tien_con_lai_trong_vi: {So_tien_con_lai:,} VND")
print(f"Chuc_mung_ban_da_khoi_tao_vi_dien_tu_thanh_cong! Vui_long_kiem_tra_vi_cua_ban.")
print(f"Chuc_ban_mot_ngay_giao_dich_vui_ve_va_hieu_qua!")
