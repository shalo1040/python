# 문자열을 입력 받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하여 표시해 보자.
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