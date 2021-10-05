백준 문제 풀이
=============
번호 11022
---------

> 주소 : https://www.acmicpc.net/problem/11022 <br>
> 언어 : JAVA 11
#### 1. 문제 풀이

기존 입력기능인 scanner 클래스와 System.out.println() 출력 기능을 사용하지 않고 BufferedReader 와 BufferedWriter을 사용해서 입출력하였다.

<br>

#### 2. 입력양식
<pre>
<code>
5
1 1
2 3
3 4
9 8
5 2
</code>
</pre>

#### 3. 출력 양식
<pre>
<code>
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
</code>
</pre>

### 4. 핵심 코드

<pre>
<code>
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		String str="";
		int num1 = 0;
		int num2 = 0;
		int sum = 0;
		int num = Integer.parseInt(br.readLine());
		for(int i=1;i<num+1;i++) {
			st = new StringTokenizer(br.readLine());
			num1 = Integer.parseInt(st.nextToken());
			num2 = Integer.parseInt(st.nextToken());
			sum = num1+num2;
			str = "Case #"+i+": "+num1+" + "+num2+" = ";
			bw.write(str);
			bw.write(sum+"\n");
		}
		bw.flush();
		br.close();
		bw.close();
</code>
</pre>
