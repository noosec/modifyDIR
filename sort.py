#!/usr/bin/env  python
# -*- coding:utf-8 -*-

import re
import sys
import getopt
import os


reload(sys)
sys.setdefaultencoding('utf8')

type=sys.getfilesystemencoding()

def usage():
    print
    print "[+]./sort.py  -s a.txt  -o b.txt"
    print

    print '-s  file1  -o  file2     -从file1中提取9位数字，存放到file2中'.decode('utf-8').encode(type)

    print '-t  file                 -对文件进行排序，去重'.decode('utf-8').encode(type)
    print '-a  file                 -对于学号=45的班级，增加学号到65'.decode('utf-8').encode(type)
    print '-b                       -将某目录下文件追加到bigfile.txt文件中（需要配置目录）'.decode('utf-8').encode(type)
    print '-c  file                 -对此文件进行排序去重，整理成jsp,asp,php，dir字典'.decode('utf-8').encode(type)
    print '-h                       -显示帮助信息'.decode('utf-8').encode(type)
    print



def user_tiq(s_file,o_file):
    print "[+] Start  ..."
    #从文本中取出9位数的学号
    f=open(s_file,'r')  #源文件
    o=open(o_file,'a')  #提取后输出文件
    for eachline in f:

        re1=re.search(r'(\d{9})',eachline)
        if re1 is not None:
            print re1.group()
            o.write(re1.group(0)+'\n')
    f.close()
    o.close()
    print "[+] It's down !"



def sort(sort_file):
    #对一个文本文件进行去重排序
    print '[+] Sort Start ...'
    list1=[]
    sor=open(sort_file,'r')
    for eachline in sor:
        list1.append(eachline.strip())
    re_set=sorted(set(list1))
    sor.close()

    sort_txt=open(sort_file,'w')
    for i in range(len(re_set)):
        sort_txt.write(re_set[i]+'\n')
        #print re_set[i]
    sort_txt.close()
    print '[+] Sorted down !'

def add_data(filename):
    #对于学号=45的班级，增加学号到65
    f=open(filename,'r')
    txt=f.readlines()
    b=[]
    for i in range(len(txt)):
        if txt[i][7:9]=='45' and txt[i][0:2]!='12':#学号非12级的，
            for j in range(45,66):
                b.append(txt[i][0:7]+str(j)+'\n')
        else:
            b.append(txt[i])
    f.close()
    out=open(filename,'w')
    for i in range(len(b)):
        out.write(b[i])
    out.close()

def big_file():
    f=open('bigfile.txt','a+')
    num=os.listdir(r'E:\work\python\first_py\login\dir2')
    os.chdir(r'E:\work\python\first_py\login\dir2')
    for each in range(len(num)):

        b=open(num[each],'r')
        for eachline in b:
            f.write(eachline)

        b.close()
    f.close()


def asp_jsp_php(file1):
    sort(file1)
    f=open(file1,'r')
    cwd=os.getcwd()
    if not os.path.exists(cwd+'/dir'):
        os.mkdir('dir')
    os.chdir('dir')
    asp=open('asp.txt','a+')
    jsp=open('jsp.txt','a+')
    php=open('php.txt','a+')
    dir1=open('dir.txt','a+')
    for eachline in f:
        if re.search('.*\.asp$|.*\.aspx$|.*\.asa$|.*\.cer$',eachline) is not None:
            asp.write(eachline)
        elif re.search('\.jsp$|\.jspx$',eachline) is not None:
            jsp.write(eachline)
        elif re.search('\.php$',eachline) is not None:
            php.write(eachline)
        else:
            dir1.write(eachline)
    asp.close()
    jsp.close()
    php.close()
    dir1.close()




if __name__ == '__main__':

    tiqu_s=False
    tiqu_o=False

    sort1=False
    add=False
    zl_f=False
    big_f=False
    if not len(sys.argv[1:]):
        usage()
        sys.exit()
    try :
        opts,args=getopt.getopt(sys.argv[1:],"hs:o:t:a:c:b")
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit()
    for o,a in opts:
        if o in ("-h"):
            usage()
        elif o in ("-s"):
            s_file=a
            tiqu_s=True
        elif o in ("-o"):
            o_file=a
            tiqu_o=True
        elif o in ('-t'):
            sort_file=a
            print sort_file,type(sort_file)
            sort1=True
        elif o in ("-a"):
            add_file=a
            add=True
        elif o in ("-c"):
            zl=a
            zl_f=True
        elif o in ("-b"):
            #big1=a
            big_f=True
        else:
            print "Unhandled options "

    if tiqu_s and tiqu_o:
        user_tiq(s_file,o_file)
    if sort1:
        sort(sort_file)
    if add:
        add_data(add_file)
    if zl_f:
        asp_jsp_php(zl)
    if big_f:
        big_file()
