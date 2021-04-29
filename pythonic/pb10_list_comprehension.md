# List Comprehension

## 문제

mylist를 입력받아, 이 리스트의 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴하는 함수를 만드시오

|     INPUT      | OUTPUT  |
| :------------: | :-----: |
| [ 3, 4, 6, 7 ] | [4, 36] |

## my solution

```python
def solution(mylist):
    result = [];
    for i in mylist:
        if i % 2 == 0:
            result.append(i**2)
    return result
```

이번 문제는 아주 쉬운 문제이다. 위의 코드 처럼 반복문 안에 조건문을 넣어서 쉽게 해결할 수 있다. **B!U!T!** 쉬운 문제일수록 내가 배워가야 할, 알아가야 할 내용들이 많았다는 점을 상기하자 🔥

```python
def solution(mylist):
  return [ number ** 2 for i in mylist if number % 2 == 0 ]
```

파이썬에서는 조건문과 반복문을 한 줄로 처리할 수 있게 해주는 `list comprehension` 문법이다. 위의 코드처럼 한 줄로 표현할 수 있다. 원래 개념을 이해하기 위해선 그 단어의 뜻을 이해해야 하는데, `comprehension`은 이해, 표현등의 의미를 갖고 있다. 하지만 이러한 번역적인 의미로는 이 문법을 이해하는게 쉽지 않은 것 같다. 그냥 영어를 영어로 이해하고 이러한 문법을 `comprehension` 이라고 사용한다라는 것에 익숙해지는 것이 맞다고 생각한다. 또한 comprehension은 list 뿐만 아니라 set, dictionery에서도 사용된다. 다음 comprehension 파트에서 이러한 부분들을 조금은 깊이 있게(?) 다뤄보도록 하자.
