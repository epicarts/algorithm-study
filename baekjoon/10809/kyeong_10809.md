백준 문제 풀이
=============
번호 10809
---------

> 주소 : https://www.acmicpc.net/problem/1110 <br>
> 언어 : JAVA 11
<br>

## 1. 문제 풀이방식

파일 이름 : num10809.java

```
int[] num_arr = new int[26];
        for(int i = 0; i<num_arr.length;i++){
            num_arr[i] = -1;
        }
```
26개의 정수 배열을 -1로 초기화
<br>
<br>
```
ArrayList<Integer> arr = new ArrayList<Integer>();
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] str_array;
        int count = 0;
        str_array = str.split("");
        
        for (String s : str_array) {
            arr.add((int)s.charAt(0)-97);
        }
```
문자열 입력 받고 문자를 소문자 'a'(97)을 뺀뒤 순서대로 arrayList에 추가
<br>
<br>
```
for(int i=0;i<arr.size();i++){
            if(num_arr[arr.get(i)]==-1){
                num_arr[arr.get(i)] = count;
            }
            count++;
        }

        for (int i : num_arr) {
            System.out.print(Integer.toString(i)+" ");
        }
```
중복값이 있을때 값을 넣으려고 할경우 이미 -1이 아닌 값은 데이터가 존재한다는 것이기에 -1 인 경우에만 count 값을 넣어주게끔 구현.
<br>
<br>

## 4. 문제 소감

- 정말 하다하다 반례도 많이 찾았고 어렵기도 했던 문제다. 도대체 결과가 나오는데 왜 틀렸다고하는지... 결국 컴퓨터는 거짓말을 하지않고 내 코드가 잘못됌을 다시 한번 깨닫는 시간이였다.
