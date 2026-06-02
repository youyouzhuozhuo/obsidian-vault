"""
高级经济师（工商管理）备考系统
2026年考试 · 目标：60分及格即可

项目结构：
├── CLAUDE.md              # 项目说明
├── study_plan.py          # 本文件：学习计划与备考引擎
├── knowledge_points/      # 各章节知识点精要
│   ├── ch01_企业职能与战略决策.md
│   ├── ch02_企业制度与组织结构.md
│   ├── ...
│   └── ch11_国际商务运营.md
├── exam_strategy/         # 应试策略
│   ├── scoring_guide.md       # 答题评分标准与拿分技巧
│   ├── case_analysis.md       # 案例分析题解题模板
│   └── essay_template.md      # 论述题万能框架
├── hot_topics/            # 2026年时政热点押题
│   └── 2026_hot_topics.md
├── mock_exams/            # 模拟题与解析
│   ├── mock_1.md
│   ├── mock_2.md
│   └── mock_3.md
├── memory_aids/           # 记忆口诀与速记
│   └── memory_cheatsheet.md
└── progress/              # 学习进度跟踪
    └── progress.json
"""


# ============================================================
# 第一部分：章节权重分析（基于历年真题统计）
# 考试策略：优先攻克高分值章节，放弃低分值冷门内容
# ============================================================

CHAPTER_WEIGHTS = {
    1:  {"name": "企业职能与战略决策", "weight": 14, "difficulty": 3, "must_master": True},
    2:  {"name": "企业制度与组织结构", "weight": 10, "difficulty": 2, "must_master": True},
    3:  {"name": "市场营销管理",       "weight": 10, "difficulty": 2, "must_master": True},
    4:  {"name": "生产运营管理",       "weight": 8,  "difficulty": 3, "must_master": False},
    5:  {"name": "质量管理与安全管理", "weight": 5,  "difficulty": 2, "must_master": False},
    6:  {"name": "供应链管理",         "weight": 8,  "difficulty": 3, "must_master": False},
    7:  {"name": "企业创新",           "weight": 10, "difficulty": 2, "must_master": True},
    8:  {"name": "人力资源管理",       "weight": 10, "difficulty": 2, "must_master": True},
    9:  {"name": "财务管理",           "weight": 12, "difficulty": 4, "must_master": True},
    10: {"name": "管理信息系统与电子商务", "weight": 6, "difficulty": 2, "must_master": False},
    11: {"name": "国际商务运营",       "weight": 7,  "difficulty": 3, "must_master": False},
}

# 权重说明：百分比为该章在考试中大约占的分值比例
# difficulty: 1=简单 2=中等 3=较难 4=最难
# must_master: True表示必须掌握（高频出题章节）

# ============================================================
# 第二部分：应试策略核心 —— 60分就够的极简策略
# ============================================================

STRATEGY_60 = {
    "name": "60分及格策略",
    "core_idea": "放弃20%冷门内容，集中攻克80%高频考点",

    # 第一梯队：必须拿下（约50分的内容）
    "tier1_must_pass": {
        "chapters": [1, 7, 9, 2, 8, 3],
        "target_score": "至少拿到42分（满分的70%）",
        "reason": "这6章占约66%分值，是案例题和论述题的主要出题来源",
    },

    # 第二梯队：掌握核心概念（约20分的内容）
    "tier2_basic": {
        "chapters": [4, 6, 11],
        "target_score": "至少拿到12分",
        "reason": "会考到但不一定是主战场，掌握核心概念和关键词即可",
    },

    # 第三梯队：了解即可（约14分的内容）
    "tier3_skip": {
        "chapters": [5, 10],
        "target_score": "能写多少写多少，约6分",
        "reason": "偏冷门，出大题概率低，考前快速过一遍",
    },

    "total_target": "42 + 12 + 6 = 60分（及格）",
}

# ============================================================
# 第三部分：答题模板
# ============================================================

CASE_ANALYSIS_TEMPLATE = """
【案例分析题答题模板】

一、定性判断（2-3分）
  明确指出案例中的核心问题/现象属于哪个知识点。
  话术："根据XXX理论/政策/法规，案例中企业存在的问题是..."

二、理论阐述（3-5分）
  列出相关理论的要点（编号列出）。
  话术："该理论/政策/法规的核心要点包括：①...②...③..."

三、案例分析（5-8分）
  将理论与案例具体事实一一对应分析。
  话术："结合案例：第一，企业...（对应要点①）；第二，..."

四、对策建议（5-8分）
  提出具体的、可操作的建议（至少3条）。
  话术："建议该企业采取以下措施：
  （1）短期：...
  （2）中期：...
  （3）长期：..."

五、总结提升（2分）
  一句话拔高到政策或理论高度。
  话术："这体现了当前...的改革方向/政策导向"
"""

ESSAY_TEMPLATE = """
【论述题答题模板（30分）】

开头（3-5分）：
  "关于XXX问题，我认为..." + 一句话表明核心观点
  + 简要政策背景（提及最新政策/领导人讲话精神加分）

主体段落1：理论依据（8-10分）
  "首先，从理论层面看..."
  列出2-3个相关理论的核心内容（用编号：①②③）
  每个理论配一句话解释

主体段落2：现实分析（8-10分）
  "其次，从现实层面看..."
  分析当前现状 + 存在问题 + 数据支撑（编也得编点趋势）
  "当前我国在XXX方面存在以下问题：一是...二是...三是..."

主体段落3：对策建议（5-8分）
  "为此，建议采取以下措施："
  至少3条建议，按"政府层面"+"企业层面"分层
  每条建议具体可操作

结尾（2-3分）：
  "综上所述..." + 拔高到国家战略/政策高度
  "这与我国...战略/政策高度契合"
"""

# ============================================================
# 第四部分：各章节高频考点速查
# ============================================================

HIGH_FREQ_POINTS = {
    1: [
        "企业战略类型（总体战略：发展、稳定、紧缩）",
        "竞争战略（成本领先、差异化、集中化）",
        "SWOT分析、波特五力模型、价值链分析",
        "BCG矩阵（明星/金牛/问题/瘦狗）",
        "商业模式画布9要素",
        "经营决策方法（确定型/风险型/不确定型）",
        "决策树分析、乐观/悲观/折中/后悔值准则",
    ],
    2: [
        "公司治理结构三会一层（股东会/董事会/监事会/管理层）",
        "国有独资公司治理特点",
        "独立董事制度",
        "委托代理问题与解决机制",
        "企业组织结构类型（U型/M型/H型/矩阵制）",
        "组织变革的动力与阻力",
    ],
    3: [
        "STP战略（市场细分→目标市场→市场定位）",
        "4P/4C/4R营销组合理论",
        "产品生命周期策略（导入期/成长期/成熟期/衰退期）",
        "品牌战略（多品牌/单一品牌/复合品牌）",
        "定价策略（成本导向/需求导向/竞争导向）",
        "渠道策略（直销/经销/电商渠道）",
        "新媒体营销与数字化营销",
    ],
    7: [
        "技术创新的分类（产品创新/工艺创新）",
        "技术创新模式（自主创新/模仿创新/合作创新）",
        "技术引进与技术转移",
        "主导设计与技术标准战略",
        "创新管理的阶段与流程",
        "管理创新的内容与方法",
    ],
    8: [
        "战略性人力资源管理",
        "胜任力模型（冰山模型/洋葱模型）",
        "招聘渠道与甄选方法",
        "绩效考核方法（KPI/OKR/BSC/360度）",
        "薪酬体系设计（岗位/技能/绩效薪酬）",
        "股权激励与长期激励",
        "职业生涯管理的锚理论",
    ],
    9: [
        "财务管理的目标（利润最大化/股东财富最大化/企业价值最大化）",
        "资本成本计算（债务资本成本/权益资本成本/WACC）",
        "杠杆效应（经营杠杆/财务杠杆/总杠杆）",
        "资本结构理论（MM理论/权衡理论/优序融资理论）",
        "投资决策指标（NPV/IRR/PI/回收期）",
        "并购的类型与动因",
        "财务分析（偿债/营运/盈利/发展能力指标）",
    ],
}

# ============================================================
# 第五部分：2026年时政热点押题方向
# ============================================================

HOT_TOPICS_2026 = [
    {
        "topic": "国企改革深化提升行动",
        "related_chapters": [1, 2],
        "keywords": "中国特色现代企业制度、国有经济布局优化、核心功能提升",
        "sample_angle": "结合国企改革，论述如何完善中国特色公司治理结构",
    },
    {
        "topic": "数字经济与实体经济深度融合",
        "related_chapters": [7, 10],
        "keywords": "数字化转型、产业数字化、数字产业化、平台经济",
        "sample_angle": "企业如何通过数字化转型提升核心竞争力",
    },
    {
        "topic": "新质生产力与企业创新",
        "related_chapters": [1, 7],
        "keywords": "新质生产力、科技创新、关键核心技术攻关",
        "sample_angle": "论述企业如何通过技术创新发展新质生产力",
    },
    {
        "topic": "供应链安全与韧性",
        "related_chapters": [6, 11],
        "keywords": "产业链供应链安全、自主可控、双循环",
        "sample_angle": "分析全球供应链重构背景下中国企业如何提升供应链韧性",
    },
    {
        "topic": "绿色发展与ESG",
        "related_chapters": [4, 5, 9],
        "keywords": "双碳目标、ESG、绿色制造、可持续发展",
        "sample_angle": "论述企业如何构建ESG管理体系推动绿色转型",
    },
    {
        "topic": "人才强国战略",
        "related_chapters": [8],
        "keywords": "人才强国、高层次人才、人才评价机制",
        "sample_angle": "结合人才强国战略，论述企业如何构建战略性人力资源管理体系",
    },
    {
        "topic": "跨境电商与高水平对外开放",
        "related_chapters": [3, 10, 11],
        "keywords": "跨境电商、制度型开放、一带一路、RCEP",
        "sample_angle": "分析中国企业在跨境电商中的机遇与挑战",
    },
]


# ============================================================
# 第六部分：学习计划生成器
# ============================================================

def generate_study_plan(weeks_available: int = 8, daily_hours: float = 2.0):
    """
    生成个性化学习计划

    Args:
        weeks_available: 距离考试还有几周
        daily_hours: 每天可以学习的小时数

    Returns:
        学习计划文本
    """
    total_hours = weeks_available * 7 * daily_hours

    plan = f"""
{'='*60}
  2026年高级经济师（工商管理）备考计划
  总学习时间：{total_hours:.0f}小时（{weeks_available}周 × 7天 × {daily_hours}小时/天）
  目标分数：60分（及格线）
{'='*60}

"""

    # 第一梯队：核心章节（占总学习时间的55%）
    tier1_hours = total_hours * 0.55
    tier1_chapters = [1, 9, 7, 2, 8, 3]

    plan += f"【第一阶段】核心章节精学（约{tier1_hours:.0f}小时）\n"
    plan += "-" * 40 + "\n"

    for i, ch in enumerate(tier1_chapters):
        info = CHAPTER_WEIGHTS[ch]
        ch_hours = tier1_hours * (info['weight'] / sum(CHAPTER_WEIGHTS[c]['weight'] for c in tier1_chapters))
        plan += f"  第{ch}章 {info['name']}：{ch_hours:.1f}小时\n"

    # 第二梯队：次要章节（占总学习时间的30%）
    tier2_hours = total_hours * 0.30
    tier2_chapters = [4, 6, 11]

    plan += f"\n【第二阶段】次要章节速学（约{tier2_hours:.0f}小时）\n"
    plan += "-" * 40 + "\n"

    for ch in tier2_chapters:
        info = CHAPTER_WEIGHTS[ch]
        plan += f"  第{ch}章 {info['name']}：{tier2_hours/3:.1f}小时\n"

    # 第三梯队：了解即可（占总学习时间的5%）
    tier3_hours = total_hours * 0.05
    plan += f"\n【第三阶段】冷门章节浏览（约{tier3_hours:.0f}小时）\n"
    plan += "-" * 40 + "\n"
    plan += f"  第5章 质量管理与安全管理 + 第10章 信息系统：{tier3_hours:.1f}小时\n"

    # 冲刺阶段（占总学习时间的10%）
    sprint_hours = total_hours * 0.10
    plan += f"\n【冲刺阶段】模拟+押题+时政（约{sprint_hours:.0f}小时）\n"
    plan += "-" * 40 + "\n"
    plan += "  - 做3套模拟题，每套限时3小时\n"
    plan += "  - 背诵答题模板（案例+论述）\n"
    plan += "  - 过一遍2026年时政热点押题\n"
    plan += "  - 快速回顾各章高频考点\n"

    plan += f"\n{'='*60}\n"
    plan += "策略总结：集中精力拿下第1/2/3/7/8/9章，其余章节抓核心概念，60分稳过。\n"
    plan += "=" * 60 + "\n"

    return plan


def get_chapter_priority():
    """返回按优先级排序的章节列表"""
    chapters = []
    for ch_num, info in CHAPTER_WEIGHTS.items():
        chapters.append({
            "chapter": ch_num,
            "name": info["name"],
            "weight": info["weight"],
            "difficulty": info["difficulty"],
            "roi": info["weight"] / info["difficulty"],  # 投入产出比
            "must_master": info["must_master"],
        })

    # 按投入产出比排序（ROI高的优先学）
    chapters.sort(key=lambda x: x["roi"], reverse=True)
    return chapters


def get_quick_score_estimate(scores: dict) -> dict:
    """
    估算考试分数

    Args:
        scores: {章节号: 掌握程度(0-100)} 的字典

    Returns:
        分数估算
    """
    total = 0
    for ch, mastery in scores.items():
        weight = CHAPTER_WEIGHTS[ch]["weight"]
        total += weight * (mastery / 100)

    return {
        "estimated_score": round(total, 1),
        "pass": total >= 60,
        "gap": round(max(0, 60 - total), 1),
        "advice": "稳过！" if total >= 60 else f"还差{60-total:.1f}分，继续加油" if total >= 50 else "需要加强核心章节学习",
    }


if __name__ == "__main__":
    # 打印学习计划（默认8周备考，每天2小时）
    print(generate_study_plan(weeks_available=8, daily_hours=2.0))

    print("\n\n各章投入产出比排名（ROI = 分值/难度）：")
    print("-" * 50)
    for ch in get_chapter_priority():
        marker = "★" if ch["must_master"] else " "
        print(f"  {marker} 第{ch['chapter']:2d}章 {ch['name']:<12s} "
              f"分值={ch['weight']:2d}% 难度={ch['difficulty']} ROI={ch['roi']:.1f}")

    print("\n★ = 必须掌握章节")
