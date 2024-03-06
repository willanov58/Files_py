# 1. show contacts
# 2. add contact
# 3. find contact
# 4. change contact
# 5. delete contact

#name number comm
    
 
def show_all(my_dict):
    for i in my_dict:
        print(i)


def add_contact():
    name=input("Print name: ")
    number=input("Print number: ")
    comm=input("Print comment: ")
    new_string=f'{name} {number} {comm}'
    my_dict.append({'name':name, 'number':number, 'comm':comm})
    with open('phone_numbers.txt', 'a+') as file:
        file.write(new_string)



def find_contact(my_dict):
    search_word=input("Print your text: ")
    search_result=[]
    for item in range(len(my_dict)):
        for i in my_dict[item].values():
            if search_word in i:
                search_result.append(item)
    print("Matches in indexes: ")
    print(search_result)
    return search_result



def change_contact(my_dict,index):
    fields=list(my_dict[0].keys())
    temp_dict=my_dict[index]
    to_change=int(input("What do you want to change?: 1.Name 2.Number 3.Commentary\n"))
    new_value=input("Print new value of field: ")
    temp_dict[fields[to_change-1]]=new_value
    my_dict[index]=temp_dict
    with open('phone_numbers.txt', 'w') as file:
        for i in my_dict:
            file.write(f'{i["name"]} {i["number"]} {i["comm"]}\n')

def delete_contact(my_dict,index):
    my_dict.pop(index)
    with open('phone_numbers.txt', 'w') as file:
        for i in my_dict:
            file.write(f'{i["name"]} {i["number"]} {i["comm"]}\n')

def copy_contact(my_dict,index,claim):
    fields=list(my_dict[0].keys())
    temp_dict=[]
    temp_dict.append(my_dict[index])
    with open(f'{claim}.txt', 'w') as file:
        for i in temp_dict:
            file.write(f'{i["name"]} {i["number"]} {i["comm"]}\n')
            
my_dict=[]
with open('phone_numbers.txt', 'r') as file:
    for i in file:
        my_list = i.split()
        my_dict.append({'name':my_list[0], 'number':my_list[1], 'comm':my_list[2]})


            
print("""\nChoose function:
1) show contacts
2) add contact
3) find contact
4) change contact
5) delete contact
6) copy contact
7) exit""")
while True:
        
        menu_item=int(input("choose function: "))
        if menu_item==1:
            show_all(my_dict)
        elif menu_item==2:
            add_contact()
        elif menu_item==3:
            find_contact(my_dict)
        elif menu_item==4:
            ind=int(input("Print the index of line that you want to change: "))
            change_contact(my_dict,ind)
        elif menu_item==5:
            ind=int(input("Print the index of line that you want to delete: "))
            delete_contact(my_dict,ind)
        elif menu_item==6:
            ind=int(input("Print the index of line that you want to copy: "))
            claim=str(input("Print name for the file where you want copy to: "))
            copy_contact(my_dict,ind,claim)

            
        elif menu_item==7:
            print("Program is dead")
            break

