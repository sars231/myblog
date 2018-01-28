# myblog
my blog based on django

<<<<<<< HEAD
### 1月27日更新
解决无法提交中文的bug<br>
excption value:(1366, "Incorrect string value: '\\xE6\\xA0\\x87\\xE9\\xA2\\x98' for column 'title' at row 1")<br>
原因是mysql的设置不正确<br>
进入mysql，使用命令"show variables like 'character%'"，查看数据库字符集情况<br>
发现 character-set-server 和  character-set-database 的值为latin1<br>
我们需要将它的默认值改为utf8<br>
编辑  /etc/mysql/mysql.conf.d/mysqld.cnf    在[mysqld]下添加  character-set-server=utf8<br>
systemctl restart mysql  重启 MySQL Server，再此查看字符集变量，发现已经是utf8<br>
这个时候将原来的database删除（drop database 'databasename')，重新再新建一个database（create database 'databasename')，
=======
1月27日更新
解决无法提交中文的bug
excption value:(1366, "Incorrect string value: '\\xE6\\xA0\\x87\\xE9\\xA2\\x98' for column 'title' at row 1")
原因是mysql的设置不正确
进入mysql，使用命令"show variables like 'character%'"，查看数据库字符集情况
发现 character-set-server 和  character-set-database 的值为latin1
我们需要将它的默认值改为utf8
编辑  /etc/mysql/mysql.conf.d/mysqld.cnf    在[mysqld]下添加  character-set-server=utf8
systemctl restart mysql  重启 MySQL Server，再此查看字符集变量，发现已经是utf8
这个时候将原来的database删除（drop database 'databasename')，重新再新建一个database（create database 'databasename')，\n
>>>>>>> 76138d164a8bdc73bd42281ae29b90c4cd0c7abb
问题解决
### 1月28日更新
给django添加富文本编辑器，使用ckedior
在这里参考了Aaron的博客（http://www.aaron-zhao.com/post/1/）。<br>
ckedior开源的github地址：https://github.com/django-ckeditor/django-ckeditor.git<br>
#### md文件编辑器，采用了moedior
Moedior开源的github地址：https://github.com/Moeditor/Moeditor.git<br>
#### Building
1. npm install<br>
2. npm start<br>
##### In China, you may want to replace npm with cnpm for a faster download speed.

npm install cnpm -g --registry=https://registry.npm.taobao.org<br>
cnpm install<br>
cnpm start<br>
