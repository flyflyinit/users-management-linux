import subprocess
from users.showusers import showmyuserslist
import time
import concurrent.futures

def askdeleteuser():
    while True:
        try:
            ask = str(input("\nDelete More Users [Y/N] : "))
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
            if ask.lower() == 'y':
                ask2deleteuser()
                continue
            elif ask.lower() == 'n':
                print("END.")
                break
            else:
                print("\n[WRONG VALUE] try again! ")
                continue


def ask2deleteuser():
    while True:
        try:
            showmyuserslist()
            users_range = str(
                input("\nEnter User IDs of The Users That you want to Delete (example: 1005,1010-1020,1055,1057 ) : "))
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
            deleteuser(users_range)
            break


def deleteuserThreading(username):
    print(f"Deletion Of User {username} ...")
    subprocess.call(f'userdel -r {username}', shell=True)
    return f"{username} deleted!"


def deleteuser(users_range):
    list_of_users = showmyuserslist()
    usersid = users_range.split(",")
    list_of_users_to_delete=[]

    for userid in usersid:
        if '-' in userid:
            useridrange = userid.split("-")
            beginrange = int(useridrange[0])
            endrange = int(useridrange[1])
            print(f"\nDeletion Of Users In UID Range {beginrange} - {endrange} ")

            for j in range(beginrange,endrange+1):
                for k in list_of_users:
                    if str(k[2]) == str(j):
                        username = k[0]
                        list_of_users_to_delete.append(username)
                        break
                    else:
                        continue

        else:
            for i in list_of_users:
                if str(i[2]) == str(userid) :
                    username = i[0]
                    list_of_users_to_delete.append(username)
                    break
                else:
                    continue

    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(deleteuserThreading, list_of_users_to_delete)
        for result in results:
            print(result)
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')


'''
    while True:
        if no_duplication:
            duplicate_user = 'n'
            break
        else:
            try:
                users_range = str 
                duplicate_user = str(input("Do You Want To Users with Range or [Y/N] : "))
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
                if duplicate_user.lower() == 'y':
                    break
                elif duplicate_user.lower() == 'n':
                    break
                else:
                    print("\n[WRONG VALUE] try again! ")
                    continue

    initial_increment = False
    for i in range(1, users_number + 1):
        if duplicate_user.lower() == 'y':
            while initial_increment == False:
                while True:
                    print("\nParameters For All Users : ")
                    try:
                        username = str(
                            input("username (username will be genereate like this username1,username2... ) : "))
                        userid = int(input("range beginning user-id : "))
                        comment = str(input("comment (comments will be generated like this  comment1,comment2... ) : "))
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
                        initial_increment = True
                        break

            username_u = username + str(i)
            comment_u = comment + str(i)
            print(f"\nCreation Of User Number {i} ...")
            subprocess.call(f'useradd -u {userid} -c "{comment_u}" {username_u}', shell=True)
            print("success!")
            userid = userid + 1
            continue

        elif duplicate_user.lower() == 'n':
            while True:
                print(f"\nCreation Of User Number {i} ... ")
                try:
                    username = str(input("username : "))
                    userid = int(input("user-id : "))
                    comment = str(input("comment : "))
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
                    subprocess.call(f'useradd -u {userid} -c "{comment}" {username}', shell=True)
                    print("success!")
                    break
        else:
            print("\n[WRONG VALUE] try again! ")
            break
'''
