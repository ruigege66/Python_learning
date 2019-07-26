#使用shelve创建文件并使用
import shelve
shv = shelve.open(r"shv.db")
shv["one"] = 1
shv["two"] = 2

shv.close()

shv = shelve.open(r"shv.db")
try:
    print(shv["one"])
    print(shv["three"])
except:
    print("打印three时出错了")
finally:
    shv.close()

shv = shelve.open(r"shv.db",writeback=True)
try:
    shv["one"] = {"eind":1,"zwei":2,"drei":3}
    one = shv["one"]
    print(one)
    # 这里就对 数据进行了更改，如果没有上面writeback=True,下面额语句就白写了​
    one["eind"] = 100
    print(one)
finally:
    shv.close()

