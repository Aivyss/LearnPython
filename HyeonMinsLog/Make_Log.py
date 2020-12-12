import logging
import sys
import inspect

sys.path.append('C:\\Users\\hklei\\PycharmProjects\\HyeonMinsLog')
from Configure_Log import *
from datetime import datetime


class Make_log:
    now = datetime.now()

    def __init__(self, log_onoff):
        self.Name = ".\\" + str(Make_log.now.year) + "-" + str(Make_log.now.month) + "-" + str(
            Make_log.now.day) + ".log"
        self.log_onOff = log_onoff
        self.print_onoff = False  # bool type
        self.config = Configure_Log(self.Name)

        #  어차피 이 객체를 쓴다는거 자체가 log_open을 할텐데 따로 메소드 만들 필요가 있나...?
        self.config.configure(
            '-------------------------------------------------------------------------------- %(message)s --------------------------------------------------------------------------------')
        logging.log(10, self.Name)

    def __init__(self, log_onoff, print_onoff):
        self.Name = ".\\" + str(Make_log.now.year) + "-" + str(Make_log.now.month) + "-" + str(
            Make_log.now.day) + ".log"
        self.log_onOff = log_onoff
        self.print_onoff = print_onoff  # bool type
        self.config = Configure_Log(self.Name)

        #  어차피 이 객체를 쓴다는거 자체가 log_open을 할텐데 따로 메소드 만들 필요가 있나...?
        self.config.configure(
            '-------------------------------------------------------------------------------- %(message)s --------------------------------------------------------------------------------')
        logging.log(10, self.Name)

    def log_l(self, comment, *args):
        if self.log_onOff:
            self.config.configure('%(message)s')

            if len(args) == 0:
                logging.log(10, comment)

            else:
                for str_splt in args:
                    comment = str(comment) + str(str_splt)

                logging.log(10, comment)

            if self.print_onoff:
                print(comment)

    def log_w(self, Comment, *Log_Level):
        if self.log_onOff:
            self.config.configure('[%(asctime)s]: [%(levelname)s] \t  %(message)s')
            Comment_log = ('[%s] ' % str(inspect.currentframe().f_back.f_lineno)) + str(Comment)

            if len(Log_Level) > 0:
                New_Log_Level = str(Log_Level[len(Log_Level) - 1]).lower()
                for str_splt in Log_Level[:-1]:
                    Comment_log = Comment_log + str(str_splt)
                    Comment = str(Comment) + str(str_splt)

            elif len(Log_Level) == 0:
                New_Log_Level = 'debug'

            if (New_Log_Level.upper() == 'DEBUG') or (New_Log_Level.upper() == 'D'):
                logging.log(10, Comment_log)
            elif (New_Log_Level.upper() == 'INFO') or (New_Log_Level.upper() == 'I'):
                logging.log(20, Comment_log)
            elif (New_Log_Level.upper() == 'WARNING') or (New_Log_Level.upper() == 'W'):
                logging.log(30, Comment_log)
            elif (New_Log_Level.upper() == 'ERROR') or (New_Log_Level.upper() == 'E'):
                logging.log(40, Comment_log)
            elif (New_Log_Level.upper() == 'CRITICAL') or (New_Log_Level.upper() == 'C'):
                logging.log(50, Comment_log)
            else:
                Comment_log = Comment_log + str(Log_Level[-1:][0])
                Comment = str(Comment) + str(Log_Level[-1:][0])
                logging.log(10, Comment_log)

            if self.print_onoff:
                print(Comment)


if __name__ == '__main__':

    a = {}
    b = {}
    c = {}

    a["p"] = b
    b["o"] = {1: "a", 2: c}
    c["i"] = {1: "z", 2: "x", 3: "c"}

    log_maker = Make_log(True, True)

    log_maker.log_l('Testing~')
    log_maker.log_l(1, '2', (3), [4], {5})

    log_maker.log_w(Comment='hi')
    log_maker.log_w('hello', 'e')
    log_maker.log_w('wow', 'critical')
    log_maker.log_w("My", " name", " is", " James")
    log_maker.log_w("My", " name", " is ", "c")
    log_maker.log_w('1', 2, '3')
    log_maker.log_w(4, '5', 6)
    log_maker.log_w([1, 2, 3], ['a', 'b', 'c'])
    log_maker.log_w({'a': 1}, {'b': 2})
    log_maker.log_w(1, '2', (3), [4], {5})

    log_maker.log_w('hello', 'e', 'abc')
    log_maker.log_w('hello', 'e', 'abc', 'c')
    log_maker.log_w('hello', 'e', 'abc', 'warning')
    log_maker.log_w('hello', 'e', 'abc', 'lol')

    try:
        1 + '1'
    except Exception as E:
        log_maker.log_w(E)
        log_maker.log_w(E, 'E')
        log_maker.log_w('Error Message: ', E, 'E')

    log_maker.aaa = 10
    print(log_maker.aaa)
