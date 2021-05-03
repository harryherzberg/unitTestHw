import unittest

class Cube:
  def __init__(self):
    self.volume = 0
    self.length = 0
  def takeDimensions(self):
    self.length = int( input( "what number needs to be cubed: ") )
  def cubeMe(self):
    self.volume = self.length*self.length*self.length
  def printVol(self):
    print(self.volume)


class TestStringMethods(unittest.TestCase):
    #tests to see if an actual cube works (should pass)
    def testCubing(self):
        myCube = Cube()
        myCube.length = 3
        myCube.cubeMe()
        self.assertEqual(myCube.volume, 27)
#tests to see if theres a negitive number in length (should fail)
    def testNegative(self):
        myCube = Cube()
        myCube.length = -3
        myCube.cubeMe()
        self.assertGreater(myCube.length, 0, "if you fail this then you have no way of insuring that cublength is greater than 0, id reccomend something that checks it in the function 'cubeMe'")
        
#tests to see if theres a string or non int in length (should fail)
    def testIsInt(self):
        myCube = Cube()
        myCube.length = "notAnInt"
        assert type(myCube.length) is int, "if you fail this then you can set length to anything, i would reccomend enforcing getters and setters for cube, takeDimensions also needs to ensure that it is only grabbing an int."

try:
  if __name__ == '__main__':
    unittest.main()
except:
  print("an error occured")
