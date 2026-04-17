# student manager application '
students = []

# add student 
def add_student():
      name = input('enter your name : ')
      roll = int(input('enter your roll number :'))
      course = input('enter your course: ')
      
      student = {
            'name':name,
            'roll no ':roll,
            'course':course
      }
      students.append(student)
      print('\n student added succesfully ! \n')
      
# view students
def view_student():
      if len(students) == 0:
            print('\n No Student Found ! \n')
            return
      
      print('\n students list \n')
      print('-'*40)
      for i , student in enumerate(students,start=1):
            print(f'{i}.name : {student['name']}')      
            print(f'roll no  : {student['name']}')      
            print(f'course : {student['name']}') 
            print('-'*40)
            
# delete student
def delete():
      if len(students) == 0 :
            print('\n no student Found ! \n ')
            return
      view_student()
      try:
            index = int(input('enter the student number to delete : '))
            if 1<= index <= len(students):
                  removed = students.pop(index-1)
                  print(f'\n removed name : {removed['name']} succesfully ')
            else:
                  print(f'\n invalid number : !')
                  
      except ValueError:
            print(f'please enterthe valid number !')
            
# main function 
def main():
      while True:
            print('\n Student Manager System \n')
            print('1.add student')
            print('2.view student')
            print('3.delete student')
            print('4.exit')
            
            choice = int(input('\n enter your choice : (1-4)\n '))
            
            if choice == 1:
                  add_student()
            elif choice == 2:
                  view_student()
            elif choice == 3:
                  delete()
            elif choice == 4:
                  print('\n exit good bye ! ')
                  break
            else:
                  print('\n invalid choice try agian ! \n')
                  
main()
            
            
                 

      
      