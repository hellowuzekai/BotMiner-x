loader
------
解析pcap文件，结果存入MySQL数据库。

### 准备工作

* MySQL环境 `sudo apt-get install mysql-server mysql-client`
* 启动MySQL服务 `sudo service mysql start`

### 初次使用

* 编辑数据库配置 `vi loader/config.py`
* 建立数据表结构 `python loader/main.py --init`

### 切分数据包（使用data文件夹下的示例数据，按1000个包切分）

* `mkdir testdata`
* `editcap -c 1000 ../data/bot-brute-2.pcap ./testdata/small.pcap`

### 数据入库

* `python main.py ./data2 <GROUP_ID> <TIME> <NOTE>`

```html
<GROUP_ID> 数据组别，与已有重复会报错
<TIME>     添加数据的时间，不重要。
<NOTE>     备注信息（数据内容描述、上传者等）
```

命令行输出：
```
[loader] Total pcap files: 177
[loader] 1/177 finished.
[loader] 2/177 finished.
...
[loader] 175/177 finished.
[loader] 176/177 finished.
[loader] 177/177 finished.
```

botminer
--------
以`GROUP_ID`检索，从库中提取指定的Packets，分类计算flow/cflow值，生成8/52维向量。

### TODO

* 划分13个区间逻辑错误待修改
* epoch 24小时不合理，待改进
* cflow划分方式尝试只按ip_src分类
* 核心算法(x-means/others)待添加

web
---
flask开发展示界面