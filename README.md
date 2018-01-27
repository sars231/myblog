# myblog
my blog based on django

1月27日更新
解决无法提交中文的bug
excption value:(1366, "Incorrect string value: '\\xE6\\xA0\\x87\\xE9\\xA2\\x98' for column 'title' at row 1")
原因是mysql的设置不正确
进入mysql，使用命令"show variables like 'character%'"，查看数据库字符集情况
发现 character-set-server 和  character-set-database 的值为latin1
我们需要将它的默认值改为utf8
编辑  /etc/mysql/mysql.conf.d/mysqld.cnf    在[mysqld]下添加  character-set-server=utf8
systemctl restart mysql  重启 MySQL Server，再此查看字符集变量，发现已经是utf8
这个时候将原来的database删除（drop database 'databasename')，重新再新建一个database（create database 'databasename')，
问题解决
