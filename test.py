import os
import shutil


def search_dir(path, result):
    child_files = os.listdir(path)

    for f in child_files:
        child = os.path.join(path, f)
        if os.path.isdir(child):
            search_dir(child, result)
        else:
            result.append(child)


if __name__ == '__main__':
    # for i in range(0, 10):
    #     print("i=%d" % i)

    # rabbit = 3
    # print("请输入N的值：")
    # N = int(input())
    # for i in range(0, N):
    #     rabbit = rabbit * 2
    # print("%d年后，兔子的数量为 %d." % (N, rabbit))

    # print("请输入N的值：")
    # N = int(input())
    # result = 0
    # for i in range(0, N + 1):
    #     result += i
    # print("1+2+...N的值为：%d" % result)

    # num1 = int(input('请输入班级1的学生数量：'))
    # class1 = set()
    # for i in range(0, num1):
    #     name = input("输入学生%d姓名：" % (i + 1))
    #     class1.add(name)
    # num2 = int(input('请输入班级2的学生数量：'))
    # class2 = set()
    # for i in range(0, num2):
    #     name = input("输入学生%d姓名：" % (i + 1))
    #     class2.add(name)
    # same = class1 & class2
    # print("重名的学生：")
    # for s in same:
    #     print(s)

    # class1 = {'Joan', "Bill", 'Niki', 'Mark', 'Mark'}
    # class2 = {'Tom', 'Linda', 'Bill'}
    #
    # diff = class2 - class1
    #
    # for name in diff:
    #     print(name)

    # dict = {'小明': {85, 96, 88}, '小红': {72, 80, 91}, '小亮': {83, 69, 75}}
    # max = 0
    # maxName = None
    # for name in dict:
    #     sum = 0
    #     for score in dict[name]:
    #         sum += score
    #     if sum > max:
    #         max = sum
    #         maxName = name
    # print("分数最高的人位为：%s， 分数为 %d" % (maxName, max))

    # score1 = int(input("请输入第一门成绩："))
    # score2 = int(input("请输入第二门成绩："))
    # score3 = int(input("请输入第三门成绩："))
    # point1 = (score1 > 90) * 2 + ((score1 > 60) & (score1 < 90))
    # point2 = (score2 > 90) * 2 + ((score2 > 60) & (score2 < 90))
    # point3 = (score3 > 90) * 2 + ((score3 > 60) & (score3 < 90))
    # print("%d, %d, %d" % (point1, point2, point3))
    # points = point1 + point2 + point3
    # print(points)

    input_dir = "/Users/momo/Desktop/log"
    output_dir = "/Users/momo/Desktop/log_new"
    files = list()
    search_dir(input_dir, files)
    for f in files:
        print("find %s" % f)
        if os.path.isfile(f) and f.endswith(".json"):
            print("move file %s" % f)
            shutil.move(f, output_dir)
    print("test commit")

