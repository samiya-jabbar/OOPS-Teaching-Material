# Source : Udacity

class Shirt():
  def __init__(self, a_color, a_size, a_price):
    self.color = a_color
    self.size = a_size
    self.price = a_price

  def change_color(self, new_color):
    self.color = new_color

  def discount(self, discount):    
    return self.price  - discount

created_shirt = Shirt('red', 'medium' , 50)
changed_color = created_shirt.change_color('orange')
offered_discount = created_shirt.discount(10)
print('shirt color:', created_shirt.color + '\nshirt size:' , created_shirt.size + '\noriginal price:', created_shirt.price)
print('after discount:' , offered_discount)

# UNIT TEST 
  
def run_tests(created_shirt):
 
    # Unit tests to check your solution
    assert created_shirt.price == 50, 'created_shirt price should be 40'
    assert created_shirt.color == 'orange', ' created_shirt should be red'
    assert created_shirt.size == 'medium', 'created_shirt size should be M'

run_tests(created_shirt)