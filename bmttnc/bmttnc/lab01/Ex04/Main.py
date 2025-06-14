from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\n=====================")
    print("********MENU********")
    print("1. Them sinh vien")
    print("2. Cap nhat sinh vien boi ID")
    print("3. Xoa sinh vien")
    print("4. Tim kiem sinh vien")
    print("5. Sap xep danh sach sinh vien theo diem trung binh")
    print("6. Sap xep danh sach sinh vien theo ten")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")
    print("=====================")
    
    choice = int(input("Nhap lua chon: "))
    
    if choice == 1:
        qlsv.nhapSinhVien()
        print("Da them sinh vien moi!")
    elif choice == 2:
        if(qlsv.soLuongSinhVien() > 0):
            print("Cap nhat sinh vien")
            ID = int(input("Nhap ID sinh vien can cap nhat: "))
            qlsv.updateSinhVien(ID)
        else:
            print("Khong co sinh vien nao de cap nhat!")
    elif choice == 3:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien")
            ID = int(input("Nhap ID sinh vien can xoa: "))
            if(qlsv.deleteByID(ID)):
                print("Da xoa sinh vien co ID = {}".format(ID))
            else:
                print("Khong tim thay sinh vien co ID = {}".format(ID))
    elif choice == 4:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien")
            name = input("Nhap ten sinh vien can tim: ")
            result = qlsv.findByName(name)
            qlsv.showSinhVien(result)
        else:
            print("Khong co sinh vien nao de tim kiem!")
    elif choice == 5:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep danh sach sinh vien theo diem trung binh")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Khong co sinh vien nao de sap xep!")
    elif choice == 6:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep danh sach sinh vien theo ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Khong co sinh vien nao de sap xep!")
    elif choice == 7:
        if(qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Khong co sinh vien nao de hien thi!")
    elif choice == 0:
        print("Thoat chuong trinh!")
        break
    else:
        print("Lua chon khong hop le! Vui long chon lai.")