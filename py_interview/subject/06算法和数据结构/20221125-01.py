"""
规则如下:
桌面上有数字卡片, 它们对应的数字[A1,A2,A3, .. An](顺序不可变), 你手上卡片的数字有[B1, B2, B3, .. Bn]
按照某个顺序摆放, 若当前位置卡片上的数字大于桌面上的数字, 你就能够积1分, 若不能, 则积0分

如:桌面上卡片的数字[6, 5, 4, 1], 你手中卡片的数字[3, 2, 2, 1],
        如果你按照[3, 2, 1, 2] 摆放, 你就能获得最高1分 ;
        如果你按照[3, 2, 2, 1] 摆放, 你就只能获得0分 ;

请问如何安排卡片顺序, 能够获得的分数最高?
要求: 按照给定桌面上卡片数字的列表, 以及你手上的卡片数字列表, 输出一个元组A, A=(摆放列表, 你能获得的最高分数)
"""

# 这是一个典型的田忌赛马问题

"""
A = [6,5,4,1]
B = [3,2,2,1]
{
    "6":[],
    "5":[],
    "4":[],
    "1":[]
}
sort(A) ---->  [1,4,5,6]
sort(B) ---->  [1,2,2,3]

"""

# 单元测试验证
import pytest
from pydash import collections


def check_hit(t, h):
    """
    # 检查按顺序获得的分数
    :param t: list, 桌面的数字列表
    :param h: list, 手上的数字列表
    :return:  int, 获得的分数
    """
    hit = collections.filter_(list(zip(t, h)), lambda x: x[0] > x[1])
    return len(hit)


@pytest.mark.parametrize('high, low, result, name', [
    ([6, 5, 4, 1], [3, 2, 2, 1], 1, 'demo'),
    ([3, 2, 1], [3, 2, 1], 2, '倒序'),
    (list(range(999))[::-1], list(range(999))[::-1], 999-1, '大量倒序'),
    ([2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2], 0, '全等'),
    ([4, 3, 2, 1, 0, -1], [5, 4, 3, 2, 2, 1], 6, '有负分数'),
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 5, '正序'),
    (list(range(999)), list(range(999)), 999 - 1, '大量正序'),
    ([3, 2, 1, 1, 2, 3], [1, 2, 3, 3, 2, 1], 4, '不定序')
])
def test_get_high_score(high, low, result, name):
    res = get_high_score(high, low)
    print('res', res)
    score = check_hit(res[0], high)
    assert res[1] == result == score


def get_high_score(desk, mine):
    sorted_a_list = sorted(desk)
    sorted_b_list = sorted(mine)
    # 根据desk表创建字典
    assigned_dict = {a: [] for a in sorted_a_list}
    # 创建空列表
    num = []
    score = 0
    for a in sorted_a_list:
        if a > sorted_a_list[score]:
            # 判断a值是否大于desk表最小值
            if a > sorted_b_list[score]:
                # 大于的话，将值放在字典assigned[key=desk中较小的值]：value=mine表中大与他的值
                assigned_dict[sorted_b_list[score]].append(a)
                score += 1
            else:
                # 不符合要求的值放在另一个列表中
                num.append(a)
        res = []
        # 循环desk表
        for b in desk:
            # 判断assigned表中，key对应的value是否存在
            if assigned_dict[b]:
                # 存在说明有大于该值的value，添加到结果列表并删除
                res.append(assigned_dict[b].pop())
            else:
                # 如果没有，说明没有大于该值的value，直接从另一个列表中取一个就可以
                res.append(num.pop())
        print(desk)
        print(res)
        print(score)
        return res, score
