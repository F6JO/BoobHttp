# BootHTTP

?	类似BurpSuite的Intruder，用于自定义爆破请求

***

### 工具说明

?	此工具类似 Burpsuite 的 Intruder 模块，但是速度要快一些，并且提供了自定义断言函数



### 操作说明

?	将要重放的数据包保存下载，在数据包内使用 {{数字}} 标注替换payload的位置，如：{{0}}，{{1}} 从0开始

?	将每个要替换位置的payloads文本的绝对路径保存到统一的文本中，在 -C 参数值中指定此文本路径

?	打比方：

?		{{0}} 的 payloads 为 D:/a.txt ，{{1}} 的 payloads为 D:/b.txt ，将 D:/a.txt 与 D:/b.txt 的绝对路径按 {{0}} {{1}} 的顺序保存在 D:/c.txt 中，在 -C 参数中指定 D:/c.txt

?	每个payloads文件数量可以不一样，按照最长数量组合，如果其中一个遍历结束，那么会用 Null 替代。-K 参数可以指定替换的字符

	#### 自定义断言

?	在asse.py文件中提供了 Chu_li 函数，在响应被处理前会经过次函数处理。

?	其中有三个参数，text 为响应包，lens 为响应长度，code 为状态码。

?	此函数必须返回布尔值，用来判断返回内容是否为正确的内容

?	返回True则会将此payload保存到succeed.txt文件中。



### 示例

?	python3 BoobHttp.py -r "D:/baopo.txt" -C mulu.txt

?	python3 BoobHttp.py -r "D:/baopo.txt" -C mulu.txt -o jieguo.txt

?	python3 BoobHttp.py -r "D:/baopo.txt" -C mulu.txt -q https 



### 工具截图

![Image text](https://github.com/F6JO/BoobHttp/blob/main/jingtai/qidong.jpg?raw=true)

![Image text](https://github.com/F6JO/BoobHttp/blob/main/jingtai/baocun.jpg?raw=true)





### 参数说明

-h, --help                          					   查看帮助

-q FANGFA                           				  设定请求是http还是https，默认http

-C CANSHU, --canshu CANSHU           设置payloads导航文件，要求文件内是每一个替换位置的payload文件路径

-r QINGQIU                          				  读取原始HTTP请求，使用{{数字}}来设置替换的位置,如：{{0}}

-o BAOCUN                           				 保存日志的路径，要求txt文件。默认为当前目录下的log.txt

-t XIANCHENG, --thread XIANCHENG  设定的线程数，默认20

-m CHAOSHI, --time CHAOSHI             设定每个请求超时时间，默认5

-c CHONGSHI, --chong CHONGSHI     设定每个请求失败的重试次数，默认3

-F TIAOZHUAN, --tiao TIAOZHUAN      设定响应是否跟随跳转，默认False

-K KONG, --kong KONG                		读取其一文件结束后用来替换的字符，默认为Null

-p PRO, --pro PRO                   			  设置代理，格式：http:127.0.0.1:7890，注意没有//



