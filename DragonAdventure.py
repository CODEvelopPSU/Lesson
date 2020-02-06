import time
print("Welcome to the Dragon Cave Adventure!")
time.sleep(2)
print("You awake inside a cave and see a dragon!")
time.sleep(2)
print("It looks like it's asleep...")
time.sleep(1)
print("You look for a way out. Maybe you could climb over the dragon's tail...")

choice1 = int(input("1 - Explore the cave more. 2 - Climb over the dragon's tail"))
if choice1 == 1:
  print("You feel around in the darkness, but you don't find anything useful.")
elif choice1 == 2:
  print("You try to gently climb over the dragon's tail, but it starts to move and growl. You back away.")

time.sleep(1)
print("The dragon shuffles, and you see an opening where you can squeeze by and escape the cave.")
time.sleep(2)
print("You hear a noise coming from your right.")
time.sleep(1)

choice2 = int(input("1 - Investigate the noise. 2 - Try to sneak past the dragon."))
if choice2 == 1:
  print("You go to investigate and the noise stops, but you see a strange light")
  time.sleep(1)
  choice3 = int(input("1 - Continue on. 2 - Head back."))
  if choice3 == 1:
    print("You get closer to the light and see that it's actually a passage to the outside. Hooray!")
  elif choice3 == 2:
    print("You turn around to go back...and see the dragon staring right at you.    GAME OVER")
elif choice2 == 2:
  print("Slowly tou edge past the dragon, careful not to make a sound.")
  time.sleep(2)
  print("You emerge from the cave and see a rescue party approaching you. Hooray!")


