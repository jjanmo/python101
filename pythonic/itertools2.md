# Itertools2

## 문제

2차원 리스트를 1차원 리스트로 만들기

문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.

|              INPUT              |          OUTPUT           |
| :-----------------------------: | :-----------------------: |
|          [ [1], [2] ]           |          [1, 2]           |
| [['A', 'B'], ['X', 'Y'], ['1']] | ['A', 'B', 'X' ,'Y', '1'] |

## my solution

```python
def solution(mylist):
  result = []
  for sub in mylist:
    for i in sub:
      result.append(i)

  return result
```

> 위 풀이는 가장 일반적인 풀이이지 않을까 생각한다. 여기서 약간 파이썬스러운(?) 코드를 넣으면 이중for문을 돌지 않아도 된다. 그 풀이는 아래와 같다.

```python
def solution(mylist):
  result = []
  for sub in mylist:
      result += i

  return result
```

> 자바스크립트와는 다르게 파이썬에서의 리스트의 합은 리스트의 결합이 된다. 자바스크립트에 익숙한 나에겐 익숙하지 않은 부분이다.

## pythonic solution

>
