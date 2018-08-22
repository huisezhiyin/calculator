# coding:utf-8
from itertools import combinations, permutations

spring_points_dict = {"ig": 30, "rng": 90, "rw": 50, "jdg": 0, "edg": 70, "*": 0}
summer_points_list = [90, 70, 50, 30, 10]


def calculator(team_list, team_summer_bottom):
    team_probability = {}
    result_list = []
    # 列出所有可能的排名组合
    all_combination = list(permutations(team_list, len(team_list)))
    for combination in all_combination:
        # 目前仅可以知晓ig rw不会低于前四
        result_one = out_line(combination, team_summer_bottom)
        if result_one:
            result_list.append(result_one)
    print len(result_list)
    result_tuple = set(result_list)
    for team in result_tuple:
        # 此处保留两位小数
        probability = round(round(float(result_list.count(team)) / len(result_list), 2) * 100, 2)
        team_probability[team] = probability
    print team_probability
    for i in team_list:
        percent = 0
        for key in team_probability.keys():
            if i in key:
                percent += team_probability[key]
        print "{0}:{1}".format(i, percent)


def out_line(team_rank_tuple, team_summer_bottom):
    # 出线计算器
    # 夏季赛排名状况
    team_rank_list = list(team_rank_tuple)
    for team in team_summer_bottom.keys():
        if team_rank_list.index(team) >= team_summer_bottom[team]:
            return False
    team_points_dict = {}
    # 第一名直接出线
    first = team_rank_list[0]
    out_line_list = [first]
    team_rank_list.remove(first)
    # 计算所有队伍的总积分
    for num in xrange(0, len(team_rank_list)):
        all_points = spring_points_dict[team_rank_list[num]] + summer_points_list[num]
        team_points_dict[team_rank_list[num]] = all_points
    result = sorted(team_points_dict.items(), key=lambda d: d[1], reverse=True)
    out_line_list.append(result[0][0])
    # 不关心第一名或第二名
    out_line_list = sorted(out_line_list, reverse=True)
    return "{0},{1}".format(out_line_list[0], out_line_list[1])


if __name__ == '__main__':
    team_list = ["ig", "rng", "rw", "jdg", "edg", '*']
    team_summer_bottom = {"ig": 4, "rw": 4}
    calculator(team_list, team_summer_bottom)
