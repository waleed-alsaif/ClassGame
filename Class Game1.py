class Game:
   def __init__(self):
      print("Welcom In This Game.. ^_^")
      print("Choos Your Game"
            '\n'"press[1]: Play Even_Odd Game"
            '\n'"press[2]: Play Average Game"
            '\n'"press[3]: Play multiplication Game"
            '\n'"press[4]: Play Max_Min_Game Game")

      self.choices()
##################################################
   #### Choices Code
   def choices(self):
      while True:
         user_choices = input("Enter Yor Choices:")
         try:
            user_choices = int(user_choices)
            if user_choices == 1:
               self.Even_Odd_Game()
            elif user_choices == 2:
               self.Average_Game()
            elif user_choices == 3:
               self.multiplication_Game()
            elif user_choices == 4:
               self.Max_Min_Game()
            else:
               print("Please Choose Between 1,2 Or 3 ")
         except ValueError:
            print("Please Enter A Vaild Number")
            break

   ##################################################
   #### Even_Odd Code
   def Even_Odd_Game(self):
      print("Press 'X' for Exit Game")
      while True:
        num = input("Enter Any Number:")
        if num == 'x':
           break
        try:
           num=int(num)
           if num %2 == 0:
                print(num,"This Number is Even")
           else:
              print(num, "Theis Number Is Odd")
        except ValueError:
         print("Please Enter A Vaild Number")

   def Average_Game(self):
      while True:
         try:
            count=int(input("How Many Number Would You Like To Sum:"))
            curent_count = 0
            summ = 0
            while curent_count < count:
               number =float(input("Enter The Number:"))
               summ += number
               curent_count += 1
            print("The Tottal Number =",summ,'\n'"The Averge Number =",summ/count)
         except ValueError:
            print("Please Enter A Vaild Number")
            break


   def multiplication_Game(self):
      while True:
         try:
            count = int(input("How Many Number Would You Like To Multible:"))
            curent_count = 0
            multipl = 1
            while curent_count < count:
               number = float(input("Enter The Number:"))
               multipl *= number
               curent_count += 1
            print("The Tottal Number =", multipl)
         except ValueError:
            print("Please Enter A Vaild Number")
            break

   def Max_Min_Game(self):
      while True:
         try:
            intList = []
            number = int(input("Please enter the Total Number of List Elements: "))
            for i in range(1, number + 1):
               value = int(input("Please enter the Value of %d Element : " % i))
               intList.append(value)

            print('\n'"The Maximum Value in this List is : ", max(intList),
                  '\n'"The Maximum Value in this List is : ", min(intList))
         except ValueError:
            print("Please Enter A Vaild Number")
         break
game1 = Game()