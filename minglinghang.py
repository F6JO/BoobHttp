#-*-coding:gb2312-*-
import argparse

def minglinghang():

    parser = argparse.ArgumentParser(description="BoobHttp")
    parser.add_argument("-q", dest='fangfa',help='设定请求是http还是https，默认http',default="http")
    parser.add_argument('-C', '--canshu', dest='canshu', help='设置payloads导航文件，要求文件内是每一个替换位置的payload文件路径')
    parser.add_argument("-r", dest='qingqiu',help='读取原始HTTP请求，使用{{数字}}来设置替换的位置,如：{{0}}')
    parser.add_argument('-o', dest='baocun', help='保存日志的路径，要求txt文件。默认为当前目录下的log.txt',default="log.txt",type=str)
    parser.add_argument('-t','--thread',dest='xiancheng',help='设定的线程数，默认20',default=20,type=int)
    parser.add_argument('-m','--time',dest='chaoshi',help='设定每个请求超时时间，默认5',default=5,type=int)
    parser.add_argument('-c','--chong',dest='chongshi',help='设定每个请求失败的重试次数，默认3',default=3,type=int)
    parser.add_argument('-F','--tiao',dest='tiaozhuan',help='设定响应是否跟随跳转，默认False',default=False,type=bool)
    parser.add_argument('-K','--kong',dest='kong',help='读取其一文件结束后用来替换的字符，默认为Null',default="Null")
    parser.add_argument('-p','--pro',dest='pro',help='设置代理，格式：http:127.0.0.1:7890，注意没有//',default=None)

    return parser.parse_args()