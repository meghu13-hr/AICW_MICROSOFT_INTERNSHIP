phone_book={}
def add_contact():
    name=input("enter the name:").strip().lower()
    phno=int(input("enter the number:").strip())
    phone_book[name] =phno
    #phone_book.update({name:phno})
    print("contact saved succesfully")
    print(phone_book)
def read_contact():
    search_name=input("enter the searching name").strip().lower()
    if search_name in phone_book.keys():
        print(f"the number for {search_name} is:{phone_book[search_name]}")
    else:
        print(f" the contact is not available")
def update_contact():
    update_name=input("enter the name to be updated").strip().lower()
    update_num=int(input("enter the num to be updated").strip())
    phone_book[update_name]=update_num
    print("contact saved !!!")
def delete_contact():
    delete_name=input("enter the deleted name")
    if delete_name in phone_book.keys():
        del phone_book[delete_name]
        print(f"the {delete_name} is deleted !!!")
    else:
        print(f"{delete_name} not found")
def main():
    while(True):
        print("""choose the task from below choice
              1.create contact
              2.read contact
              3.update contact
              4.delete contact""")
        choice=int(input("enter the choice:"))
        if choice==1:
            add_contact()
        elif choice==2:
            read_contact()
        elif choice==3:
            update_contact()
        elif choice==4:
            delete_contact()
        else:
            break
if __name__=="__main__":
    main()