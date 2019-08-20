#!/usr/bin/env python
# -*- coding:utf8 -*-

'''
@author  : Winnie
@contact : li_fangyuan@gowild.cn
@time    : 2019/8/20 下午5:51
@description: 

'''

import pandas as pd

train = pd.read_csv('train_set.csv')
val = pd.read_csv('val_set.csv')
test = pd.read_csv('test_set.csv')
print(train.shape, val.shape, test.shape)

map_dict = {
    '琥珀': '你',
    '用户': '我',
    '无主体': '无',
    '用户+琥珀': '双方',
    '第三方': '其他',
}

train['label'] = train['label'].map(lambda x:map_dict[x])
train.to_csv('train_set.csv',index=False)

val['label'] = val['label'].map(lambda x:map_dict[x])
val.to_csv('val_set.csv',index=False)

test['label'] = test['label'].map(lambda x:map_dict[x])
test.to_csv('test_set.csv',index=False)


