
下载gitlab 社区版
https://packages.gitlab.com/gitlab/gitlab-ce

下载对应系统的policycoreutils-python

http://www.rpmfind.net/linux/rpm2html/search.php?query=policycoreutils-python

依赖太多 可用yum
>yum install policycoreutils-python

赋权给对应用户
>chown -R gitlab /home/gitlab

sudo里增加 
>username ALL=(ALL) ALL
修改sudo权限
>chmod 440 /etc/sudoers

安装
>sudo rpm -ivh ./gitlab-ce-11.11.3-ce.0.el6.x86_64.rpm


>chown -R gitlab /etc/gitlab

修改配置文件 
>/ect/gitlab/gitlab.rb
>external_url 为ip地址 http://123.321.123.1:9099

检查配置
>gitlab-ctl check-config

重载config
>gitlab-ctl reconfigure 

启动后502
>gitlab-ctl tail
看日志
unicorn 端口冲突

先停止
>gitlab-ctl stop

>/var/opt/gitlab/gitlab-rails/etc/unicorn.rb
修改
>listen "123.123.123.123:9098", :tcp_nopush => true 

重启动
>gitlab-ctl restart 



>ssh-keygen -C "xxx@xxx.com"

GitLab: API is not accessible 

修改
>opt/gitlab/embedded/service/gitlab-shell/config.yml
>gitlab_url : "123.123.123.123:9099"

参考
https://wiki.archlinux.org/index.php?title=Gitlab_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)&oldid=558848
