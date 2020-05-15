"""
while문을 이용하여 아래와 같이 별(*)을 표시하는 프로그램을 작성해 보자.
*
**
***
****
"""
i = 1
while(i < 5):
    for k in range(i):
        print("*", end="")
    print()
    i+=1