"""Графики для README. Запуск из корня репозитория: python scripts/make_figures.py"""
import pandas as pd, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
BLUE='#2b6cb0'; LIGHT='#90cdf4'; GREY='#a0aec0'; ORANGE='#dd6b20'
plt.rcParams.update({'font.size':10,'axes.titlesize':12,'axes.titleweight':'bold','axes.spines.top':False,'axes.spines.right':False,
                     'axes.grid':True,'grid.alpha':.25,'axes.axisbelow':True,'legend.frameon':False})
r=pd.read_excel('data/indicators_raw.xlsx').set_index('Год')
inc=r['Среднедушевые доходы с учетом ИПЦ, руб']; gini=r['Коэффициент Джини']
# 1. Доходы и Джини
fig,ax=plt.subplots(figsize=(10,4))
ax.plot(inc.index,inc/1000,'o-',color=BLUE,ms=4,label='реальные доходы на душу'); ax.set_ylabel('Доходы, тыс. ₽ (с учётом ИПЦ)',color=BLUE)
ax2=ax.twinx(); ax2.plot(gini.index,gini,'s--',color=ORANGE,ms=4,label='коэффициент Джини'); ax2.set_ylabel('Коэффициент Джини',color=ORANGE); ax2.grid(False); ax2.spines['right'].set_visible(True)
ax.set_title('Реальные доходы и неравенство росли вместе до 2008 года, а после 2013-го вместе снижались')
h1,l1=ax.get_legend_handles_labels(); h2,l2=ax2.get_legend_handles_labels(); ax.legend(h1+h2,l1+l2,loc='upper left')
fig.tight_layout(); fig.savefig('images/income_and_gini.png',dpi=130); plt.close()
