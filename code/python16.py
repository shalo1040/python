#	입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자. (단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg(sum, cnt):
    return sum/cnt

sum = 0
cnt = 0

while(1):
    x = int(input())
    if x != -1:
        sum += x
        cnt += 1
    else:
        break

print(avg(sum,cnt))