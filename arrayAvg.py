import unittest

class List:
  def __init__(self):
    self.arry = []
    self.avg = 0
  def append(self):
    filler = int( ( "what number needs to be appended: ") )
    self.arry.append(filler)
  def avgMe(self):
    if len(self.arry) == 0:
      self.avg = -1
      return
    self.avg = sum(self.arry)/len(self.arry)
  def printAvg(self):
    print(self.avg)


class myTest(unittest.TestCase):
    #tests to see if an actual array works (should pass)
    def testAvg(self):
        myArr = List()
        myArr.arry.append(1)
        myArr.arry.append(2)
        myArr.arry.append(3)
        myArr.avgMe()
        self.assertEqual(myArr.avg, 2)
#can A list have no elements and still get avgd (should fail )
    def testAppend(self):
      myArr = List()
      self.assertGreater(len(myArr.arry), 0, "if you fail this then there is nothing that ensures that myArr len has to be greater than 0")
        
#can I append a string to the list? (should fail)

    def testIsInt(self):
        myArr = List()
        myArr.arry.append(1)
        myArr.arry.append("notAnInt")
        #myArr.arry.append("3")
        myArr.arry.append(1)
        myArr.arry.append(1)
        for x in range(len(myArr.arry)):
          assert type(myArr.arry[x]) is int, "if you fail this then theres nothing preventing a string in the arry"

try:
  if __name__ == '__main__':
    unittest.main()
except:
  print("gay")
