class toyfactory:
  def __init__(self):
    print("A new is made")
  def __del__(self):
    print("A toy is destroyed")

#object creation
def make_toy():
    print("Making a toy!!!!!!")
    toy = toyfactory()
    print("Toy is ready")
    return toy
  
print("Starting the toy factory!!")
toy = make_toy()
print("factory is closing!!")