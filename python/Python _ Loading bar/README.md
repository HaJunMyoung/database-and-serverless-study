# Python: Loading bar | 파이썬: 로딩 바
이곳은 파이썬으로 만들어진 몇 개의 로딩 바가 저장된 곳입니다.  
각각의 타입은 다른 유형의 로딩을 보여줍니다.

Some types of Loading bar written by Python are save here.  
Each type shows another expression of Loading bar.

# Naming | 이름 짓기
로딩 바 파일들은 다음과 같은 규칙으로 이름 지어졌습니다.  
Loading bar files are named by following this:

**LB** : **L**oading **B**ar, Main category | 대분류  
**Number** : Type No. | 타입번호  
**Character(문자)** : For distinguishing similar type | 비슷한 타입을 구분하기 위한 문자  

## LB01A_feeling squares
output:
```
#처음
□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□

#과정(20%)
■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□

#마지막
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
```

### Keypoints 키포인트
핵심: □를 ■로 **대체하는**효과를 주기 위해, *캐리지 리턴*(이스케이프 코드 `\r`)을 사용했습니다.
>'캐리지 리턴'이 무엇인가요?  
> 캐리지 리턴은, 커서를 맨 앞으로 옮기는 이스케이프 코드입니다.  
> `\n`이 줄바꿈을 하는 리턴인것처럼, `\r`은 커서를 앞으로 옮기는 역할을 하죠.  


Point: For **replacing** □ to ■, I used *carage return*(escape code: `\r`)
>What is 'carage return'?  
> Carage return is an escape code that moves the Cursor to front.  
> Just like escape code `\n` makes new line, `\r` moves the cursor to front.  

### Errors 에러
`print()`를 사용하여 로딩 바를 출력할 때, 꼭 `print("내용", end='')` 작성해주어야 합니다.  
When use `print()`, you should write that like this: `print("contents", end='')`

중요한 것은, **end=''** 를 추가하는 것입니다.  
이 코드는 print()가 내용을 출력하고 자동으로 하는 줄바꿈을 무효화시킵니다. ''로 끝내라고 알려주는 것이죠.  
만약 **end=''** 를 하지 않는다면, 줄바꿈이 되고 캐리지 리턴이 적용되어, *피라미드*를 보게 될 것입니다.

Adding **end=''** is important.  
print() end the sentence with '\n' autonomically. But if you use this, you can specify the end as ''.  
If don't, you can see a *pyramid*

## LB02A_feeling dash
output:
```
[--------------------------------------------------] 0%
[##########----------------------------------------] 20%
[##################################################] 100%
```
LB01A와 상당 부분 유사하므로(문자의 종류를 바꾸어 로딩의 의미를 나타내는 표현 방식이) Keypoints와 Errors는 생략합니다.

- - -
last update: 1/10/2020