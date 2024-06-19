#TO-DO List
class MyTodo:
  def __init__(self):
    self.todo=[]
  def add_task(self,task):
    self.todo.append({"Task":task,"Completed":"False"})
  def mark_task(self,index):
    if(0<= index <len(self.todo)):
      self.todo[index]["Completed"]="True"
      print("Marked true")
    else:
      print("ENTER CORRECT INDEX")
  def display_task(self):
    s=list(enumerate(self.todo))
    for i in s[0:]:
      print(i)
  def update_task(self,index,utask):
    if(index>=0 and index<len(self.todo)):
      self.todo[index]["Task"]=utask
      print("Task is being updated")
    else:
      print("ENTER CORRECT INDEX")
  def delete_task(self,index):
    if(index>=0 and index<len(self.todo)):
      self.todo.pop(index)
      print("Element is popped")
    else:
      print("ENTER CORRECT INDEX")
def main():
  obj=MyTodo()
  while(True):
    print("1. To add task")
    print("2. Mark task as Completed")
    print("3. Display task")
    print("4. Delete task")
    print("5. update task")
    print("6. Exit")
    choice=int(input("Enter choice: "))
    if(choice==1):
      a=input("Enter task: ")
      obj.add_task(a)
      obj.display_task()
    elif(choice==2):
      index=int(input("Enter index of task which is completed: "))
      obj.mark_task(index)
      obj.display_task()
    elif(choice==3):
      obj.display_task()
    elif(choice==4):
      index=int(input("Enter index of task which is to be deleted: "))
      obj.delete_task(index)
      obj.display_task()
    elif(choice==5):
      index=int(input("Enter index of task which is to be updated: "))
      utask=input("Enter updated task: ")
      obj.update_task(index,utask)
      obj.display_task()
    elif(choice==6):
      print("Exiting program!")
      break
    else:
      print("OOPS! Enter correct choice")
if __name__=="__main__":
  main()