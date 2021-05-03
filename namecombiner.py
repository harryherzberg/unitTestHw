import unittest

class NameCombiner:
  def __init__(self):
    self.firstname = ""
    self.lastname = ""
    self.fullname = ""
  def takeFirstname(self):
    filler = input ( "firstname: ")
    self.firstname = filler
  def takeLastname(self):
    filler2 = input ( "lastname: ")
    self.lastname = filler2
  def combine(self):
      self.fullname = str(self.firstname + " " + self.lastname)


class myTest(unittest.TestCase):

    #tests to see if you can input nothing for firstname/lastname
    def testEmpt(self):
        print("testing to see if either can be empty")
        name = NameCombiner()
        name.takeFirstname()
        name.takeLastname()
        self.assertNotEqual(name.firstname, "")
        self.assertNotEqual(name.lastname, "")
#tests to see if you can input a number for firstname/lastname
    def testAppend(self):
      print("testing to see if either can include numbers")
      name = NameCombiner()
      name.takeFirstname()
      name.takeLastname()
      for x in name.firstname:
          try: 
            x = int(x)
          except:
            x = x
          assert type(x) is str, "if you fail this then theres nothing preventing a number in your name"
      for x in name.lastname:
          try: 
            x = int(x)
          except:
            x = x
          assert type(x) is str, "if you fail this then theres nothing preventing a number in your name"
#          
#can you input a space in firstname / lastname? 

    def testIsInt(self):
        print("testing to see if either can include ' '")
        name = NameCombiner()
        name.takeFirstname()
        name.takeLastname()
        for x in name.firstname:
          self.assertNotEqual(x, ' ')
        for x in name.lastname:
          self.assertNotEqual(x, ' ')
try:
  if __name__ == '__main__':
    unittest.main()
except:
  print("error")
