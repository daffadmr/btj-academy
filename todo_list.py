import json

def add_todo():
  note_name = input("Enter to do name: ")
  priority= input("Enter priority: ")

  new_note = {
    "name": note_name,
    "priority": priority,
    "status": "To do"
  }

  note_to_json = json.dumps(new_note)

  with open("todo_list.txt", "a") as file:
    file.write(note_to_json + "\n")

def view_todo():
  print("Your To Do List:")
  print("Name | Priority | Status")
  print("-"*25)

  finished_count = 0
  with open("todo_list.txt", "r") as file:
    todos = file.readlines()
    if len(todos) == 0:
        print("To do list is empty")
    for todo in todos:
      todo_temp = json.loads(todo)     
      print(f"{todo_temp["name"]} | {todo_temp["priority"]} | {todo_temp["status"]} ")
      if todo_temp["status"] == "Finished":
        finished_count += 1
    print()
    print(f"Progress To do anda: {finished_count/len(todos) * 100}%")

def view_todo_todo():
  print("Your To Do List:")
  print("Name | Priority | Status")
  print("-"*25)
  with open("todo_list.txt", "r") as file:
    todos = file.readlines()
    if len(todos) == 0:
      print("To do list is empty")
    for todo in todos:
      todo_temp = json.loads(todo)
      if todo_temp["status"] == "To do":
        print(f"{todo_temp["name"]} | {todo_temp["priority"]} | {todo_temp["status"]} ")

def view_todo_in_progress():
  print("Your To Do List:")
  print("Name | Priority | Status")
  print("-"*25)
  with open("todo_list.txt", "r") as file:
    todos = file.readlines()
    if len(todos) == 0:
      print("To do list is empty")
    for todo in todos:
      todo_temp = json.loads(todo)
      if todo_temp["status"] == "In progress":
        print(f"{todo_temp["name"]} | {todo_temp["priority"]} | {todo_temp["status"]} ")

def view_todo_finished():
  print("Your To Do List:")
  print("Name | Priority | Status")
  print("-"*25)
  with open("todo_list.txt", "r") as file:
    todos = file.readlines()
    if len(todos) == 0:
      print("To do list is empty")
    for todo in todos:
      todo_temp = json.loads(todo)
      if todo_temp["status"] == "Finished":
        print(f"{todo_temp["name"]} | {todo_temp["priority"]} | {todo_temp["status"]} ")
    
def delete_todo():
  view_todo()

  delete_choice = input("Which to do you want to delete? (The name of to do): ")

  with open("todo_list.txt", "r") as file:
    todos = file.readlines()
    for todo in todos:
      todo_temp = json.loads(todo)
      if todo_temp["name"] == delete_choice:
        todos.remove(todo)
  
    with open("todo_list.txt", "w") as new_file:
      new_file.writelines(todos)
  
  view_todo()
    
def update_todo():
  view_todo()
  update_choice = input("Which to do you want to update? (The name of to do): ")

  with open("todo_list.txt", "r") as file:
    temp_todolist = []
    todos = file.readlines()
    for todo in todos:
      todo_temp = json.loads(todo)
      if todo_temp["name"] == update_choice:
        print("What progress?")
        print("1. To do")
        print("2. In progress")
        print("3. Finished")
        status = input("Enter the number: ")

        if status == "1":
          if todo_temp["status"] == "To do":
            print("Your to do already on To do status")
            break
          else:
            todo_temp["status"] = "To do"
        elif status == "2":
          if todo_temp["status"] == "In progress":
            print("Your to do already on In progress status")
            break
          else:
            todo_temp["status"] = "In progress"
        elif status == "3":
          if todo_temp["status"] == "Finished":
            print("Your to do already on Finished status")
            break
          else:
            todo_temp["status"] = "Finished"
        else:
          print("Wrong input!")

      temp_todolist.append(json.dumps(todo_temp) + "\n")

      with open("todo_list.txt", "w") as new_file:
        new_file.writelines(temp_todolist)
  
  view_todo()

while True:
  print("\nMenu:")
  print("1. Add to do")
  print("2. View to do (All progress)")
  print("3. View to do (To do)")
  print("4. View to do (In progress)")
  print("5. View to do (Finished)")
  print("6. Delete to do")
  print("7. Change to do status")
  print("8. Exit")
  
  pilihan = input("Enter your choice (1-8): ")

  if pilihan == "1":
    add_todo()
  elif pilihan == "2":
    view_todo()
  elif pilihan == "3":
    view_todo_todo()
  elif pilihan == "4":
    view_todo_in_progress()
  elif pilihan == "5":
    view_todo_finished()
  elif pilihan == "6":
    delete_todo()
  elif pilihan == "7":
    update_todo()
  elif pilihan == "8":
    exit()
  else:
    print("Wrong input!")