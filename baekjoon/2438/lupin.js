var a = prompt('입력'); //n의 값을 받아준다
len = (2*a) //n의 두배를 받아내서 ++와 --의 별 값을 받아낸다
for (i=1;i<len;i++){//for문으로 별찍기 시작한다
    if(i<=a)//i 값이 a 까지 갔을때 결과값 집어넣기
        {
            for (j=0;j<i;j++)//결과값에 대해 * 찍기 개수가 많아지게
                {
                    document.write("*");
                    
                    
                }
            document.write('<br>');//찍은뒤 다음줄로
        }
    else
        {
            for (j=len;j>i;j--)//a 이후의 *찍기 개수가 적어지게
                {
                    document.write("*");
                    
                } 
            document.write('<br>');
        }
}