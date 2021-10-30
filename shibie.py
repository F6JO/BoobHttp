#-*-coding:gb2312-*-
import copy


class jiexi():
    def __init__(self,wenjian,fangfa):
        self.fangfa = fangfa
        dakai = open(wenjian, "r")
        self.liebiao = dakai.readlines()
    def Get_mode(self):
        post = self.liebiao[0].startswith('POST',0)
        get = self.liebiao[0].startswith('GET',0)
        if post:
            return "POST"
        elif get:
            return "GET"
        else:
            return "False"
    def Get_url(self):
        lujing = self.liebiao[0].split(" ",3)[1]
        if "http" in self.liebiao[0]:
            return lujing
        else:
            ip = ""
            for i in self.liebiao:
                if i.startswith("Host",0):
                    a = i.split(': ', 1)
                    if len(a) == 2:
                        ip = a[1].strip('\n')
                        break
                    elif len(a) == 1:
                        b = i.split(':', 1)
                        ip = b[1].strip('\n')
                        break
            return self.fangfa + "://"+ip+lujing

    def Get_head(self):
        liebiao = copy.copy(self.liebiao)
        zidian = {}
        for i in liebiao[1::]:
            a = i.split(': ', 1)
            if len(a) == 1:
                a = i.split(':', 1)
            if len(a) == 2:
                if a[0] == "Host":
                    continue
                a[1] = a[1].strip('\n')
                a[0] = a[0].strip('\n')
                zidian[a[0]] = a[1]
            else:
                break
        return zidian

    def Get_data(self):
        fangfa = self.Get_mode()
        if fangfa != "False":
            if fangfa == "POST":
                if self.liebiao[-1] == "\n":
                    return ""
                else:
                    return self.liebiao[-1]
        else:
            print("不支持此方法，请使用POST/GET")
            exit()
if __name__ == '__main__':
    pass
    # for i in lei.liebiao:
    #     print(i)
    # print(lei.Get_data())
    # print(lei.Get_mode())
    # print(lei.Get_url())
    # print(lei.Get_head())
    # lei.Get_data()