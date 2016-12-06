#自我介绍 By 张可#

##性格

>外向：喜欢与人打交道。

>可靠：做一件事会尽力地完成它，注重细节。

##兴趣：

####美剧

> 从[越狱（Prison Break）](http://baike.baidu.com/subview/36434/5381066.htm) 开始，喜欢上了看美剧。
</br> 
> 暑假看完了 [绝命毒师（Breaking Bad）](http://baike.baidu.com/item/%E7%BB%9D%E5%91%BD%E6%AF%92%E5%B8%88) 真正让我震撼的一部美剧，一个高中化学老师走上制造毒品的道路。
</br> 
> 最近在看 [西部世界(Westworld)](http://baike.baidu.com/item/%E8%A5%BF%E9%83%A8%E4%B8%96%E7%95%8C/16357504)很有HBO的风格：尺度很大。讲述机器人觉醒反抗人类的故事，故事很吸引人。</br>

附上他们的百度网盘地址：</br>

>*  越狱 ：[百度网盘](http://pan.baidu.com/share/link?uk=3616157110&shareid=2123699771#list/path=%2F)</br>
*  绝命毒师：[百度网盘](http://pan.baidu.com/share/link?uk=2203926320&shareid=1645144288#list/path=%2F)</br>
*  西部世界：[百度网盘](http://pan.baidu.com/share/link?uk=220833725&shareid=3191095298#list/path=%2F)</br>

####知乎

闲来无事也会刷刷知乎

比较喜欢的几位用户：


>* [@王陶陶](https://www.zhihu.com/people/wang-tao-tao-91-97/answers)他对于美国大选以及国际形势的观点很精彩</br>
* [@vzch](https://www.zhihu.com/people/excited-vczh/answers) 轮子哥，人肉翻墙到美国的微软大神，职业带逛~</br>
* [@马前卒](https://www.zhihu.com/people/ma-qian-zu/answers)  军事历史哲学生物天文地理.......此君无所不通</br>

***

我学过一点C语言<br>
下面是我写过的一段C的代码,它能让你输入一个 年/月/日  后告诉你这是该年的第几天。

>例如输入： 1998/6/23 
>
>会输出  ： 174

<pre>

#include<stdio.h>
int main ()
{
    int a,b,c,h;
    char x,y;
    while (scanf("%d/%d/%d",&a,&b,&c)!=EOF)
   {
       int g=0;
      {
        if(((a%100==0)&&(a%400==0))||((a%100!=0)&&(a%4==0)))
            h=29;
        else
            h=28;
            //runnian
        for (int i=b;i>=1;i--)
        {
            if (i==b)
                g=g+c;
            else if(i==2)
                g=g+h;
            else if (i==1||i==3||i==5||i==7||i==8||i==10)
                g=g+31;
            else
                g=g+30;
        }
      }
    printf ("%d\n",g);
   }
    return 0;
}

</pre>
>
***
我的自我介绍先到这里，你们可以在以后的接触中进一步了解我。

![](http://ohr9krjig.bkt.clouddn.com/image/png%E8%AF%86%E5%BE%97%E5%94%94%E8%AF%86%E5%BE%97.png)
