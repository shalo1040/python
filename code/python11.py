# 1부터 1000까지의 자연수 중 3의 배수의 합을 구하세요
ans = 0
for i in range(1001):
    if(i%3==0):
        ans += i
print(ans)