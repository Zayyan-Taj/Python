# Your cat just had kittens! Now you want to put up an ad to give them
# to your friends. You'll need to save all names of the kittens,
# confirm that they each of them is cute, and show a message that
# that kitten is ready for adoption.
#
# Break this task up into a couple of steps of pseudocode
# and write the pseudocode below in code comments.
# You don't need to write any functional code, just map out the steps.

# Get the names of the kittens from the user
kitten_names = []
while True:
    name = input("Enter the name of a kitten (or 'done' to finish): ")
    if name.lower() == "done":
        break
    kitten_names.append(name)

# Ask the user if each kitten is cute
for name in kitten_names:
    cute = input(f"Is {name} cute? (yes/no): ")
    if cute.lower() == "yes":
        print(f"{name} is ready for adoption!")
    else:
        print(f"{name} is not ready for adoption.")