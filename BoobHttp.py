#-*-coding:gb2312-*-
import os
import time

import requests
from shibie import jiexi
import re
import copy
import threadpool
import threading
from minglinghang import minglinghang
from tuan import banner
from asse import *
requests.logging.captureWarnings(True)

class run():
    def __init__(self):
        print(banner())
        canshus = minglinghang()
        self.canshu = canshus.canshu
        # self.canshu = "mulu.txt"
        self.baocun = canshus.baocun
        self.xiancheng = canshus.xiancheng
        self.chaoshi = canshus.chaoshi
        self.chongshi = canshus.chongshi
        self.tiaozhuan = canshus.tiaozhuan
        self.kong = canshus.kong
        self.lock = threading.Lock()
        self.fangfa = canshus.fangfa
        self.pro = self.daili_chuli(canshus.pro)
        self.geshu = 0
        qingqiu = canshus.qingqiu
        # qingqiu = "D:/zhuru.txt"
        jiexihou = jiexi(qingqiu,self.fangfa)
        self.mode = jiexihou.Get_mode()
        self.url = jiexihou.Get_url()
        self.head = jiexihou.Get_head()
        self.data = jiexihou.Get_data()
        self.succeed = "succeed.txt"
        self.cishu = 1
        self.shibai = 0

    def daili_chuli(self,pro):
        if pro == None:
            return None
        else:
            if bool(re.search("https{0,1}:[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[1-9]{1,3}:[1-9]{1}[0-9]{0,4}",pro)):
                l = pro.split(':', 1)
                return {l[0]:l[1]}
            else:
                print("代理格式错误，格式如：http:127.0.0.1:7890 或 https:123.123.123.123:123，注意中间没有//")
                quit()

    def duqucanshu(self):
        print("处理参数......")
        # 处理参数，将每个文件的参数拼接为列表
        liebiao = open(self.canshu,"r",encoding="utf-8").readlines()
        self.geshu = len(liebiao)
        max = 0
        canshuliebiao = []
        jishu = 0
        for i in liebiao:
            list1 = []
            i = i.replace("\n","")
            file = open(i,"r").readlines()
            print(str(jishu)+"参数paloads个数：" + str(len(file)))
            jishu+=1
            if len(file) > max:
                max = len(file)
            for x in range(0,len(file)):
                list1.append(file[x].replace("\n",""))
            canshuliebiao.append(list1)
        for i in canshuliebiao:
            if len(i) < max:
                for a in range(len(i),max):
                    i.append(self.kong)

        # 将两个一维数组合并为一个二维数组
        zuizhonglist = []
        for i in range(len(canshuliebiao[0])):
            list4 = []
            for a in canshuliebiao:
                list4.append(a[i])
            zuizhonglist.append(list4)
        return zuizhonglist


    def tihuan(self,liebiao):
        url = copy.copy(self.url)
        head = str(copy.copy(self.head))
        data = copy.copy(self.data)
        for i in range(self.geshu):
            zhao = "\{\{"+str(i)+"\}\}"
            zhao1 = "{{"+str(i)+"}}"
            if bool(re.search(zhao,url)):
                url = url.replace(zhao1,liebiao[i])
            if bool(re.search(zhao,head)):
                head = head.replace(zhao1,liebiao[i])
            if data != None:
                if bool(re.search(zhao,data)):
                    data = data.replace(zhao1,liebiao[i])
        head = eval(head)
        list1 = self.qingqiu(url,head,data)
        if list1 == None:
            self.lock.acquire()
            self.shibai+=1
            self.lock.release()
        else:
            self.chuli(list1[0],list1[1],list1[2],liebiao)

    def qingqiu(self,url,head,data):
        cishu = 0
        while True:
            try:
                if self.mode == "GET":
                    if self.pro == None:
                        reques = requests.get(url, headers=head, allow_redirects=self.tiaozhuan,verify=False,timeout=self.chaoshi)
                    else:
                        reques = requests.get(url, headers=head, proxies=self.pro,allow_redirects=self.tiaozhuan,verify=False,timeout=self.chaoshi)
                    wenben = reques.text
                    changdu = len(wenben)
                    code = reques.status_code
                    return [wenben,changdu,code]
                elif self.mode == "POST":
                    if self.pro == None:
                        reques = requests.post(url, headers=head,verify=False,data=data, allow_redirects=self.tiaozhuan,timeout=self.chaoshi)
                    else:
                        reques = requests.post(url, headers=head,verify=False,proxies=self.pro,data=data, allow_redirects=self.tiaozhuan,timeout=self.chaoshi)
                    wenben = reques.text
                    changdu = len(wenben)
                    code = reques.status_code
                    return [wenben,changdu,code]
            except requests.exceptions.ReadTimeout:
                if cishu == self.chongshi:      #重试次数
                    return None
                cishu += 1

    def chuli(self,wenben,changdu,code,payloads):
        boo = Chu_li(wenben, changdu, code)
        self.lock.acquire()
        str1 = str(self.cishu)+2*"\t"
        self.cishu += 1
        self.lock.release()
        for i in payloads:
            str1 = str1+i+2*"\t"
        str1 += str(code)+2*"\t"
        str1 += str(changdu)
        if boo:
            self.lock.acquire()
            self.xieru(self.succeed,str1)
            self.lock.release()
        if self.baocun != None:
            self.lock.acquire()
            self.xieru(self.baocun, str1)
            self.lock.release()


    def xieru(self,wenjian,nr):
        if self.cishu == 2 | ((wenjian == self.succeed) and  not os.path.exists(wenjian)):
            file = open(wenjian, "w")
            file.write("Id"+"\t"*2)
            for i in range(0, self.geshu):
                file.write("arg"+str(i)+"\t"*2)
            file.write("Code"+"\t"*2+"Lens\n")
            file.write(nr + "\n")
            file.close()
        else:
            file1 = open(wenjian,"a")
            file1.write(nr+"\n")
            file1.close()


    def run(self):
        if os.path.exists(self.succeed):
            file = open(self.succeed,"w")
            file.write("Id" + "\t" * 2)
            for i in range(0, self.geshu):
                file.write("arg" + str(i) + "\t" * 2)
            file.write("Code" + "\t" * 2 + "Lens\n")
            file.close()
        canshu = self.duqucanshu()
        pool = threadpool.ThreadPool(self.xiancheng)
        xiancheng = threadpool.makeRequests(self.tihuan, canshu)
        print("正在分配线程......")
        for i in xiancheng:
            pool.putRequest(i)
        print("程序运行中，请关注日志文件.......")
        pool.wait()
        print("程序运行完毕")
        print("重试 {} 次仍失败个数 {} 个".format(self.chongshi,self.shibai))
        print("匹配成功payload已保存到succeed.txt文件")




if __name__ == '__main__':
    run().run()
