#!/usr/bin/env python
# encoding: utf-8

from pylab import *
#多线程比对的时间和空间
working_time_35=[201,114,114,111,111,110]
working_memory_35=[3235278848,3274301440,3274747904,3275419648,3286237184,3286425600]
working_time_70=[460,254,256,253,256,254]
working_memory_70=[3268591616,3338215424,3342258176,3356774400,3370038016,3386941440]
working_memory_125=[3402596352,3482193920,3511316480,3561840640,3591553024,3814600704]
working_time_125=[1071,586,590,590,589,592]


mpl.rcParams['font.sans-serif'] = ['Adobe Fangsong Std'] #指定默认字体
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
#plt.figure()
figure(figsize=[12,5],dpi=128)
subplot(1,2,1)
plot(xrange(1,7),working_time_35,marker='o',linestyle="-",label=u"35bp")
plot(xrange(1,7),working_time_70,'x-',label=u'70bp')
plot(xrange(1,7),working_time_125,'v-',label=u'125bp')
xlim(0,7)
xlabel(u'Thread Count')
xticks(xrange(1,7),xrange(1,7))
ylim(50,1100)
ylabel(u"Time(s)")
legend(loc="upper right")
#show()
#figure()
subplot(1,2,2)
plot(xrange(1,7),[item/1024.0/1024.0 for item in working_memory_35],'o-',label="35bp")
plot(xrange(1,7),[item/1024.0/1024.0 for item in working_memory_70],'x-',label="70bp")
plot(xrange(1,7),[item/1024.0/1024.0 for item in working_memory_125],'v-',label="125bp")
xlim(0,7)
xlabel(u'Thread Count')
xticks(xrange(1,7),xrange(1,7))
ylim(3000,3650)
ylabel(u"Memory(MB)")
legend(loc="upper left")
show()
