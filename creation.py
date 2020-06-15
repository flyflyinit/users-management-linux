import subprocess
import concurrent.futures
import time

def createuserThreading(user):
    print(f"\nCreation Of User {user[2]} ,with id {user[0]} ...")
    subprocess.call(f'useradd -u {user[0]} -c "{user[1]}" {user[2]}', shell=True)
    return f"{user[2]} created!"


def askcreateuser():
    while True:
        try:
            ask = str(input("\nCreate More Users [Y/N] : "))
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
                createuser()
                continue
            elif ask.lower() == 'n':
                print("END.")
                break
            else:
                print("\n[WRONG VALUE] try again! ")
                continue

def createuser():
    no_duplication = False
    while True:
        try:
            users_number = int(input("How Many Users You Want To Create : "))
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
            if users_number == 1:
                no_duplication = True
            break

    while True:
        if no_duplication:
            duplicate_user = 'n'
            break
        else:
            try:
                duplicate_user = str(input("Do You Want To Duplicate The Same Parameters For All Users [Y/N] : "))
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
    list_of_users_to_create=[]

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

            list_of_users_to_create.append((userid,comment_u,username_u))

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

    if duplicate_user.lower() == 'y':
        start = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(createuserThreading, list_of_users_to_create)
            for result in results:
                print(result)
        finish = time.perf_counter()
        print(f'Finished in {round(finish - start, 2)} second(s)')


if __name__ == '__main__':
    askcreateuser()