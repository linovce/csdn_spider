# CSDN_Spider

#### 介绍
csdn爬虫，爬取后台内容管理的markdown源数据。

#### 使用说明

1.  在CSDNSpider/spiders下创建两个文件夹“文章”、“cookie”
2.  修改CSDN_Articles.py中url为自己的博客地址
3.  运行CSDN_Login.py，微信扫描二维码登录
4.  运行CSDN_spider.py，获取文章ID列表
5.  运行CSDN_Articles.py，获取全部文章
6.  3和5可直接运行，4需要在终端窗口输入命令运行：scrapy crawl csdn_spider

#### 结果预览

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210529174007253.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NTI0MTU3,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210529174119525.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1NTI0MTU3,size_16,color_FFFFFF,t_70)

#### 补充

1.  小弟Python也是自学，如有路过的大佬对代码有建议可在下方留言。