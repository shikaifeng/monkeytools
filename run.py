# -*- coding: utf-8 -*-

'''
shikaifeng test
'''


import sys
import subprocess
import time,os
from jinja2 import Template

memfile = os.path.abspath('.') +"/output/" + time.strftime("%Y-%m-%d_%H_%M_%S", time.gmtime()) + "_package_total_meminfo.txt"
timefile = os.path.abspath('.') +"/output/" + time.strftime("%Y-%m-%d_%H_%M_%S", time.gmtime()) + "_memtimeinfo.txt"
tempfile = os.path.abspath('.') + "/zhexiantutemp.html"
rendertempfile = os.path.abspath('.') + "/template_render_test.html"

def now_time():
    localtime = time.asctime( time.localtime(time.time()) )
    time_array = localtime.split(" ")[3].split(":")
    print time_array
    return time_array[0]+'_'+time_array[1]+"_"+time_array[2]

def WriteTotalMemAndTime(waittime,package_name):
    try:
        print os.system("adb devices")
        cmd = "adb shell dumpsys meminfo com.yunos.tvtaobao | grep 'TOTAL'|awk '{print $2}'"
        os.path
        totalMem = open(memfile, "a")
        f_x_time = open (timefile, "a")
        output = subprocess.Popen(cmd,shell=True,stdout=totalMem).stdout
        t = time.strftime ('%Y-%m-%d_%H:%M:%S', time.localtime (time.time ()))
        f_x_time.write(time.strftime(t)+"\r")


        #output = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).stdout
        #print output.read()
        print '应用内存正在记录。。。请稍后'

        time.sleep(float(waittime)*1)
        totalMem.close()
        f_x_time.close()
    except KeyboardInterrupt:
        print '报告正在生成'
        #s.system('adb kill-server')


def getDumpmeminfo():
    '''
    根据应用包名查看内存信息,默认返回TOTAL信息
    使用dumpsys meminfo'''
    mem_data = []
    for line in open(memfile):
        temp = int(line.split()[0])
        mem_data.append(temp/1024)
        print temp
    return mem_data

def getDumpmeminfoTime():
    for line in open(timefile):
        temp = line.split()
        return temp


def generateHtml():
    reload (sys)
    sys.setdefaultencoding ('utf8')
    mem_data = getDumpmeminfo()
    x_time= getDumpmeminfoTime()
    f = open (tempfile)
    template_str = f.read ()
    template = Template (template_str)
    out = template.render ({"xtime": x_time, "pmem": mem_data, })
    dest_file = os.path.abspath('.') + "/template_render_test.html"
    f = open(dest_file, 'w')
    f.write(out)
    f.close()

if __name__ == '__main__':
        count = 0
while (count < 1):
        WriteTotalMemAndTime(1,"com.yunos.tvtaobao")
        count =count+1
print getDumpmeminfo()
print getDumpmeminfoTime()
print len(getDumpmeminfo())
print len(getDumpmeminfoTime())
generateHtml()
