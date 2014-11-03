#!/usr/bin/env python
# encoding: utf-8

from pylab import *
seed_length=[0,8,16,24,32,40,48]
working_time_70=[1415.992,1399.711,1055.278,810.279,463.349,313.016,227.662]
recall_rate_70=[0.96,0.93,0.91,0.88,0.84,0.82,0.8]
accuracy_rate_70=[0.97,0.976,0.98,0.988,0.99,0.992,0.993]



mpl.rcParams['font.sans-serif'] = ['Adobe Fangsong Std'] #指定默认字体
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
#plt.figure()
figure(figsize=[12,5],dpi=128)
subplot(1,2,1)
plot(seed_length,working_time_70,'o-')
xlabel(u"seed长度")
ylabel(u"比对时间(单位：秒)")
xlim(-4,52,)
xticks(xrange(0,52,8))
subplot(1,2,2)
plot(seed_length,recall_rate_70,'o-',label='Recall Rate')
plot(seed_length,accuracy_rate_70,'x-',label='Accuracy')
xlabel(u"seed长度")
xlim(-4,52)
xticks(xrange(0,52,8))
legend(loc="lower left")
show()
