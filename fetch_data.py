#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
震有科技（688418.SH）— 获取过去一年数据，画收盘价曲线图，保存 CSV
"""

import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
from datetime import datetime, timedelta
from dotenv import load_dotenv

# ── 配置 ──────────────────────────────────────────────────────────────
load_dotenv()
TOKEN = os.getenv('TUSHARE_TOKEN')
if not TOKEN:
    raise SystemExit('错误：未设置 TUSHARE_TOKEN，请在 .env 中配置')

TS_CODE = '688418.SH'
END_DATE = datetime.now().strftime('%Y%m%d')
START_DATE = (datetime.now() - timedelta(days=365)).strftime('%Y%m%d')

os.makedirs('data', exist_ok=True)
os.makedirs('reports', exist_ok=True)

# ── 1. 获取数据 ──────────────────────────────────────────────────────
print(f'获取 {TS_CODE} {START_DATE} → {END_DATE} 的数据...')

import tushare as ts
pro = ts.pro_api(TOKEN)
df = pro.daily(ts_code=TS_CODE, start_date=START_DATE, end_date=END_DATE)

if df is None or df.empty:
    raise SystemExit('错误：未获取到数据')

df = df.sort_values('trade_date', ascending=True)
df['trade_date'] = pd.to_datetime(df['trade_date'], format='%Y%m%d')
print(f'✓ 共 {len(df)} 条记录，'
      f'日期 {df["trade_date"].min().strftime("%Y-%m-%d")} → '
      f'{df["trade_date"].max().strftime("%Y-%m-%d")}')

# ── 2. 保存 CSV ──────────────────────────────────────────────────────
csv_path = os.path.join('data', TS_CODE.replace('.', '_') + '_daily.csv')
df.to_csv(csv_path, index=False, encoding='utf-8-sig')
print(f'✓ CSV 已保存：{csv_path}')

# ── 3. 画收盘价曲线图 ────────────────────────────────────────────────
# 中文字体
sys_platform = platform.system()
if sys_platform == 'Darwin':
    candidates = ['Arial Unicode MS', 'STHeiti', 'Heiti SC', 'PingFang SC']
elif sys_platform == 'Windows':
    candidates = ['SimHei']
else:
    candidates = ['WenQuanYi Micro Hei', 'Noto Sans CJK SC']

available = {f.name for f in fm.fontManager.ttflist}
for font in candidates:
    if font in available:
        plt.rcParams['font.sans-serif'] = [font]
        break
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['trade_date'], df['close'], color='#2563eb', linewidth=1.5)
ax.fill_between(df['trade_date'], df['close'], alpha=0.15, color='#2563eb')
ax.set_title(f'震有科技（{TS_CODE}）收盘价走势', fontsize=16, pad=15)
ax.set_xlabel('日期')
ax.set_ylabel('收盘价（元）')
ax.grid(True, alpha=0.3)
fig.autofmt_xdate()

chart_path = os.path.join('reports', 'close_price.png')
fig.savefig(chart_path, dpi=150, bbox_inches='tight')
plt.close(fig)
print(f'✓ 收盘价曲线图已保存：{chart_path}')

# ── 完成 ──────────────────────────────────────────────────────────────
print(f'\n✅ 全部完成！')
print(f'   CSV:  {csv_path}')
print(f'   图表: {chart_path}')
