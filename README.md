# 物流管理-报表生成项目



## 声明

虽该项目是为校外公司设计，但最终部分需求由于甲方原因并未给全资料，故关于财务部分设计并未继续进行(其他方面均已设计完成)，资金也未完全结清，按规定该软件版权仍归本人所属，时隔半年因实习需要公开软件代码

## 软件相关

+ 软件位置在dist/start/start.exe
+ 数据库请尽量使用mysql数据库，数据库需要进行初始化，创建数据库`transport_db`
+ 打开软件，在左下角配置里可连接到数据库，请按照表单字段正确连接，等待软件弹出连接成功后退出软件
+ 在数据库transport_db的user_password_db 中插入一个账号和密码，grade填写1，该账号密码即该软件的管理员账号密码(账号密码符合命名要求即可)
+ 至此，所有配置均已结束，再次打开软件，使用_刚刚配置的账号密码进行登录，即可登录成功

## 权限说明

+ 在管理员页面 功能-添加 可以添加用户，其中权限

  + 1 代表管理员

  + 2 散货操人员

  + 3 集装箱操人员

  + 4 财务操人员

    管理员可以看到所有的数据

    每个不同权限的人可以在登录后的主表中看到自己的所有的数据，在部门中看到同级别权限的同事的数据

## 表单生成

+ 表单模板在template文件夹下
+ 表单生成的位置在Excel_files下，注意: 取相同的名字则生成的文件会被覆盖

## 模板复用

+ 所有的模板均有对应的.ui文件，每个.ui，除了只有部分代码才能控制的样式基本所有的样式均在.ui文件本身，所有的ui文件及编译后的ui文件均在resource/ui下， 所用图片资源在resource/image下，如果您认为某个模板好看，您可以找到对应的.ui文件及image引入您的项目
+ 还有更多的细节，如历史记录操作，切换账号，数据导出，数据导入到软件等等如果您需要您均可以用于自己的项目

## 最后请记得点下Star

​																									--cmx

​																							          



