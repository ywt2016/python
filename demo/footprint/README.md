
├── README.md 说明文档
├── javascript 网页版本
│   └── index.html
└── python python版本
    ├── build.py 编译生成文件
    └── config.py 你需要修改的配置文件

```



### python版本

* 下载本项目，进入到python目录下，有两个文件，config是你需要修改的2. 
* 项目依赖于requests模块 需要pip安装

```
config={
	'title':'去过的地方',
	'subtitle':'北京 昆明 西北 呼和浩特',
	'foot':[
		'北京 昆明 丽江 香格里拉 丽江 昆明 北京',
		'霍营地铁站 布达拉宫',
		'北京 北戴河 北京',
		'北京 兰州 敦煌 张掖 祁连 西宁 青海湖 茶卡盐湖 西宁 银川 呼和浩特 北京'
	]
}

```

* 修改上面这个配置里的title(标题),subtitle(副标题)和foot(行程)
* foot是一个数组，每个元素是一个行程，目的地(景点)之间用空格分开
* 执行 python build.py ,会生成一个footprint.html，


### 彩色版本和定制区域


* config加一个color变量，就会把足迹线变成彩色，如下

```
config={
	'title':'去过的地方',
	'subtitle':'北京 昆明 西北 呼和浩特',
	'color':True,
	'foot':[
		'北京 昆明 丽江 香格里拉 丽江 昆明 北京',
		'霍营地铁站 布达拉宫',
		'北京 北戴河 北京',
		'北京 兰州 敦煌 张掖 祁连 西宁 青海湖 茶卡盐湖 西宁 银川 呼和浩特 北京'
	]
}
```

![](http://7xjoq9.com1.z0.glb.clouddn.com/footprint04.gif)


* 如果你只在北京内部玩，或者定制一个北京旅游计划，可以加一个region字段，如下

```
config={
	'title':'北京去过的地方',
	'subtitle':'走啊走',
	'color':True,
	'region':'北京',
	'foot':[
		'北京交通大学 霍营地铁站 古北水镇',
		'北京交通大学 八达岭 北京交通大学',
		'北京交通大学 妙峰山 潭柘寺'
		
	]
}








