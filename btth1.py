class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.account_name = account_name 
        self.__balance = 0 

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, new_name):
        if not new_name or not new_name.strip():
            print("Tên tài khoản không được để trống")
            return
        self._account_name = " ".join(new_name.split()).upper()

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_transaction_fee(cls, new_fee):
        try:
            new_fee = int(new_fee)
            if new_fee < 0:
                print("Phí giao dịch không được âm")
                print(f"Phí giao dịch hiện tại vẫn là {cls.transaction_fee:,} VND")
                return False
            cls.transaction_fee = new_fee
            print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {new_fee:,} VND")
            return True
        except ValueError:
            print("Phí giao dịch nhập vào phải là một số hợp lệ!")
            return False

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False
        self.__balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VND")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False
        
        total_deduction = amount + BankAccount.transaction_fee
        if self.__balance < total_deduction:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            return False
        
        self.__balance -= total_deduction
        print(f"Rút tiền thành công: -{amount:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
        return True

    def display_info(self):
        print("--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.account_name}")
        print(f"Số dư hiện tại: {self.__balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")


current_account = None

while True:
    print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
    print("1. Mở tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Giao dịch Nạp / Rút tiền")
    print("4. Cập nhật Tên chủ tài khoản")
    print("5. Đổi phí giao dịch hệ thống")
    print("6. Thoát chương trình")
    print("==========================================")
    
    select = input("Chọn chức năng (1-6): ").strip()
    
    match select:
        case "1":
            print("--- MỞ TÀI KHOẢN MỚI ---")
            while True:
                acc_num = input("Nhập số tài khoản 10 chữ số: ").strip()
                if not BankAccount.validate_account_number(acc_num):
                    print("Số tài khoản không hợp lệ!")
                    print("Số tài khoản phải gồm đúng 10 chữ số.")
                    continue
                break
                
            acc_name = input("Nhập tên chủ tài khoản: ")
            current_account = BankAccount(acc_num, acc_name)
            
            if hasattr(current_account, '_account_name'):
                print("Mở tài khoản thành công!")
                print(f"Số tài khoản: {current_account.account_number}")
                print(f"Tên chủ tài khoản: {current_account.account_name}")
            else:
                current_account = None

        case "2":
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
            else:
                current_account.display_info()

        case "3":
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
            else:
                print("--- GIAO DỊCH NẠP / RÚT TIỀN ---")
                print("1. Nạp tiền")
                print("2. Rút tiền")
                type_select = input("Chọn loại giao dịch (1-2): ").strip()
                
                try:
                    amount_in = float(input("Nhập số tiền giao dịch: "))
                    if type_select == "1":
                        current_account.deposit(amount_in)
                    elif type_select == "2":
                        current_account.withdraw(amount_in)
                    else:
                        print("Lựa chọn loại giao dịch không hợp lệ.")
                        
                    print(f"Số dư mới: {current_account.balance:,} VND")
                except ValueError:
                    print("Số tiền nhập vào không hợp lệ!")
                
        case "4":
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
            else:
                print("--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
                new_name_in = input("Nhập tên mới: ")
                old_name = current_account.account_name
                current_account.account_name = new_name_in
                
                if current_account.account_name != old_name or (new_name_in.strip() != ""):
                    if new_name_in.strip():
                        print(f"Cập nhật thành công. Tên mới: {current_account.account_name}")

        case "5":
            print("--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
            print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")
            fee_in = input("Nhập phí giao dịch mới: ").strip()
            BankAccount.update_transaction_fee(fee_in)

        case "6":
            print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
            break
            
        case _:
            print("Chức năng không hợp lệ! Vui lòng chọn lại từ 1-6.")
