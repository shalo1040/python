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