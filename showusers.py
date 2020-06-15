import subprocess

def showuserinformation():
    list_of_users = showmyuserslist()
    while True:
        try:
            chosen_user = str(input("\nChoose User  ( enter username ) : "))
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
            for i in list_of_users:
                if str(i[0]) == chosen_user:
                    A = i[6]
                    print("\n\nGeneral Information : \n")
                    subprocess.call(f'id {chosen_user}', shell=True)
                    print(f"username:{i[0]}  ,homedir:{i[5]}  ,comment:{i[4]}  ,shell:{A[:-1:]}")
                    subprocess.call(f'chage -l {chosen_user}', shell=True)

            break


def retrievedatafrompasswdfile():
    list_of_users = []
    with open("/etc/passwd", mode='r') as passwd_content:
        each_line = passwd_content.readlines()
        passwd_content.close()

    for each_user in each_line:
        each_user2 = each_user.split(":")
        list_of_users.append(each_user2)

    return list_of_users

def showmyuserslist():
    list_of_users = retrievedatafrompasswdfile()
    '''
    for i in list_of_users:
        print(i)
    '''
    print("\n\n----------------------------------------\nList Of Users : \n-------------------------------------")
    for i in list_of_users:
        if int(i[2]) >= 1000:
            A = i[6]
            print(
                f"username:{i[0]}  ,userID:{i[2]}  ,groupID:{i[3]}  ,homedir:{i[5]}  ,comment:{i[4]}  ,shell:{A[:-1:]}")

    return list_of_users