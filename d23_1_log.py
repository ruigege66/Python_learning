color = ["red","yellow","blue","green"]
for green in color:
    print(green)
    if green == "green":
        print("Green")

import logging
logging.debug(msg,*arg,**kwargs)      #创建一条级别为DEBUG的日志​
logging.info(msg,*arg,**kwargs)       #创建一条级别为INFO的日志​
logging.warning(msg,*arg,**kwargs)    #创建一条级别为WARNING的日志​
logging.error(msg,*arg,**kwargs)      #创建一条级别为ERROR的日志​
logging.critical(msg,*arg,**kwargs)   #创建一条级别为CRITICAL的日志​
logging.log(level,*arg,**kwargs)      #创建一条级别为level的日志​
logging.basicConfig(**kwargs)         #对root logger进行一次性配置​
logging.debug("This is a debug log")
#另一种写法
logging.log(logging.DEBUG,"This is a debug log")
