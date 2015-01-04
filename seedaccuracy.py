#!/usr/bin/env python
# encoding: utf-8

from pylab import *
seed_length=[0,8,16,24,32,40,48]
working_time_70=[7037,6823,5834,5112,4580,4426,4337]

recall_rate_70=[0.9107,0.9012,0.8744,0.8575,0.8443,0.8312,0.8020]
accuracy_rate_70=[0.98,0.9898,0.9942,0.9978,0.9991,0.9993,0.9995]



#mpl.rcParams['font.sans-serif'] = ['Adobe Fangsong Std'] #指定默认字体
#mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
#plt.figure()
figure(figsize=[12,5],dpi=128)
subplot(1,2,1)
plot(seed_length,working_time_70,'o-')
xlabel("Seed Length")
ylabel("Time(s)")
xlim(-4,52,)
xticks(xrange(0,52,8))
subplot(1,2,2)
plot(seed_length,recall_rate_70,'o-',label='Recall Rate')
plot(seed_length,accuracy_rate_70,'x-',label='Accuracy')
xlabel("Seed Length")
xlim(-4,52)
xticks(xrange(0,52,8))
legend(loc="lower left")
show()
