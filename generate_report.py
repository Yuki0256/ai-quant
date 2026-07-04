#!/usr/bin/env python3
"""生成作业 PDF 报告"""

from fpdf import FPDF
import os

REPO_URL = "https://github.com/Yuki0256/ai-quant"
PAGES_URL = "https://yuki0256.github.io/ai-quant/"

FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"


class Report(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("zh", "", 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 8, "量化交易作业报告  |  震有科技(688418.SH)", align="C")
            self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font("zh", "", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"第 {self.page_no()} 页", align="C")


def main():
    pdf = Report()
    pdf.add_font("zh", "", FONT_PATH)
    pdf.add_font("zh", "B", FONT_PATH)  # fpdf2 will simulate bold
    pdf.set_auto_page_break(auto=True, margin=20)

    # ── 封面 ──────────────────────────────────────────────────
    pdf.add_page()
    pdf.ln(60)
    pdf.set_font("zh", "B", 28)
    pdf.cell(0, 15, "量化交易作业报告", align="C")
    pdf.ln(20)
    pdf.set_font("zh", "", 14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "震有科技（688418.SH）卫星互联网量化分析", align="C")
    pdf.ln(16)
    pdf.set_font("zh", "", 11)
    pdf.cell(0, 8, f"仓库地址：{REPO_URL}", align="C")
    pdf.ln(8)
    pdf.cell(0, 8, f"Pages 地址：{PAGES_URL}", align="C")
    pdf.ln(40)
    pdf.set_text_color(150, 150, 150)
    pdf.set_font("zh", "", 10)
    pdf.cell(0, 8, "生成日期：2026-07-04", align="C")

    # ── Q1 ─────────────────────────────────────────────────────
    pdf.add_page()
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("zh", "B", 18)
    pdf.cell(0, 14, "一、量化交易相比传统手工交易的优势")
    pdf.ln(18)

    items_q1 = [
        ("1. 不被情绪牵着走",
         "人不是机器，看到股票大涨就想追，大跌就慌着割肉，这是本能。量化交易先把规则写进程序，条件到了自动下单，不害怕、不贪婪，严格执行既定策略。"),
        ("2. 眼睛多、看得全",
         "一个人同时盯十几只股票已经很累了。量化程序可以同时看几千只股票，把价格、成交量、公司财报、新闻舆情一起算，找到人脑发现不了的规律。"),
        ("3. 先模拟再实战",
         "手工炒股靠经验，亏了才知道不对。量化可以把策略放到过去几年的数据上跑一遍，看看历史上能赚多少、最大会亏多少。好比游戏里先练级，再打BOSS。"),
        ("4. 下单快、不费力",
         "看到信号再手动下单，几秒就过去了。量化程序在毫秒级就能完成买入卖出，还能7x24小时自动盯盘，不用天天对着屏幕。"),
        ("5. 小钱和大钱一样管",
         "一套量化策略，管1万块钱和管1个亿，逻辑是一样的。手工交易资金大了以后买卖都会影响价格，量化可以用算法慢慢买卖，把影响降到最低。"),
    ]
    for title, body in items_q1:
        pdf.set_font("zh", "B", 12)
        pdf.cell(0, 9, title)
        pdf.ln(11)
        pdf.set_font("zh", "", 10)
        pdf.multi_cell(0, 6, body)
        pdf.ln(6)

    # ── Q2 ─────────────────────────────────────────────────────
    pdf.add_page()
    pdf.set_font("zh", "B", 18)
    pdf.cell(0, 14, "二、基本概念解释")
    pdf.ln(18)

    pdf.set_font("zh", "B", 12)
    pdf.cell(0, 9, "K线——一根柱子讲清楚一天的价格")
    pdf.ln(11)
    pdf.set_font("zh", "", 10)
    pdf.multi_cell(0, 6, (
        "K线最早是日本米商发明的，现在全世界看股票都用它。每一根K线包含四个价格：开盘价（今天第一笔成交价）、收盘价（今天最后一笔成交价）、最高价和最低价。\n\n"
        "• 阳线（红色、空心）：收盘价比开盘价高，说明今天涨了\n"
        "• 阴线（绿色、实心）：收盘价比开盘价低，说明今天跌了\n"
        "• 上影线：当天涨到过这个价但被打下来了，说明上方有压力\n"
        "• 下影线：当天跌到这里又被拉回来了，说明下方有支撑\n\n"
        "把很多根K线连在一起，就能看出股价是怎么走的——是涨是跌、波动大不大。"
    ))
    pdf.ln(6)

    pdf.set_font("zh", "B", 12)
    pdf.cell(0, 9, "基本面——这家公司到底值多少钱")
    pdf.ln(11)
    pdf.set_font("zh", "", 10)
    pdf.multi_cell(0, 6, (
        "基本面分析不看K线图，而是研究公司本身。问的问题很简单：这家公司赚不赚钱？生意好不好？有没有前途？\n\n"
        "• 宏观大环境：经济好不好、利率高不高、行业有没有政策支持\n"
        "• 公司自身：收入利润怎么样、有没有负债、管理层靠不靠谱\n\n"
        '核心思路是“买股票就是买公司”——如果股价比公司实际价值低，就买；比实际价值高太多，就卖。代表人物是巴菲特。'
    ))
    pdf.ln(6)

    pdf.set_font("zh", "B", 12)
    pdf.cell(0, 9, "技术面——看图说话")
    pdf.ln(11)
    pdf.set_font("zh", "", 10)
    pdf.multi_cell(0, 6, (
        "技术面不管公司赚多少钱，只看价格和成交量。它的想法是：市场里所有人的买卖行为都体现在价格上了，研究K线图就能找到买卖时机。\n\n"
        "• 看图：找趋势线、看支撑位和阻力位\n"
        "• 算指标：比如5日均线（过去5天平均价）、MACD、RSI等\n"
        "• 看量：价格上涨有没有放量配合，下跌有没有缩量\n\n"
        "核心假设是人性的贪婪和恐惧不会变，过去出现过的走势模式以后还会再出现。"
    ))
    pdf.ln(6)

    # ── Q3 ─────────────────────────────────────────────────────
    pdf.add_page()
    pdf.set_font("zh", "B", 18)
    pdf.cell(0, 14, "三、Tushare 数据获取与可视化")
    pdf.ln(16)

    pdf.set_font("zh", "", 10)
    pdf.multi_cell(0, 6, (
        "使用 Tushare Pro API 获取震有科技（688418.SH）过去一年的每日交易数据，"
        "共242条记录，日期从2025-07-04至2026-07-03。"
    ))
    pdf.ln(6)

    # 插入图表
    chart_path = "reports/close_price.png"
    if os.path.exists(chart_path):
        # Calculate dimensions to fit within page margins
        page_w = pdf.w - 2 * pdf.l_margin
        pdf.image(chart_path, x=pdf.l_margin, w=page_w)
        pdf.ln(4)
        pdf.set_font("zh", "", 9)
        pdf.set_text_color(120, 120, 120)
        pdf.cell(0, 6, "图：震有科技（688418.SH）近一年收盘价走势", align="C")
        pdf.set_text_color(0, 0, 0)
    pdf.ln(10)

    pdf.set_font("zh", "B", 12)
    pdf.cell(0, 9, "数据文件")
    pdf.ln(11)
    pdf.set_font("zh", "", 10)
    pdf.multi_cell(0, 6, (
        "CSV 数据文件：data/688418_SH_daily.csv\n"
        "包含字段：ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount\n\n"
        "收盘价曲线图：reports/close_price.png"
    ))
    pdf.ln(10)

    pdf.set_font("zh", "B", 12)
    pdf.cell(0, 9, "Python 核心代码")
    pdf.ln(14)
    code = (
        'import tushare as ts\n'
        'from dotenv import load_dotenv\n\n'
        'load_dotenv()\n'
        "pro = ts.pro_api(os.getenv('TUSHARE_TOKEN'))\n\n"
        "# 获取过去一年数据\n"
        "df = pro.daily(ts_code='688418.SH',\n"
        "               start_date='20250704',\n"
        "               end_date='20260704')\n"
        "df = df.sort_values('trade_date')\n\n"
        "# 保存 CSV\n"
        "df.to_csv('data/688418_SH_daily.csv',\n"
        "          index=False, encoding='utf-8-sig')\n\n"
        "# 画收盘价曲线图\n"
        "plt.plot(df['trade_date'], df['close'])\n"
        "plt.savefig('reports/close_price.png')"
    )
    pdf.set_font("zh", "", 9)
    pdf.set_fill_color(240, 240, 240)
    pdf.multi_cell(0, 5, code, fill=True)

    pdf.ln(10)
    pdf.set_font("zh", "", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 7, f"完整代码与数据见仓库：{REPO_URL}")

    pdf.output("量化交易作业报告.pdf")
    print("✓ PDF 已生成：量化交易作业报告.pdf")


if __name__ == "__main__":
    main()
