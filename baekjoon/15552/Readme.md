백준 문제 풀이
=============
번호 15552
---------

> 주소 : https://www.acmicpc.net/problem/15552 <br>
> 언어 : JAVA 11

#### 1. 문제 풀이

기존 입력기능인 scanner 클래스와 System.out.println() 출력 기능을 사용하지 않고 BufferedReader 와 BufferedWriter을 사용해서 입출력하였다.

<br>

#### 2. 입력양식
<pre>
<code>
5 (출력할 개수)
1 1
2 3
4 5
6 2
1 3
</code>
</pre>

#### 3. 출력 양식
<pre>
<code>
2
5
9
8
4
</code>
</pre>

<pre>
<code>
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int numt = Integer.parseInt(br.readLine());
		
		for(int i=0;i<numt;i++) {
			st = new StringTokenizer(br.readLine());
			bw.write((Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken()))+"\n");
		}
		bw.flush();
		bw.close();
</code>
</pre>
