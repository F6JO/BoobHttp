# BootHTTP

?	����BurpSuite��Intruder�������Զ��屬������

***

### ����˵��

?	�˹������� Burpsuite �� Intruder ģ�飬�����ٶ�Ҫ��һЩ�������ṩ���Զ�����Ժ���



### ����˵��

?	��Ҫ�طŵ����ݰ��������أ������ݰ���ʹ�� {{����}} ��ע�滻payload��λ�ã��磺{{0}}��{{1}} ��0��ʼ

?	��ÿ��Ҫ�滻λ�õ�payloads�ı��ľ���·�����浽ͳһ���ı��У��� -C ����ֵ��ָ�����ı�·��

?	��ȷ���

?		{{0}} �� payloads Ϊ D:/a.txt ��{{1}} �� payloadsΪ D:/b.txt ���� D:/a.txt �� D:/b.txt �ľ���·���� {{0}} {{1}} ��˳�򱣴��� D:/c.txt �У��� -C ������ָ�� D:/c.txt

?	ÿ��payloads�ļ��������Բ�һ���������������ϣ��������һ��������������ô���� Null �����-K ��������ָ���滻���ַ�

	#### �Զ������

?	��asse.py�ļ����ṩ�� Chu_li ����������Ӧ������ǰ�ᾭ���κ�������

?	����������������text Ϊ��Ӧ����lens Ϊ��Ӧ���ȣ�code Ϊ״̬�롣

?	�˺������뷵�ز���ֵ�������жϷ��������Ƿ�Ϊ��ȷ������

?	����True��Ὣ��payload���浽succeed.txt�ļ��С�



### ʾ��

?	python3 BoobHttp.py -r "D:/baopo.txt" -C mulu.txt

?	python3 BoobHttp.py -r "D:/baopo.txt" -C mulu.txt -o jieguo.txt

?	python3 BoobHttp.py -r "D:/baopo.txt" -C mulu.txt -q https 



### ���߽�ͼ

![Image text](https://github.com/F6JO/BoobHttp/blob/main/jingtai/qidong.jpg?raw=true)

![Image text](https://github.com/F6JO/BoobHttp/blob/main/jingtai/baocun.jpg?raw=true)





### ����˵��

-h, --help                          					   �鿴����

-q FANGFA                           				  �趨������http����https��Ĭ��http

-C CANSHU, --canshu CANSHU           ����payloads�����ļ���Ҫ���ļ�����ÿһ���滻λ�õ�payload�ļ�·��

-r QINGQIU                          				  ��ȡԭʼHTTP����ʹ��{{����}}�������滻��λ��,�磺{{0}}

-o BAOCUN                           				 ������־��·����Ҫ��txt�ļ���Ĭ��Ϊ��ǰĿ¼�µ�log.txt

-t XIANCHENG, --thread XIANCHENG  �趨���߳�����Ĭ��20

-m CHAOSHI, --time CHAOSHI             �趨ÿ������ʱʱ�䣬Ĭ��5

-c CHONGSHI, --chong CHONGSHI     �趨ÿ������ʧ�ܵ����Դ�����Ĭ��3

-F TIAOZHUAN, --tiao TIAOZHUAN      �趨��Ӧ�Ƿ������ת��Ĭ��False

-K KONG, --kong KONG                		��ȡ��һ�ļ������������滻���ַ���Ĭ��ΪNull

-p PRO, --pro PRO                   			  ���ô�����ʽ��http:127.0.0.1:7890��ע��û��//



