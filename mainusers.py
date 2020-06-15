from users.creation import askcreateuser
from users.passwd import changepassword
from users.showusers import showmyuserslist
from users.showusers import showuserinformation
from users.deletion import askdeleteuser

def mainusers():

    while True:
        try:
            select_choice = int(input(
                "\n1- Create Users\n2- Modify Passwords For Users\n3- Show Users List\n4- Show User Information\n5- Delete Users\n6- Exit Users Mode\nChoose Option : "))
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
            if select_choice == 1:
                askcreateuser()
                continue
            elif select_choice == 2:
                changepassword()
                continue
            elif select_choice == 3:
                showmyuserslist()
                continue
            elif select_choice == 4:
                showuserinformation()
                continue
            elif select_choice == 5:
                askdeleteuser()
                continue
            elif select_choice == 6:
                print("END.")
                break
            else:
                print("\n[WRONG VALUE] try again! ")
                continue


if __name__ == "__main__":
    mainusers()