from tkinter import *
from pylab import *
import operator
import requests
#爬虫模块1：对数据进行统计返回排行版前十的数据
def pachong2(url):
    n=[]
    list1=[]
    for i in range(1,4):
        url = url[0:-1] + '{}'.format(i)
        r=requests .get(url).json()
        for j in r['data']['datas']:
            data = {
                '主播': j['nick'],
                '人数':float("%.2f" %(float(j['totalCount'])/10000)),
            }
            list1.append(data)
    sorted_x = sorted(list1, key=operator.itemgetter('人数'))
    for k in range(0,len(sorted_x )):
        if k>=len(sorted_x )-10:
            n.append(sorted_x[k])
    return n
#使用条形图对三个游戏的排行榜前十进行显示
def hit_me3():
    window.destroy()
    root = Tk()
    root.geometry('3000x3000')
    root.title('spider-man')
    l = Label(root, text='\n' + '\n' + '                 请选择游戏', font=('宋体', 50),
              foreground='blue', underline=1, anchor='nw'
              , width=100, height=5, bg='orange')
    l.pack()
    #英雄联盟
    def pa1():
        root.destroy()
        list1 = pachong2('https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1&tagAll=0&page=2')
        m = []
        n = []
        for i in range(0, len(list1)):
            m.append(list1[i]['主播'])
            n.append(list1[i]['人数'])
        mpl.rcParams['font.sans-serif'] = ['SimHei']
        patches = plt.bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], height=n, width=0.5, color='k',
                          tick_label=m)
        plt.legend()
        plt.ylabel('人数/万')
        plt.xlabel('主播')
        plt.title('英雄联盟排行榜前十统计图')
        for rect in patches:
            height = rect.get_height()
            if height != 0:
                plt.text(rect.get_x() + rect.get_width() / 10, height + 10, '{}'.format(height))
        plt.show()
    #穿越火线
    def pa2():
        root.destroy()
        list1 = pachong2('https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=4&tagAll=0&page=2')
        m = []
        n = []
        for i in range(0, len(list1)):
            m.append(list1[i]['主播'])
            n.append(list1[i]['人数'])
        mpl.rcParams['font.sans-serif'] = ['SimHei']
        patches = plt.bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], height=n, width=0.5, color='k',
                          tick_label=m)
        plt.legend()
        plt.ylabel('人数/万')
        plt.xlabel('主播')
        plt.title('穿越火线排行榜前十统计图')
        for rect in patches:
            height = rect.get_height()
            if height != 0:
                plt.text(rect.get_x() + rect.get_width() / 10, height + 10, '{}'.format(height))
        plt.show()
    #绝地求生
    def pa3():
        root .destroy()
        list1 = pachong2('https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2793&tagAll=0&page=2')
        m = []
        n = []
        for i in range(0, len(list1)):
            m.append(list1[i]['主播'])
            n.append(list1[i]['人数'])
        mpl.rcParams['font.sans-serif'] = ['SimHei']
        patches = plt.bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], height=n, width=0.5, color='k',
                          tick_label=m)
        plt.legend()
        plt.ylabel('人数/万')
        plt.xlabel('主播')
        plt.title('绝地求生排行榜前十统计图')
        for rect in patches:
            height = rect.get_height()
            if height != 0:
                plt.text(rect.get_x() + rect.get_width() / 10, height + 10, '{}'.format(height))
        plt.show()
    r1 = Radiobutton(root, text='英雄联盟', font=('宋体', 30), bg='orange', command=pa1)
    r1.pack()
    r2 = Radiobutton(root, text='穿越火线', font=('宋体', 30), bg='orange', command=pa2)
    r2.pack()
    r3 = Radiobutton(root, text='绝地求生', font=('宋体', 30), bg='orange', command=pa3)
    r3.pack()
    root.mainloop()
#使用扇形图对总人数进行对比
def hit_me2():
    window .destroy()
    list1=pachong('https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1&tagAll=0&page=2')
    list2=pachong('https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=4&tagAll=0&page=2')
    list3=pachong('https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2793&tagAll=0&page=2')
    m=0
    n=0
    k=0
    for i in list1:
        m=m+i['人数']
    for i in list2:
        n=n+i['人数']
    for i in list3:
        k=k+i['人数']
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(6, 9))
    labels = ['英雄联盟', '穿越火线', '绝地求生']
    sizes = [m,n,k]
    colors = ['red', 'yellowgreen', 'lightskyblue']
    explode = (0.05, 0, 0)

    patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                      startangle=90, pctdistance=0.6)
    for t in l_text:
        t.set_size = (30)
    for t in p_text:
        t.set_size = (20)
    plt.axis('equal')
    plt.legend()
    plt.show()
#爬虫模块2：爬取主播和相对应的观看人数，然后进行排序返回
def pachong(url):
    list1=[]
    for i in range(1,4):
        url = url[0:-1] + '{}'.format(i)
        r=requests .get(url).json()
        for j in r['data']['datas']:
            data = {
                '主播': j['nick'],
                '人数':float("%.2f" %(float(j['totalCount'])/10000)),
            }
            list1.append(data)
    sorted_x = sorted(list1, key=operator.itemgetter('人数'))
    return sorted_x
window = Tk()
window.geometry('3000x3000')
window.title('spider-man')
l = Label(window, text='\n'+'                欢迎使用虎牙直播数据分析器', font=('宋体', 40),
          foreground='blue',underline=1, anchor='nw'
          ,width=100, height=3, bg='orange')
l.pack()
def hit_me():
    window.destroy()
    list20 = pachong('https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1&tagAll=0&page=2')
    list21=pachong('https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=4&tagAll=0&page=2')
    def tongji(list20):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        list11 = []
        list12 = []
        list13 = []
        list14 = []
        for i in range(0, len(list20)):
            list1.append(list20[i]['主播'])
            list2.append(list20[i]['人数'])
        for i in range(0, len(list2)):
            if list2[i] >= 0 and list2[i] <= 10:
                list3.append(list20[i]['主播'])
            if list2[i] > 10 and list2[i] <= 20:
                list4.append(list20[i]['主播'])
            if list2[i] > 20 and list2[i] <= 30:
                list5.append(list20[i]['主播'])
            if list2[i] > 30 and list2[i] <= 40:
                list6.append(list20[i]['主播'])
            if list2[i] > 40 and list2[i] <= 50:
                list7.append(list20[i]['主播'])
            if list2[i] > 50 and list2[i] <= 60:
                list8.append(list20[i]['主播'])
            if list2[i] > 60 and list2[i] <= 70:
                list9.append(list20[i]['主播'])
            if list2[i] > 70 and list2[i] <= 80:
                list10.append(list20[i]['主播'])
            if list2[i] > 80 and list2[i] <= 90:
                list11.append(list20[i]['主播'])
            if list2[i] > 90 and list2[i] <= 100:
                list12.append(list20[i]['主播'])
            if list2[i] > 100 and list2[i] <= 200:
                list13.append(list20[i]['主播'])
            if list2[i] > 200:
                list14.append(list20[i]['主播'])
        list15 = [len(list3), len(list4), len(list5), len(list6), len(list7), len(list8), len(list9), len(list10),
                  len(list11), len(list12), len(list13), len(list14)]
        return list15
    #使用条形图对英雄联盟和穿越火线的观看人数的范围就行人数统计

    def tiao(list1, list2):
        mpl.rcParams['font.sans-serif'] = ['SimHei']
        patches = plt.bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], height=list1, width=0.5, color='k',
                          tick_label=['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90',
                                      '90-100', '100-200', '>200'], label='英雄联盟')
        patches2 = plt.bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], height=list2, width=0.3, color='r',
                           tick_label=['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90',
                                       '90-100', '100-200', '>200'], label='穿越火线')
        plt.legend()
        plt.ylabel('人数/个')
        plt.xlabel('范围/万')
        plt.title('虎牙人数统计图')
        for rect in patches:
            height = rect.get_height()
            if height != 0:
                plt.text(rect.get_x() + rect.get_width() / 10, height + 10, '{}'.format(height))
        for rect in patches2:
            height = rect.get_height()
            if height != 0:
                plt.text(rect.get_x() + rect.get_width() / 10, height + 5, '{}'.format(height), color='r')
        plt.show()
    if __name__ == '__main__':
        list30 = tongji(list20)
        list31 = tongji(list21)
        tiao(list30, list31)
#GUI界面
r1= Radiobutton(window,text='人气范围统计图',font=('宋体',40),bg='orange',command=hit_me)
r1.pack()
r2 = Radiobutton(window,text='全部人气比较图',font=('宋体',40),bg='orange',command=hit_me2)
r2.pack()
r3 = Radiobutton(window,text='游戏排行榜人气前十',font=('宋体',40),bg='orange',command=hit_me3)
r3.pack()
canvas=Canvas(window,bg='blue',height=450,width=450)
image_file=PhotoImage (file='2.png')
canvas .create_image(0,0,anchor='nw',image=image_file)
canvas .pack()
window .mainloop()
