# zip() 정리

> zip()은 알아도 사용하지 못하는 파이썬의 함수라고 생각한다. ( 첫번째는 map() 🙄 ) 문제를 통해서 설명을 했지만, 다시 한 번 정리 해보고자 한다.

## Syntax

```python
  zip(*iterable)
```

각각의 iterable의 요소를 순서대로 하나씩 묶은 튜플 형태를 출력한다. 인자로 들어가는 iterable의 개수에 따라서 아래와 같이 분류될 수 있다.

## Example

1.  No arguments

    ```python
      zip()
    ```

    빈 값이 나오기 때문에 아무것도 출력되지 않는다.

2.  Single argument

    ```python
       numbers = [1, 2, 3, 4]

       for i in zip(numbers):
         print(i)
       # (1, ) (2, ) (3, ) (4, )
    ```

    요소가 한 개인 튜플 형식으로 출력된다.

3.  Multiple arguments of the same lengths

    ```python
       numbers = [1, 2, 3, 4]
       strings = ['a', 'b', 'c', 'd']

       for i in zip(numbers, strings):
         print(i)
       # (1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')
    ```

    일반적으로 zip()을 사용할 때를 나타낸다.

4.  Multiple arguments of different lengths

    ```python
      numbers = [1, 2]
      strings = ['a', 'b', 'c', 'd']

      for i in zip(numbers, strings):
        print(i)
      # (1, 'a'), (2, 'b')
    ```

    짧은 리스트를 기준으로 해서 zip이 이루어 진다. 하지만 <u>만약에 긴 리스트를 기준으로 zip하고 싶다면 어떻게 해야 할까?</u>

    ```python
      from itertools import zip_longest as zl
      numbers = [1, 2]
      strings = ['a', 'b', 'c', 'd']

      for i in zl(numbers, strings):
        print(i)
      # (1, 'a'), (2, 'b'), (None, 'c'), (None, 'd')
    ```

    itertools 모듈에서의 zip_longest() 메소드를 사용하면 위와 같이 긴 리스트를 기준으로도 zip이 가능해진다.

5.  Unzipping values

    ```python
      numbers = [1, 2, 3]
      strings = ['a', 'b', 'c']
      emojis = ['🔥','😀','🐶']

      zipped = zip(numbers, strings, emojis)
      z, y, z = zip(*zipped)
      print(x, y, z)

      # (1, 2, 3) ('a', 'b', 'c') ('🔥', '😀', '🐶')
    ```

    zip을 한 객체를 다시 zip을 하면 처음과 같은 값을 지니고 있는 튜플을 얻을 수 있다. ( zip을 2번 한 것! )

6.  Unpacking zipped value

    ```python
      numbers = [1, 2, 3]
      strings = ['a', 'b', 'c']
      emojis = ['🔥','😀','🐶']

      zipped = zip(numbers, strings, emojis)
      for x, y, z in zipped:
        print(x, y, z)

      # 1 a 🔥
      # 2 b 😀
      # 3 c 🐶
    ```

    생성된 zip객체의 요소를 unpacking하여 위와 같이 접근할 수 있다.
