# 다음 문제를 자바스크립트로 어떻게 풀까?

```
mystr 이라는 변수로 문자열이 입력된다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성하시오
```

|   INPUT    | OUTPUT |
| :--------: | :----: |
|   'aab'    |  'a'   |
| 'dfdefdgf' |  'df'  |
|   'bbaa'   |  'ab'  |

<br />

## My Solution

```js
function solution(mystr) {
  const counter = {};
  for (let i = 0; i < string.length; i++) {
    if (counter[string[i]]) {
      counter[string[i]]++;
    } else {
      counter[string[i]] = 1;
    }
  }

  const counterArray = Object.entries(counter);

  counterArray.sort((a, b) => b[1] - a[1]);

  const max = counterArray[0][1];
  const result = [];
  for (let i = 0; i < counterArray.length; i++) {
    if (max === counterArray[i][1]) {
      result.push(counterArray[i][0]);
    }
  }

  return result.sort().join('');
}
```

코드가 뭔가 난잡하다. 난잡하게 된 이유는 **최빈 알파벳**을 고르는 것과 최빈 알파벳이 여러 개인 경우 **알파벳 순서대로 정렬**하는 부분에서 코드가 많이 복잡해졌다. 하지만 중요한 부분은 객체 형식으로 각각의 알파벳의 빈도를 세는 부분이다. 객체를 만들어서 key는 알파벳, value는 빈도수를 적용하여 세는 방식으로 하면 조금 더 쉽고 간단하게 계산할 수 있다.
