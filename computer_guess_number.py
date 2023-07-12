import random

numbers = {
0: """" 
 0000
00  00
00  00
00  00
 0000   """,
1:"""
1111
  11
  11
  11
111111 """,
2:"""
 2222
22  22
   22
  22
222222 """,
3: """
 3333
33  33
   333
33  33
 3333 """,
4: """
44  44
44  44
444444
    44
    44 """,
5: """
555555
55
55555
    55
55555 """,
6: """
 6666
66
66666
66  66
 6666 """,
7: """
777777
   77
  77
 77
77 """,
8: """
 8888
88  88
 8888
88  88
 8888 """,
9: """
 9999
99  99
 99999
    99
 9999 """
}

def main():
    print("Think of a number from 1 to 10")
    lower = 1
    upper = 10
    result, number = guess(lower, upper)
    while result not in ['y', 'yes', 'correct', 'c']:
        if result in ['h', 'higher']:
            lower = number+1
            result, number = guess(lower, upper)
        elif result in ['lower', 'l']:
            upper = number-1
            result, number = guess(lower, upper)
        else:
            print("Invalid Input")
            result = input("Higher, Lower, Correct: ")

    print(f"\nYay! Your number is {number}")
    quit()


def guess(lower, upper):
    computer = random.randint(lower, upper)
    print(f"Is your number {computer}?")
    print(f"{numbers[computer]}", end="\n\n")
    feedback = input("Higher, Lower, Correct: ")
    return feedback, computer


if __name__ == "__main__":
    main()