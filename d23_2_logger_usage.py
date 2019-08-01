import logging

LOG_FORMAT = "%(asctime)s======%(levelname)s++++++(message)"
logging.basicConfig(filename="log1.txt",level=logging.WARNING,format=LOG_FORMAT)
#参数讲解：
#（1）level代表高于或者等于这个值，那么我们才会记录这条日志
#（2）filename代表日志会写在这个文件之中，如果没有这个字段则会显示在控制台上
#（3）format代表我们的日志显示的格式自定义，如果字段为空，那么默认格式为：level:log_name:content

logging.log(logging.INFO,"This is a INFO log")
logging.log(logging.ERROR,"This is a ERROR log.")

# logging.getLogger()
