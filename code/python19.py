str = input("문자열을 입력해주세요: ")
ans = ""
cnt = 1
for i in range(len(str)-1):
    if str[i]==str[i+1]:
        cnt += 1
    else:
        ans += str[i]
        ans += f'{cnt}'
        cnt = 1
ans += str[len(str)-1]
ans += f'{cnt}'
print(ans)