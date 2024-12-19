####################### DEBUGING ################################


##### STEP 1
# describe the problem
#Its not printing anything why because the range( starts from 1 to 20 but excluding 20 it never reaches 20 )
def myfunnction():
    for i in range(1, 21):
        if i == 20:
            print('You got it')
            
myfunnction()

##### STEP 2
# Reproduce the bug
# the error happpens when you try to access an index that xeceeds the number of items inside the list
from random import randint
dice_imgs = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣']
dice_num = randint(1, 5)
print(dice_imgs[dice_num])

###### Step 3 
# play computer


##### Step 4 
# Fix the error



##### Step 5
#print is your friend


##### Step 6
# use a debuger

#### Bonus tip
# take a break