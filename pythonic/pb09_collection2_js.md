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

## Solution

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

코드가 뭔가 난잡하다.😭 난잡하게 된 이유는 **최빈 알파벳**을 고르는 것과 최빈 알파벳이 여러 개인 경우 **알파벳 순서대로 정렬**하는 부분에서 코드가 많이 복잡해졌다. 하지만 **중요한 부분은 객체 형식으로 각각의 알파벳의 빈도를 세는 부분**이다. 객체를 만들어서 key는 알파벳, value는 빈도수를 적용하여 세는 방식으로 하면 조금 더 쉽고 간단하게 계산할 수 있다.

<br/>

## 풀이 순서 요약

1. 문자열을 순회하며 같은 글자의 개수를 세어서 객체 형태로 `알파벳 : 개수` 형태로 만든다.
2. (객체는 정렬할 수 없기 때문에) 객체를 배열 형태로 변환하여 `개수의 내림차순`으로 정렬한다.

   > `Object.entries(해당 object)` 는 객체의 요소를 각각 [ key, value ] 형태로 담은 배열을 반환한다.

3. 배열 안에서 `가장 많은 개수의 알파벳`을 선택하여 반환한다. (1개일 수도 여러 개일 수도 있다)

<br />

## Upgrade Version

위 풀이를 보면 자바스크립트의 Array 메소드를 남발(?)하는 것을 볼 수 있었다. 답은 나오지만 깔끔하지 못한 느낌이 많이 들었다. 그래서 좀 더 깔끔하고 명시적인 방법이 뭐가 있을지에 대해서 찾아보게 되었다. 그 결과 아래와 같이 바꿀 수 있었다.

```js
function solution(string) {
  //1번 코드뭉치
  const counter = {};
  for (let i = 0; i < string.length; i++) {
    if (counter[string[i]]) {
      counter[string[i]]++;
    } else {
      counter[string[i]] = 1;
    }
  }

  //2번 코드뭉치
  const counterArray = Object.entries(counter);
  counterArray.sort((a, b) => {
    if (a[1] > b[1]) {
      return -1;
    } else if (a[1] < b[1]) {
      return 1;
    } else {
      if (a[0] > b[0]) {
        return 1;
      } else {
        return -1;
      }
    }
  });

  //3번 코드뭉치
  const max = counterArray[0][1];
  let result = counterArray[0][0];
  for (let i = 1; i < counterArray.length; i++) {
    if (max === counterArray[i][1]) {
      result += counterArray[i][0];
    }
  }

  return result;
```

위 코드를 보면 코드뭉치(?)별로 하는 일이 좀 더 명확해졌다. **1번 코드뭉치** 문자열을 순회하면서 같은 알파벳 개수를 세어서 객체 형태로 만들어준다. **2번 코드 뭉치**는 정렬하는 부분이다. 여기서는 2가지 정렬을 한 번에 처리한다.(정렬 기준이 2가지 이다.) 알파벳 개수가 많은 순으로 정렬한 후 개수가 같은 경우 알파벳 순으로 다시 정렬하게 된다. 이를 sort()를 좀 더 명료하게(?) 사용하여 구현하였다. **3번 코드뭉치**는 같은 알파벳 개수가 가장 큰 알파벳을 고르는 부분이다.

<br />
