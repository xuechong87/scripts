//增加到暂存区
git add (*)

//提交到repo
git commit -m <comment> (-a 全部提交)

//查看暂存区状态
git status (-v 查看文件详情)

//推送到远程仓库
git push <repoName> <branchName>


git diff  <filepath> 工作区与暂存区比较

git diff HEAD <filepath> 工作区与HEAD ( 当前工作分支) 比较

git diff --staged 或 --cached  <filepath> 暂存区与HEAD比较

git diff <branchName> <filepath>  当前分支的文件与branchName 分支的文件进行比较

git diff <commit_id> <filepath> 与某一次提交进行比较

//查看远程分支
git branch -a

//创建分支
git branch <branchName>

//删除分支(本地)
git branch -d <branchName>

//删除分支(远程)
git push origin --delete <branchName> 

//切换分支
git checkout <branchName>

//合并 把branchName合并到当前分支
git merge <branchName>

//根据版本号创建tag
git tag -a <tag name> <versionid> -m <comments> 

//提交tag到远程库
git push origin --tag

//获取远程tag
git fetch origin tag <tagname>	

//删除远程tag
git push origin --delete tag <tagname>


找到需要回退的那次commit的 哈希值
git log

git reset --hard commit_id 

//查看所有分支记录\
后续由金科人员参与并把控运维时间处理工作,严格执行每个事件必须录入系统记录，并按业务条线和问题类型进行分类，完善每日每周每月的问题汇总记录机制，归纳数据作为后续系统优化的参考。 

git log -g 

//将某个提交复制到当前的分支内
git cherry-pick <commit_id> 


//将本地分支push到远程指定分值上
git push origin <local_branch>:<remote_branch>

这个操作，local_branch必须为你本地存在的分支，remote_branch为远程分支，如果remote_branch不存在则会自动创建分支。

类似，git push origin :remote_branch，local_branch留空的话则是删除远程remote_branch分支。



//revert

git revert用于反转提交,执行evert命令时要求工作树必须是干净的.

git revert用一个新提交来消除一个历史提交所做的任何修改.

revert 之后你的本地代码会回滚到指定的历史版本,这时你再 git push 既可以把线上的代码更新.(这里不会像reset造成冲突的问题)



revert 使用,需要先找到你想回滚版本唯一的commit标识代码,可以用 git log 或者在adgit搭建的web环境历史提交记录里查看.

git revert c011eb3c20ba6fb38cc94fe5a8dda366a3990c61
通常,前几位即可

git revert c011eb3


git revert是用一次新的commit来回滚之前的commit，git reset是直接删除指定的commit

看似达到的效果是一样的,其实完全不同.

第一:

上面我们说的如果你已经push到线上代码库, reset 删除指定commit以后,你git push可能导致一大堆冲突.但是revert 并不会.

第二:

如果在日后现有分支和历史分支需要合并的时候,reset 恢复部分的代码依然会出现在历史分支里.但是revert 方向提交的commit 并不会出现在历史分支里.

第三:

reset 是在正常的commit历史中,删除了指定的commit,这时 HEAD 是向后移动了,而 revert 是在正常的commit历史中再commit一次,只不过是反向提交,他的 HEAD 是一直向前的.


//撤销本地commit 
git reset --hard HEAD^

//撤消操作
git commit --amend

有时候我们提交完了才发现漏掉了几个文件没有添加，或者提交信息写错了。 此时，可以运行带有 --amend 选
项的提交命令尝试重新提交：
$ git commit -m 'initial commit'
$ git add forgotten_file
$ git commit --amend

//取消暂存的文件
git reset HEAD <filename>


//撤消对文件的修改
git checkout -- [file] 


// git svn 

//git-svn clone svn_repository
git svn clone svn_repository	

//获取中心svn repository的更新
git svn rebase

//将本地git库的修改同步到中心svn库
git svn dcommit

如果你正在提交的文件在svn服务器上已经被别人改过，就会发生提交冲突。通常解决方法如下：
首先使用git-svn rebase获取svn服务器上的最新冲突文件，比如：conflict.c，这将导致与本地conflict.c冲突，不过此时svn版本信息已经添加到本地git库中(通过git log可以查看)，git-svn rebase提示你在解决conflict.c的冲突后，运行git rebase –continue完成rebase操作
打开conflict.c，修改代码，解决冲突
执行git rebase –continue，git提示：You must edit all merge conflicts and then mark them as resolved using git add
执行git add conflict.c，告知git已完成冲突解决
再次执行git rebase –continue，提示”Applying: git xxx”，此时”git xxx”版本又一次成功加入本地版本库，可通过git log查看；
执行git-svn dcommit将conflict.c的改动同步到svn中心库，到此算是完成一次冲突解决。




///git submodule

//增加一个子模块
git submodule add <gitpath> <nickName>
//example : git submodule add git@github.com:eastlending/eastlending_external.git external

//初始化子模块:在检出工程后需要先初始化子模块才能更新
git submodule init 

//更新子模块代码
git submodule update

====

如果我们git clone的下载代码的时候是连接的https://而不是git@git (ssh)的形式，当我们操作git pull/push到远程的时候，总是提示我们输入账号和密码才能操作成功，频繁的输入账号和密码会很麻烦。

解决办法：

git bash进入你的项目目录，输入：

git config --global credential.helper store
