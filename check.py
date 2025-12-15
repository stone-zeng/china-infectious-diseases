import csv
import unittest

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


class TestData(unittest.TestCase):
    def _check_hepatitis(self, row: dict[str, str]):
        a = get(row, "病毒性肝炎")
        b = sum(get(row, i) for i in HEPATITIS)
        return a == b, "病毒性肝炎"

    def _check_level_i_ii(self, row: dict[str, str]):
        a = get(row, "甲乙类传染病合计")
        b = sum(get(row, i) for i in LEVEL_I) + sum(get(row, i) for i in LEVEL_II)
        return a == b, "甲乙类传染病合计"

    def _check_level_iii(self, row: dict[str, str]):
        a = get(row, "丙类传染病合计")
        b = sum(get(row, i) for i in LEVEL_III)
        return a == b or a == 0 or b == 0, "丙类传染病合计"

    def _check_total(self, row: dict[str, str]):
        a = get(row, "甲乙丙类总计")
        b = get(row, "甲乙类传染病合计") + get(row, "丙类传染病合计")
        return a == b or a == 0 or b == 0, "甲乙丙类总计"

    def _check(self, file: str, key: str, exceptions: dict[str, list[str]] = {}):
        checks = [
            self._check_hepatitis,
            self._check_level_i_ii,
            self._check_level_iii,
            self._check_total,
        ]
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in list(reader):
                header = next(iter(row.values()))
                with self.subTest(**{key: header}):
                    for check in checks:
                        res, name = check(row)
                        if not res:
                            if not (name in exceptions and header in exceptions[name]):
                                self.fail(name)

    def test_yearly_cases(self):
        self._check(
            "data/yearly-cases.csv",
            key="year",
            exceptions={
                "甲乙丙类总计": ["2004", "2005", "2006", "2007"],
                "甲乙类传染病合计": ["2002", "2003", "2013"],
                "丙类传染病合计": ["2004", "2005", "2006", "2007"],
            },
        )

    def test_yearly_deaths(self):
        self._check(
            "data/yearly-deaths.csv",
            key="year",
            exceptions={"甲乙类传染病合计": ["2002", "2003", "2013"]},
        )

    def test_monthly_cases(self):
        self._check(
            "data/monthly-cases.csv",
            key="month",
            exceptions={
                "甲乙类传染病合计": [
                    "2004-01",
                    "2004-02",
                    "2004-03",
                    "2004-04",
                    "2004-05",
                    "2004-06",
                    "2004-07",
                    "2004-08",
                    "2004-09",
                    "2004-10",
                    "2004-11",
                    "2004-12",
                    "2007-02",
                ],
                "丙类传染病合计": ["2005-04", "2005-05", "2007-01", "2007-02"],
            },
        )

    def test_monthly_deaths(self):
        self._check(
            "data/monthly-deaths.csv",
            key="month",
            exceptions={"甲乙类传染病合计": ["2004-05", "2004-08", "2006-01"]},
        )
