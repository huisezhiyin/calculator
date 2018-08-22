# coding:utf-8

from itertools import permutations

spring_points_dict = {"ig": 30, "rng": 90, "rw": 50, "jdg": 0, "edg": 70, "west3": 0, "west4": 0, "sng": 0}
summer_points_list = [0, 90, 70, 40, 20, 10]


def expectation_check(origin_list, expect_list):
    # 期望检查
    for team in origin_list:
        if expect_list.index(team) > (origin_list.index(team) + 1):
            return False
    return True


def expect_production(origin_list):
    # 列出所有合法期望
    expect_list = []
    all_combination = list(permutations(origin_list, len(origin_list)))
    for combination in all_combination:
        if expectation_check(origin_list, combination):
            # 期望合法 加入期望队列
            expect_list.append(combination)
    return expect_list


def out_line(team_rank_tuple):
    # 根据春季赛积分计算出线队伍
    team_points_dict = {}
    team_rank_list = list(team_rank_tuple)
    first = team_rank_list[0]
    out_line_list = [first]
    for num in xrange(0, len(team_rank_list)):
        all_points = spring_points_dict[team_rank_list[num]] + summer_points_list[num]
        team_points_dict[team_rank_list[num]] = all_points
    team_points_dict.pop(first)
    result = sorted(team_points_dict.items(), key=lambda d: d[1], reverse=True)
    out_line_list.append(result[0][0])
    out_line_list = sorted(out_line_list, reverse=True)
    return "{0},{1}".format(out_line_list[0], out_line_list[1])


def team_rank_calculator(playoffs_result1, playoffs_result2):
    # 根据两个季后赛赛制循环的所有可能列出所有排名可能
    # 列出所有排名可能
    all_result_list = []
    for result_1 in playoffs_result1:
        for result_2 in playoffs_result2:
            # 列出四种可能
            tmp1 = [result_1[0], result_2[0], result_1[1], result_2[1], result_1[2], result_2[2]]
            tmp2 = [result_2[0], result_1[0], result_1[1], result_2[1], result_1[2], result_2[2]]
            tmp3 = [result_1[0], result_2[0], result_2[1], result_1[1], result_1[2], result_2[2]]
            tmp4 = [result_2[0], result_1[0], result_2[1], result_1[1], result_1[2], result_2[2]]
            all_result_list.append(tmp1)
            all_result_list.append(tmp2)
            all_result_list.append(tmp3)
            all_result_list.append(tmp4)
    return all_result_list


def calculator(playoffs_1, playoffs_2):
    team_probability = {}
    playoffs_result1 = expect_production(playoffs_1)
    playoffs_result2 = expect_production(playoffs_2)
    rank_list = team_rank_calculator(playoffs_result1, playoffs_result2)
    out_line_list = []
    for rank in rank_list:
        out_line_list.append(out_line(rank))
    out_line_tuple = set(out_line_list)
    for team in out_line_tuple:
        # 此处保留两位小数
        probability = round(round(float(out_line_list.count(team)) / len(out_line_list), 2) * 100, 2)
        team_probability[team] = probability
    print team_probability
    for i in spring_points_dict.keys():
        percent = 0
        for key in team_probability.keys():
            if i in key:
                percent += team_probability[key]
        print "{0} : {1}%".format(i, percent)


if __name__ == '__main__':
    playoffs1 = ["rw", "jdg", "west3", "sng"]
    playoffs2 = ["ig", "edg", "rng", "west4"]
    calculator(playoffs1, playoffs2)
