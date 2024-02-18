#Challenge 1: Hurdle 1
def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

for step in range(6):
  jump()


#Challenge 2: Hurdle 2
def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

while not at_goal():
  jump()


#Challenge 3: Hurdle 3
def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

while not at_goal():
  if wall_in_front():
    jump()
  else:
    move()


#Challenge 4: Hurdle 4
def turn_right():
  turn_left()
  turn_left()
  turn_left()

def jump():
  turn_left()
  while wall_on_right():
    move()
  turn_right()
  move()
  turn_right()
  while front_is_clear():
    move()
  turn_left()

while not at_goal():
  if wall_in_front():
    jump()
  else:
    move()
