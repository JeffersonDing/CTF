cube = 2739699434633097765008468371124644741923408864896396205946954196101304653772173210372608955799251139999322976228678445908704975780068946332615022064030241384638601426716056067126300711933438732265846838735860353259574129074615298010047322960704972157930663061480726566962254887144927753449042590678730779046154516549667611603792754880414526688217305247008627664864637891883902537649625488225238118503996674292057904635593729208703096877231276911845233833770015093213639131244386867600956112884383105437861665666273910566732634878464610789895607273567372933766243229798663389032807187003756226177111720510187664096691560511459141773632683383938152396711991246874813205614169161561906148974478519987935950318569760474249427787310865749167740917232799538099494710964837536211535351200520324575676987080484141561336505103872809932354748531675934527453231255132361489570816639925234935907741385330442961877410196615649696508210921
no_of_guesses = 0
#####
# GUESS AND CHECK 
####
# This only works for perfect cubes and
# also there will be more iterations for large numbers
for guess in range(abs(cube)+1):
  # passed all potential cube roots
  no_of_guesses +=1
  if guess**3 >= abs(cube):
        # no need to keep searching
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))
    print("number of guesses", no_of_guesses)
    
#######
# APPROXIMATE CUBE ROOT
#this method gets just a good enough answer
####
#cube = 10000
# does not find cube root of 10000. It skips the acceptable epsilon range 
epsilon = 0.1
guess = 0.0
increment = 0.01

# look for close enough answer and make sure
# didn't accidentally skip the close enough bound
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    no_of_guesses += 1
print('no if guesses =', no_of_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube, "with these parameters.")
else:
    print(guess, 'is close to the cube root of', cube)

#######
# Binary search
# This reduces the number of iterations by half in every pass
# the algorithm converges with complexity of log(base 2) n(search space)
######
#set precision
epsilon = 0.01
start = 0 
end = cube
guess = (start + end)/2.0

#
#check the error, i.e. difference between guess**3 and the given cube
#stop iterating when the error is acceptable, i.e. less than e
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        start = guess
    else:
        end = guess
    guess =  (start + end)/2.0
    no_of_guesses += 1
print("no of guesses", no_of_guesses)
print("cube root of", cube, "is", guess)


#   