#-*-coding:gb2312-*-
import argparse

def minglinghang():

    parser = argparse.ArgumentParser(description="BoobHttp")
    parser.add_argument("-q", dest='fangfa',help='�趨������http����https��Ĭ��http',default="http")
    parser.add_argument('-C', '--canshu', dest='canshu', help='����payloads�����ļ���Ҫ���ļ�����ÿһ���滻λ�õ�payload�ļ�·��')
    parser.add_argument("-r", dest='qingqiu',help='��ȡԭʼHTTP����ʹ��{{����}}�������滻��λ��,�磺{{0}}')
    parser.add_argument('-o', dest='baocun', help='������־��·����Ҫ��txt�ļ���Ĭ��Ϊ��ǰĿ¼�µ�log.txt',default="log.txt",type=str)
    parser.add_argument('-t','--thread',dest='xiancheng',help='�趨���߳�����Ĭ��20',default=20,type=int)
    parser.add_argument('-m','--time',dest='chaoshi',help='�趨ÿ������ʱʱ�䣬Ĭ��5',default=5,type=int)
    parser.add_argument('-c','--chong',dest='chongshi',help='�趨ÿ������ʧ�ܵ����Դ�����Ĭ��3',default=3,type=int)
    parser.add_argument('-F','--tiao',dest='tiaozhuan',help='�趨��Ӧ�Ƿ������ת��Ĭ��False',default=False,type=bool)
    parser.add_argument('-K','--kong',dest='kong',help='��ȡ��һ�ļ������������滻���ַ���Ĭ��ΪNull',default="Null")
    parser.add_argument('-p','--pro',dest='pro',help='���ô�����ʽ��http:127.0.0.1:7890��ע��û��//',default=None)

    return parser.parse_args()