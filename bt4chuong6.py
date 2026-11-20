s = input("Nhập chuỗi: ")

# Tìm vị trí của từ "Email:"
vi_tri = s.find("Email:")

# Nếu có "Email:" trong chuỗi
if vi_tri != -1:
    # Lấy phần sau "Email:"
    email = s[vi_tri + len("Email:"):].strip()
    if email != "":
        print(email)
    else:
        print("Không có email")
else:
    print("Không có email")
