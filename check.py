import csv

HEPATITIS = [
    "甲型肝炎",
    "乙型肝炎",
    "丙型肝炎",
    "丁型肝炎",
    "戊型肝炎",
    "未分型肝炎",
]
LEVEL_I = [
    "鼠疫",
    "霍乱",
]
LEVEL_II = [
    "新型冠状病毒感染",
    "传染性非典型肺炎",
    "艾滋病",
    "病毒性肝炎",
    "脊髓灰质炎",
    "人感染新亚型流感",
    "人感染高致病性禽流感",
    "人感染H7N9禽流感",
    "甲型H1N1流感",
    "麻疹",
    "流行性出血热",
    "狂犬病",
    "流行性乙型脑炎",
    "登革热",
    "猴痘",
    "炭疽",
    "细菌性和阿米巴性痢疾",
    "肺结核",
    "伤寒和副伤寒",
    "流行性脑脊髓膜炎",
    "百日咳",
    "白喉",
    "新生儿破伤风",
    "猩红热",
    "布鲁氏菌病",
    "淋病",
    "梅毒",
    "钩端螺旋体病",
    "血吸虫病",
    "疟疾",
]
LEVEL_III = [
    "流行性感冒",
    "流行性腮腺炎",
    "风疹",
    "急性出血性结膜炎",
    "麻风病",
    "流行性和地方性斑疹伤寒",
    "黑热病",
    "包虫病",
    "丝虫病",
    "手足口病",
    "其他感染性腹泻病",
]


def get(row: dict[str, str], name: str):
    if name not in row:
        return 0
    val = row[name]
    if val == "":
        return 0
    return int(val)


def check_hepatitis(row: dict[str, str]):
    a = get(row, "病毒性肝炎")
    b = sum(get(row, i) for i in HEPATITIS)
    if a != b:
        raise Exception("病毒性肝炎", a, b)


def check_level_i_ii(row: dict[str, str]):
    a = get(row, "甲乙类传染病合计")
    b = sum(get(row, i) for i in LEVEL_I) + sum(get(row, i) for i in LEVEL_II)
    if a != b:
        raise Exception("甲乙类传染病合计", a, b)


def check_level_iii(row: dict[str, str]):
    a = get(row, "丙类传染病合计")
    b = sum(get(row, i) for i in LEVEL_III)
    if a != b and a != 0 and b != 0:
        raise Exception("丙类传染病合计", a, b)


def check_total(row: dict[str, str]):
    a = get(row, "甲乙丙类总计")
    b = get(row, "甲乙类传染病合计") + get(row, "丙类传染病合计")
    if a != b and a != 0 and b != 0:
        raise Exception("甲乙丙类总计", a, b)


def check(file: str, exceptions: dict[str, list[str]] = {}):
    print(f"\n# {file}\n")
    checks = [
        check_hepatitis,
        check_level_i_ii,
        check_level_iii,
        check_total,
    ]
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in list(reader):
            header = next(iter(row.values()))
            errors: list[Exception] = []
            for func in checks:
                try:
                    func(row)
                except Exception as e:
                    name = e.args[0]
                    if not (name in exceptions and header in exceptions[name]):
                        errors.append(e)
            if errors:
                print(f"## {header}")
                for e in errors:
                    print(f"\t{e.args[0]}: {e.args[1]} != {e.args[2]}")


def main():
    check(
        "data/yearly-cases.csv",
        exceptions={
            "甲乙类传染病合计": ["2013"],  # 甲型 H1N1 流感
        },
    )
    check(
        "data/yearly-deaths.csv",
        exceptions={
            "甲乙类传染病合计": ["2013"],  # 甲型 H1N1 流感
        },
    )
    check(
        "data/monthly-cases.csv",
        exceptions={
            "丙类传染病合计": ["2005-04", "2005-05", "2007-01", "2007-02"],
        },
    )
    check("data/monthly-deaths.csv")


if __name__ == "__main__":
    main()
