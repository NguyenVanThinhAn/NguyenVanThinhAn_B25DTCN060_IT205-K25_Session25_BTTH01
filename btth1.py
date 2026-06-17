class BankAccount:

    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self._account_name = ""
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
        cleaned_name = " ".join(new_name.strip().split())

        if not cleaned_name:
            print("Tên tài khoản không được để trống")
            return

        self._account_name = cleaned_name.upper()


    @staticmethod
    def validate_account_number(account_number):
        return (
            account_number.isdigit()
            and len(account_number) == 10
        )


    @classmethod
    def update_transaction_fee(cls, new_fee):
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            return False

        cls.transaction_fee = new_fee
        return True


    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        total_amount = amount + BankAccount.transaction_fee

        if self.__balance < total_amount:
            print(
                "Giao dịch thất bại. "
                "Số dư không đủ để thanh toán số tiền và phí giao dịch"
            )
            return False

        self.__balance -= total_amount
        return True

    def display_info(self):
        print("--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.account_name}")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(
            f"Phí giao dịch: "
            f"{BankAccount.transaction_fee:,} VND"
        )
def create_account():
    print("--- MỞ TÀI KHOẢN MỚI ---")

    while True:
        account_number = input(
            "Nhập số tài khoản 10 chữ số: "
        ).strip()

        if BankAccount.validate_account_number(
                account_number):
            break

        print("Số tài khoản không hợp lệ!")
        print("Số tài khoản phải gồm đúng 10 chữ số.")

    account_name = input(
        "Nhập tên chủ tài khoản: "
    )

    account = BankAccount(
        account_number,
        account_name
    )

    print("Mở tài khoản thành công!")
    print(f"Số tài khoản: {account.account_number}")
    print(f"Tên chủ tài khoản: {account.account_name}")

    return account


def view_account(account):
    if account is None:
        print("Hệ thống chưa có thông tin tài khoản")
        print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        return

    account.display_info()


def transaction_menu(account):
    if account is None:
        print("Hệ thống chưa có thông tin tài khoản")
        print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        return

    print("--- GIAO DỊCH NẠP / RÚT TIỀN ---")
    print("1. Nạp tiền")
    print("2. Rút tiền")

    choice = input(
        "Chọn loại giao dịch (1-2): "
    ).strip()

    try:
        amount = int(
            input("Nhập số tiền giao dịch: ")
        )
    except ValueError:
        print("Số tiền không hợp lệ")
        return

    if choice == "1":
        if account.deposit(amount):
            print(
                f"Nạp tiền thành công: "
                f"+{amount:,} VND"
            )
            print(
                f"Số dư mới: "
                f"{account.balance:,} VND"
            )

    elif choice == "2":
        if account.withdraw(amount):
            print(
                f"Rút tiền thành công: "
                f"-{amount:,} VND"
            )
            print(
                f"Phí giao dịch: "
                f"{BankAccount.transaction_fee:,} VND"
            )
            print(
                f"Số dư mới: "
                f"{account.balance:,} VND"
            )
        else:
            print(
                f"Số dư mới: "
                f"{account.balance:,} VND"
            )

    else:
        print("Lựa chọn không hợp lệ")


def update_account_name(account):
    if account is None:
        print("Hệ thống chưa có thông tin tài khoản")
        print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
        return

    print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")

    old_name = account.account_name

    new_name = input("Nhập tên mới: ")

    account.account_name = new_name

    if account.account_name != old_name:
        print(
            f"Cập nhật thành công. "
            f"Tên mới: {account.account_name}"
        )


def update_fee():
    print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
    print(
        f"Phí giao dịch hiện tại: "
        f"{BankAccount.transaction_fee:,} VND"
    )

    try:
        new_fee = int(
            input("Nhập phí giao dịch mới: ")
        )
    except ValueError:
        print("Phí giao dịch không hợp lệ")
        return

    if BankAccount.update_transaction_fee(new_fee):
        print(
            f"Đã cập nhật phí giao dịch toàn hệ thống "
            f"thành {BankAccount.transaction_fee:,} VND"
        )
    else:
        print(
            f"Phí giao dịch hiện tại vẫn là "
            f"{BankAccount.transaction_fee:,} VND"
        )


def main():
    current_account = None

    while True:

        choice = input('''
===== VIETCOMBANK DIGIBANK SIMULATOR =====
1. Mở tài khoản mới
2. Xem thông tin tài khoản
3. Giao dịch Nạp / Rút tiền
4. Cập nhật Tên chủ tài khoản
5. Đổi phí giao dịch hệ thống
6. Thoát chương trình
==========================================
Chọn chức năng (1-6): 
''')

        if choice == "1":
            current_account = create_account()

        elif choice == "2":
            view_account(current_account)

        elif choice == "3":
            transaction_menu(current_account)

        elif choice == "4":
            update_account_name(current_account)

        elif choice == "5":
            update_fee()

        elif choice == "6":
            print("Thoát chương trình")
            break

        else:
            print("Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()