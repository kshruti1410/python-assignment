""" Implementing generator """
def gen_number():
    """ checking number which is divided by both 5 and 7 """
    for num in range(INPUT_NUMBER):
        if num % 5 == 0 and num % 7 == 0:
            yield num

RESULT = ""
INPUT_NUMBER = int(input(" Enter number "))
for gen_num in gen_number():
   # print(gen_num, end=",")
    RESULT = RESULT+str(gen_num)+","

print(RESULT[ :-1])