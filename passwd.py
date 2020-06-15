import subprocess
from users.showusers import showmyuserslist


def changepassword():
    showmyuserslist()

    while True:
        try:
            users_number = str(input("Do You Want To Change Password For One User Or Many Users [ONE/MANY] : "))
        except TypeError:
            print("\n[DATATYPE ERROR] try again! ")
            continue
        except ValueError:
            print("\n[VALUE ERROR] try again! ")
            continue
        except:
            print("\n[ERROR] try again! ")
            continue
        else:
            if users_number.lower() == 'one':
                changepassword_one_user()
                break
            elif users_number.lower() == 'many':
                changepassword_many_users()
                break
            else:
                print("\n[WRONG VALUE] try again! ")
                continue


def changepassword_one_user():
    while True:
        try:
            user = str(input("Enter username : "))
        except TypeError:
            print("\n[DATATYPE ERROR] try again! ")
            continue
        except ValueError:
            print("\n[VALUE ERROR] try again! ")
            continue
        except:
            print("\n[ERROR] try again! ")
            continue
        else:
            subprocess.call(f'passwd {user}', shell=True)
            print("success!")
            break


def changepassword_many_users():
    while True:
        try:
            users = str(input("Specify usernames ( example: username1,username2.. )  : "))
        except TypeError:
            print("\n[DATATYPE ERROR] try again! ")
            continue
        except ValueError:
            print("\n[VALUE ERROR] try again! ")
            continue
        except:
            print("\n[ERROR] try again! ")
            continue
        else:
            list_of_users = users.split(",")
            for user in list_of_users:
                print("\n")
                subprocess.call(f'passwd {user}', shell=True)
            print("success!")
            break
