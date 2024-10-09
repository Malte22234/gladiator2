import random
print("Du är en gladiator utan vapen som ska slåss i en gladiator arena din motståndare gandalf är en mycket erfaren och farlig motståndare var försiktigt med honom. ")
spelarens_val=input("Välj mellan A,B och C för att attackera").lower()
if (spelarens_val=="a"):
    print("spelaren valde valde A")
elif (spelarens_val=="b"):
    print("spelaren valde B")
elif (spelarens_val=="c"):
    print("Spelaren valde C")

spelarens_hp=3

Gandalf1_hp=3

Gandalf1=random.randint(1, 3)
if (Gandalf1==1 and spelarens_val == "b"):
    print("Din motståndare valde attack A och du valde attack B. Du förlorar 1 hp.")
    spelarens_hp = spelarens_hp - 1
elif(Gandalf1==2 and spelarens_val == "a"):
    print("Din motsåndare valde attack b och dy valde attack a. Han förlorar 1 hp")
    robot_hp=Gandalf1_hp - 1
elif(Gandalf1==3 and spelarens_val == "c"):
    print("din motståndare valde attack c och du valde attack c. ingen tar skada")
elif(Gandalf1==2 and spelarens_val == "c"):
    print("din motståndare valde attack b och du valde attack c. han förlorar 1 hp ")
    Gandalf1=Gandalf1_hp - 1