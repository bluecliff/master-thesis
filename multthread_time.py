#!/usr/bin/env python
# encoding: utf-8

from pylab import *
#多线程比对的时间和空间
working_time_35=[1851,935,480,267,270,268]
working_memory_35=[3330,3382,3467,3565,3597,3626]
working_time_70=[4580,2307,1169,598,598,602]
working_memory_70=[3384,3463,3551,3649,3658,3695]
working_memory_125=[3447,3538,3641,3723,3744,3771]
working_time_125=[12378,6197,3113,1564,1562,1567]


#mpl.rcParams['font.sans-serif'] = ['Adobe Fangsong Std'] #指定默认字体
#mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
#plt.figure()
figure(figsize=[12,5],dpi=128)
subplot(1,2,1)
plot(xrange(1,7),working_time_35,marker='o',linestyle="-",label=u"35bp")
plot(xrange(1,7),working_time_70,'x-',label=u'70bp')
plot(xrange(1,7),working_time_125,'v-',label=u'125bp')
xlim(0,7)
xlabel(u'Thread Count')
xticks(xrange(1,7),xrange(1,7))
#ylim(50,1100)
ylabel(u"Time(s)")
legend(loc="upper right")
#show()
#figure()
subplot(1,2,2)
plot(xrange(1,7),[item for item in working_memory_35],'o-',label="35bp")
plot(xrange(1,7),[item for item in working_memory_70],'x-',label="70bp")
plot(xrange(1,7),[item for item in working_memory_125],'v-',label="125bp")
xlim(0,7)
xlabel(u'Thread Count')
xticks(xrange(1,7),xrange(1,7))
#ylim(3000,3650)
ylabel(u"Memory(MB)")
legend(loc="upper left")
show()
