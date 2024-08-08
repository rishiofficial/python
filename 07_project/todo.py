
# todo = []

# def add_todo_list():
#     todo = input("Enter the ToDO: ")
#     return f"todo: {todo}"

# print(add_todo_list())
import json

def load_data():
    try:
       with open('todo.txt','r' ) as file:
         test = json.load(file)
         return test
    except FileNotFoundError:
      return []
    
def save_todo(todos):
    with open ("todo.txt",'w') as file:
          json.dump(todos,file)
        

def list_of_all_todo(todos):
    for index,todo in enumerate(todos,start=1):
        print(f"{index}. {todo}")
    

def add_todo_list(todos):
    todo = input("Enter the todo: ")
    todos.append({'todo:': todo})
    save_todo(todos)

def update_todo(todos):
    list_of_all_todo(todos)
    index = int(input("Enter the index of the todo: "))
    if 1<= index <= len(todos):
        todo = input("Update this todo: ")
        todos[index-1] = ({"todo ": todo})
        save_todo(todos)
    else:
        print("Invalid syntax")


def delete_todo(todos):
    list_of_all_todo(todos)
    index = int(input("Enter the index of the todo to delete: "))
    if 1<= index <= len(todos):
       del todos[index-1]
       save_todo(todos)
    else:
        print("Invalid index")


def main():
    todos = load_data()
    while True:
        print("\n A TODO App ")
        print("1.List of all todo")
        print("2.Add the todo")
        print("3.Update the todo")
        print("4.Delete the todo")
        print("5.Exit your app")
        choice= input("Enter your choice: ")

        match choice:
            case '1':
                list_of_all_todo(todos)
            case '2':
                add_todo_list(todos)
            case '3':
                update_todo(todos)
            case '4':
                delete_todo(todos)
            case '5':
                break
            case '_':
                "Invalid choice"

if __name__ == "__main__":
    main()