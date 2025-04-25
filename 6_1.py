class Password_manager:
    def __init__(self):
        self.old_passwords = []
    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        else:
            return None
    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
        else:
            print("This password already exist in the list")
    def is_correct(self, password_to_check):
        return password_to_check == self.get_password()

pm = Password_manager()

a=True
while a:
    c = int(input("Enter the case number: "))
    match c:
        case 1:
            st=input("Give the new password to set: ")
            pm.set_password(st)
        case 2:
            print(pm.get_password())
        case 3:
            st=input("Enter the password: ")
            print(pm.is_correct(st))
        case 4:
            a=False
            break