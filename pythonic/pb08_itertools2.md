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

> 위 풀이를 약간 업그레이드 시키면 아래와 같이 바꿀 수 있다.

```python
def solution(mylist):
  return sum(mylist, [])
```

이 풀이를 이해하려면 sum()메소드에 대해 조금 더 자세히 알아야 한다. `sum(a, b)` 메소드는 **두 개의 인자**를 받을 수 있다. 첫번째 인자는 **iterable 객체**이고 두번째 인자는 `시작값`을 나타낸다.

## pythonic solution

> solution1)

```python
import itertools

def solution(mylist):
  return itertools.chain(*mylist)

```

> solution2)

```python
import itertools

def solution(mylist):
  return itertools.chain.from_iterable(mylist)

```

chain() 과 chain.from_iterable()의 차이점은 인자로 들어갈 때, unpacking해주느냐 마냐의 차이가 있다.
