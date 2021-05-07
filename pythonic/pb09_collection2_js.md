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

## sort()에 대해서 알아보자

```
array.sort([compareFunction])
```

sort() 메소드는 위에 처럼 사용한다. 인자로 들어가는 `compareFunction`은 선택사항이다. 기본적으로 sort() 메소드가 작동하는 방식은 <u>각 요소가 문자열로 변환되어서 문자의 유니코드 값에 따라서 정렬</u>된다. 또한 기본 정렬방식은 **오름차순**이다. 만약에 인자로 <u>compareFunction가 들어간다면 그 방식에 따라서 정렬</u>된다. 또한 중요한 포인트는 sort()가 작동하면 원배열의 정렬을 바꾸게 된다. **복사본이 만들어지는 것이 아니다.**

<br />

```js
const movies = ['Prison Break', 'Designated Survivor', 'Double Target', 'Green Zone'];

movies.sort();
// ["Designated Survivor", "Double Target", "Green Zone", "Prison Break"]

const numbers = [77, 101, 23, 4, 18];
numbers.sort();
// [101, 18, 23, 4, 77]
```

> 기본적으로 배열의 요소가 문자열일 때는 알파벳 순서를 기준으로 정렬이 된다. 배열의 요소가 숫자일 때 역시 그 숫자를 문자열로 변환하여 비교한 후 정렬이 이루어진다.

<br />

```js
const numbers = [77, 101, 23, 4, 18];
numbers.sort((a, b) => a - b); // ascending : [4, 18, 23, 77, 101]
numbers.sort((a, b) => b - a); // descending : [101, 77, 23, 18, 4]
```

> 숫자로서 비교하기 위해선 위의 코드처럼 compareFunction를 구현할 수 있다. 왜 이와 같이 표현이 가능하게 되는지 compareFunction에 대해서 알아보자.

> **compareFunction의 반환값**에 따라서 정렬이 이루어진다. compareFunction(a, b)의 값이 양수이면 a가 b보다 큰 인덱스로 정렬한다. 반대로 compareFunction(a, b)의 값이 음수이면 a가 b보다 작은 인덱스로 정렬한다. compareFunction(a, b)의 값이 0이면 둘은 서로에 대해서 변경되지 않고 다른 요소를 기준으로 정렬된다.

```js
// ascending 오름차순
function compare(a, b) {
  if (a > b) {
    return 1;
  } else if (a < b) {
    return -1;
  } else {
    return 0;
  }
}

//descending 내림차순
function compare(a, b) {
  if (a > b) {
    return -1;
  } else if (a < b) {
    return 1;
  } else {
    return 0;
  }
}
```

<br />

> 위에서 설명한 compareFunction 함수의 형식에 따라서 조건을 잘 구현하면 배열 안에 객체를 조건에 맞게 정렬시킬 수 있다. 참고로 위 내용은 숫자로서을 정렬할 때만 사용하는 것이 아니라 정렬할 때의 compareFunction의 기본 개념이다.

```js
const coins = [
  { symbol: 'ETC', price: 159700 },
  { symbol: 'DOGE', price: 718 },
  { symbol: 'BTT', price: 10.1 },
  { symbol: 'LTC', price: 425500 },
  { symbol: 'BCH', price: 1688000 },
];

// 가격에 따라서 오름차순 정렬
coins.sort((a, b) => {
  if (a.price > b.price) return 1;
  else if (a.price < b.price) return -1;
  else return 0;
});

/*
OUTPUT
[
  {symbol: "BTT", price: 10.1},
  {symbol: "DOGE", price: 718},
  {symbol: "ETC", price: 159700},
  {symbol: "LTC", price: 425500},
  {symbol: "BCH", price: 1688000}
]
*/

// 이름에 따라서 오름차순 정렬
coins.sort((a, b) => {
  if (a.symbol > b.symbol) return 1;
  else if (a.symbol < b.symbol) return -1;
  else return 0;
});

/*
OUTPUT
[
  {symbol: "BCH", price: 1688000},
  {symbol: "BTT", price: 10.1},
  {symbol: "DOGE", price: 718},
  {symbol: "ETC", price: 159700},
  {symbol: "LTC", price: 425500}
]
*/
```

<br />

### Q. 배열 안의 객체를 두가지 요소(프로퍼티)에 의해서 정렬할 수 있을까?

아래 배열을 나이에 의한 내림차순으로 정렬한다. 만약 같은 나이인 경우, 닉네임에 의한 오름차순(알파벳 순서)으로 정렬한다.

```js
const students = [
  { nickname: 'jjanmo', age: 22 },
  { nickname: 'xxxyyyzzz', age: 14 },
  { nickname: 'freeMAN', age: 33 },
  { nickname: 'maxie', age: 7 },
  { nickname: 'DOGEboy', age: 14 },
];
```

<details>
<summary>정답 코드 보기</summary>
<div markdown="1">

```js
students.sort((a, b) => {
  if (a.age > b.age) return -1;
  else if (a.age < b.age) return 1;
  else {
    if (a.nickname > b.nickname) return 1;
    else if (a.nickname < b.nickname) return -1;
    else return 0;
  }
});

/*
OUTPUT
[
  {nickname: "freeMAN", age: 33},
  {nickname: "jjanmo", age: 22},
  {nickname: "DOGEboy", age: 14},
  {nickname: "xxxyyyzzz", age: 14},
  {nickname: "maxie", age: 7},
]
*/
```

> 나이를 비교하여 정렬한 후(if, else if), 같은 나이인 경우(else) 다시 닉네임을 비교하여 정렬한다.

> 문자열을 비교할 때는 대소문자를 구분한다. 만약 `{ nickname: 'daredevil', age: 14 }` 요소가 추가로 들어간다면 순서가 어떻게 될지 생각해보자.

```js
/*
OUTPUT
[
  {nickname: "freeMAN", age: 33},
  {nickname: "jjanmo", age: 22},
  {nickname: "DOGEboy", age: 14},
  {nickname: "daredevil", age: 14},
  {nickname: "xxxyyyzzz", age: 14},
  {nickname: "maxie", age: 7},
]
*/
```

</div>
</details>

<br />
<br />

**참고**

아래와 같이 표현할수 도 있다.

먼저, 학년에 의한 오름차순 정렬한다. 같은 학년인 경우 이름에 의한 오름차순으로 정렬한다.

```js
const students = [
  { name: 'Tom', grade: 1 },
  { name: 'Brown', grade: 3 },
  { name: 'Michael', grade: 3 },
  { name: 'Jassie', grade: 2 },
  { name: 'Jason', grade: 1 },
];

students.sort((a, b) => {
  const keyA = a.grade + a.name;
  const keyB = b.grade + b.name;
  if (keyA > keyB) return 1;
  else if (keyA < keyB) return -1;
  return 0;
});

/*
OUTPUT
[
  { name: "Jason", grade: 1 }
  { name: "Tom", grade: 1 },
  { name: "Jassie", grade: 2 },
  { name: "Brown", grade: 3 },
  { name: "Michael", grade: 3 },
]
*/
```

> 위 코드처럼 두가지 조건에 따라서 정렬 시킬 수 있다. 사실 위처럼 객체의 요소를 합쳐서 하나의 키로 만드는 방법은 이번에 처음 알게 되었다. 하지만 이렇게 사용하기 위해선 몇 가지 조건이 필요하다. 첫번째는 두가지 조건에 따른 정렬 방식이 같아야한다. 즉 모두 오름차순이거나 내림차순이여야 한다. 두번째는 문자열로 비교로 순서를 유지할 수 있어야 한다. 위의 예처럼 학년은 숫자로 비교를 하든 문자열로 비교를 하든 같은 정렬을 갖을 수 있는 경우를 말한다.
