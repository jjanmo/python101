# Collection

## 문제

> 알고리즘 문제를 풀게되면 자주 접하게 되는 문제이다

```
mystr 이라는 변수로 문자열이 입력된다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성하시오
```

|   INPUT    | OUTPUT |
| :--------: | :----: |
|   'aab'    |  'a'   |
| 'dfdefdgf' |  'df'  |
|   'bbaa'   |  'ab'  |

### my solution

```python
import string
def solution(mystr):
  my_str = input().strip()
  alphabet_list = list(string.ascii_lowercase)

  result = []
  for c in alphabet_list:
      count = 0
      for i in my_str:
          if c == i:
              count =  count + 1
      result.append(count)

  sorted_list = sorted(zip(alphabet_list, result), key=lambda x:x[1], reverse=True)

  answer = ''
  max = sorted_list[0][1]
  for x in sorted_list:
      if max > x[1]:
          break
      elif max == x[1]:
          answer = answer + x[0]

  return answer
```

> 잠깐1! 여기서 궁금해지는 [자바스크립트 풀이](./pb09_collection2_js.md)

> 잠깐2 여기서 궁금해지는 [lambda](./lambda.md) 란?

### pythonic solution

```python
import collections

def solution(mystr):
  # step1
  counter = collections.Counter(mystr).most_common()

 # step2
  result = []
  max = counter[0][1]
  for item in counter:
    if max == item[1]:
      result.append(item[0])
    else:
      break

  # step3
  sorted_result = ''.join(sorted(result))

  return sorted_result
```

> 파이썬에서는 collections라는 모듈을 제공한다. 그 중에서 `Counter`를 사용하면 좀 더 간결하고 명시적인 코드를 구현할 수 있다. 이 Counter 클래스는 기존의 딕셔너리를 확장하고 있다.(subclass) 그렇기때문에 딕셔너리에서 사용할 수 있는 메소드를 그대로 가져와서 사용할 수 있다.

> `Counter(iterable or mapping)`으로 사용할 수 있다. 이 결과로 인자로 전달받은 요소가 key 값으로, 해당 요소의 개수가 value 값으로하여 새로운 딕셔너리 형태를 반환한다. 즉 위에서 우리가 개수를 세어서 만든 딕셔너리를 한 줄로 제공해주는 것이다. 더 나아가서 `most_common()`이라는 메소드는 반환값인 딕셔너리를 valeu 값에 따라서 최빈순으로 정렬하여 새로운 배열을 반환해준다. 단, 위의 정렬 순서는 <u>발견된 순서대로</u> 나오게 된다.

> example

```python
import collections

counter1 = collections.Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter1) # Counter({'blue': 3, 'red': 2, 'green': 1})
print(counter1.most_common()) # [('blue', 3), ('red', 2), ('green', 1)]

counter2 = collections.Counter('hello world')
print(counter2) # {'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print(counter2.most_common()) # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
```

이제 코드를 살펴보자. 3가지 단계로 나누어서 살펴보았다.

- Step1

  Counter를 사용하여 알파벳 개수의 최빈순으로 정렬된 배열을 얻을 수 있다.

- Step2

  최빈 알파벳이 1개인지 여러 개인지를 체크해주는 부분이다.

- Step3

  step2에서 고른 다시 알파벳 순으로 정렬해주는 부분이다.
