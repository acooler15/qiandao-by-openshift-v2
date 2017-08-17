qiandao by openshift v2
======
程序来自于binux/qiandao(https://github.com/binux/qiandao.git)
只是做了一些修改，增加了对openshift的支持。

#openshift应用部署要求

使用diy方式（Do-It-Yourself）创建应用，可按需求添加cron,mysql,
phpMyAdmin,以及redis。
##可使用的redis添加方法
在创建的应用管理页面，点击"Or, see the entire list of cartridges you can add"，在"install your own cartridge"下方的输入框内填入
`http://cartreflect-claytondev.rhcloud.com/reflect?github=gerardogc2378/openshift-redis-cart`
即可安装redis-3.2.9,详见gerardogc2378/openshift-redis-cart（https://github.com/gerardogc2378/openshift-redis-cart.git ）

##关于python依赖的部署
在openshift部署本应用时，会自动安装依赖，可以在
`${OPENSHIFT_REPO_DIR}.openshift/action_hooks/build`
中见到执行命令，若初次部署时没有安装python依赖，可以手动执行build脚本安装

##python脚本的执行
自定义安装的python是安装在${OPENSHIFT_DATA_DIR}下，所以
执行脚本时需要指定python运行。如，启动应用命令时，执行
    `${OPENSHIFT_DATA_DIR}bin/python2.7 ${OPENSHIFT_REPO_DIR}/diy/run.py`
或者
    `nohup ${OPENSHIFT_DATA_DIR}bin/python2.7 ${OPENSHIFT_REPO_DIR}/diy/run.py > ${OPENSHIFT_DIY_LOG_DIR}server.log 2>&1 &`
也可以直接运行.openshift目录下的start脚本
    `${OPENSHIFT_REPO_DIR}.openshift/action_hooks/start`
，同理，若想要关闭应用，可以运行stop脚本
	`${OPENSHIFT_REPO_DIR}.openshift/action_hooks/stop`

##mysql数据库导入
要求：需已安装mysql
`mysql -h $OPENSHIFT_MYSQL_DB_HOST -P $OPENSHIFT_MYSQL_DB_PORT -u$OPENSHIFT_MYSQL_DB_USERNAME -p$OPENSHIFT_MYSQL_DB_PASSWORD < qiandao.sql`

##注意！！！
若是在windows下使用git命令部署，在push之前请执行
`git update-index --chmod=+x .openshift/action_hooks/*`
以及
`git update-index --chmod=+x .openshift/cron/minutely/*`

##其它请参照binux/qiandao(https://github.com/binux/qiandao.git)