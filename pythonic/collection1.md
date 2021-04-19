# Collection1

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

> 잠깐1! 여기서 궁금해지는 [자바스크립트 풀이](https://codesandbox.io/s/pb-tm9jc?file=/src/index.js) `⌗ 0422 디렉터리 collection1.js`

> 잠깐2 여기서 궁금해지는 [lambda](./lambda.md) 란?

### pythonix solution

```

```
