# 链家二手房源爬取

> 本项目用到的非自带库有：requests，pandas，numpy，xpinyin，lxml

## 简介

- 数据来源：链家二手房
- 爬取内容：房源信息，如下：

```python
self.column = [
    '标题', '介绍', '小区', '价格（万元）', '平米单价（元）', '建筑面积（平米）', '套内面积（平米）',
    '大区域', '小区域', '户型', '朝向', '所在楼层', '装修情况', '户型结构', '建筑类型', '建筑结构',
    '建造时间', '房屋用途', '挂牌时间', '上次交易时间', '房屋年限', '产权所属', '配备电梯', '梯户比例'
]
```

- 所用到的相关工具
    - 使用 request 获取 html 内容
    - 使用 Xpath 语法解析 html 内容
    - 使用 pandas 整理数据
    - 使用 tkinter 构建 GUI 界面
    - 使用 xpinyin 将中文转换为拼音
- 数据截图

<img src="http://image.trouvaille0198.top/image-20210205094644595.png" alt="image-20210205094644595" style="zoom:67%;" />

<img src="http://image.trouvaille0198.top/image-20210205094702637.png" alt="image-20210205094702637" style="zoom:67%;" />

- 程序截图

<img src="http://image.trouvaille0198.top/image-20210204212130209.png" alt="image-20210204212130209" style="zoom:67%;" />

## 实现的功能

1. 指定城市、地区
2. 指定爬取页数
3. 以 `.csv` 格式保存数据
4. 指定保存路径

## 计划实(gu)现(gu)的功能

1. 美化 GUI 

2. 简化代码

3. 增添代码注释

4. 实现终端方案（历史的后退？）

5. 尝试使用 pyqt 构造界面

6. 尝试使用简单的机器学习算法来预测房价（当然结果不好就不会放出来了）

    

