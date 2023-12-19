def check_view(_view,_num):
    if '万' in _view:
        return True
    else:
        lis = []
        for _i in _view:
            if _i == '次':
                lis = ''.join(lis)
                lis = int(lis)
                break
            else:
                lis.append(_i)
        if lis >= _num:
            return True
        else:
            return False

def check_time(_time):
    if '年' in _time or '月' in _time or '周' in _time:
        return True
    elif '天' in _time or '小时' in _time or '分钟' in _time:
        return False

def a(_ViewAndTime):
    index = -1
    for x in _ViewAndTime:
        index += 1
        view,time = x.split(' · ')
        bool_view = check_view(view,1000)
        bool_time = check_time(time)
        if bool_view and bool_time:
            _ViewAndTime[index] = True
        else:
            _ViewAndTime[index] = False
    return _ViewAndTime
