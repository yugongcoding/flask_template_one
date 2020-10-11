# 自我简介
无名编码狮，爱好编码，个人blog网站[http://www.skj.kim](http://www.skj.kim),网站服务器比较辣鸡哈，第一次访问速度比较慢，就用来记录一些CSDN审核不容易通过的博客，底层使用wordpress，模板也是网站找的。

如果想要快速搭建自己的博客网站写一些博客啊、日记啊什么的，可以私信滴滴我哦！

# 前言
这篇文章保证新手也能看得懂，看不懂的童鞋不要着急，文章最后我会做一个总结，即项目怒整体的运行思路，相信大家看完会一目了然~~

Flask十分灵活，可以自己设计代码的架构，而不像django那样把代码的架构设计好了给你使用，这里说的代码架构就是我们项目的目录设计。

另外JAVA的spring，也是把代码架构配置好的，我们可以现成使用，而Flask只是提供了一个基础框架，在这个基础的框架上可以开发很多个插件供我们使用，在github上有许多基于flask开发的扩展插件，我们可以根据自己爱好以及项目需求选择不同的扩展插件来使用。

接下来，我将详细介绍使用flask开发web常用的代码架构以及技术栈，这里所谓的技术栈就是我们使用的一些框架，这些框架的互相配合就形成了我们的技术栈。

# 代码架构
上面我们讲过了，代码架构就是项目目录的构成，先贴张图大家看了会一目了然，这个代码架构模板我放在github上了，有兴趣的可以去查看，[代码架构模板（一）https://github.com/Alan-Rick/flask_template_one](https://github.com/Alan-Rick/flask_template_one)，这里为什么是代码架构模板一呢，因为flask太灵活了，还有很多其他的代码架构供我们选择，这篇文章我们暂且说我自己常用的这个模板。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201011090305665.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzA1OTI4NQ==,size_16,color_FFFFFF,t_70#pic_center)
上图中左边红色框框内就是我们的目录配置，因为放在github的，所以顺手搞了个LICENSE，瞎玩玩而已，没啥特定意义，下面我们详细解释下各个目录的作用。

# 目录flask_template_one
这个目录是我们项目所在目录，所有的代码都放在这里面，目录名字可以设置为自己的项目名称。

# 目录server
可以看待目录server在flask_template_one的下一级，这里是起名为server是因为我们的项目核心代码都放在这里面，代码组成了一个供他人使用的服务，所以就起名server好了；
# 目录api
这个目录里面放的是我们的接口代码，由于现在前后端分离以及微服务的兴起，后端只需要写一些接口给前端调用即可，所以我们把所有的接口都集成在这个文件夹里面，看一下里面的代码构成吧！

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020101109121981.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzA1OTI4NQ==,size_16,color_FFFFFF,t_70#pic_center)
这里我们使用的是flask的蓝图框架，针对不同的应用创建不同的蓝图，方便我们管理，蓝图可以看作是项目构成的一部分，就像房子是由门窗、砖头水泥的组合，这些门窗啊水泥啊都可以看作是蓝图，这些蓝图拼凑在一起，就构成了我们项目的最终形态。

蓝图示例代码如下：

```python
# 导入需要的包文件
from flask import Blueprint, request
from flask_restx import Api, Resource

"""
创建一个蓝图，相当于创建项目组成的一部分，主要是方便我们管理自己的项目；

比如你的项目由很多个子项目构成，那么把为每一个子项目创建一个蓝图来创建对应的接口，好过于
把所有的接口都放在同一个.py文件吧！

这里创建蓝图Blueprint类还有很多其他的参数可选，大家可以看Blueprint类的源码，里面介绍的很清晰，英文不好的童鞋
请自觉学习英文；
"""
app_one_api = Blueprint('app_one_api', __name__)
"""
初始化我们的蓝图，它的作用是把我们的蓝图当作装饰器，修饰我们的类以及方法，
使得我们可以创建一个类，然后在类下面写不同的请求方法，比如get方法用来接收get请求，
post方法用来接收post请求，对于不同的方法返回不同的内容，看起来好像增加了代码量，实际上
却更容易对项目进行管理；
"""
api_one = Api(app_one_api)


"""
建立路由  有了路由可以建立相应的网络请求链接  并且可以对同一个链接发送不同的请求  节省视图的创建；

这里就是上面我们所说的Api()这个类的作用，通过它创建路由装饰器，然后装饰我们的类，在类下面写不同的请求方法，在接收到不同的请求时，
这个装饰器会将不同的请求转接到对应的类下面的方法；

@staticmethod将类内的方法修饰为静态方法，可以外部直接调用，也可以由类生成的对象调用；

接口是项目的核心部分，通过这个技术栈，童鞋你就可以愉快地写接口代码了；

"""
@api_one.route('/')
class Wss(Resource):

    # 接收get请求
    @staticmethod
    def get():
        print('hello world')
        return 'hello world'

    # 接收post请求
    @staticmethod
    def post():
        json_data = request.json
        print(json_data)
        return 'hello world'

    # 接收put请求
    @staticmethod
    def put():
        print('hello world')
        return 'hello world'


if __name__ == '__main__':
    import requests
    import json
    res_one = requests.get('http://127.0.0.1:5000/hello')
    res_two = requests.post('http://127.0.0.1:5000/hello', json=json.dumps({"a": "1"}))
    res_three = requests.put('http://127.0.0.1:5000/hello')
    print(res_one)
    print(res_two)
    print(res_three)
```
这里使用flask_restx来快速并且更加规范的构成我们的项目接口，至于代码的解释都写在上面的代码块中了，不懂得童鞋要多看看文章啦，甚至要看看源码函数介绍。正所谓实践出真理，师傅领进门，至于自己怎么理解还得靠自己领悟。

另外我们的接口集成文件，api_server.py代码如下，通过这个文件可以启动我们的项目：

```python
# -*- coding: utf-8 -*-
from flask import Flask
# 导入蓝图
from server.api.application_one.app_one_views import app_one_api
from server.api.application_two.app_two_views import app_two_api
import socket

api_server = Flask(__name__)
# 注册蓝图  也就是把接口集成起来，构成我们完整的服务项目
api_server.register_blueprint(app_one_api)
api_server.register_blueprint(app_two_api)


if __name__ == '__main__':
    api_server.run(host='0.0.0.0', port=5000, debug=True)

```

# 目录config
这个目录放置一些我们可以修改的东西，并且被其它文件经常调用的一些配置，也就是配置文件啦，不同的配置会使得程序做不同的事情，我这里其实就配置了数据库的接口；

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201011094031645.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzA1OTI4NQ==,size_16,color_FFFFFF,t_70#pic_center)
如上图，当然这里只是一个模板，在实际项目中可能要配置很多其他的东西，比如数据库接口，ORM配置，hadoop接口等等，根据项目构成配置不同的代码；

# 目录dbs
这个目录下的文件是我们创建连接数据库会话的文件，这里我使用的是ORM架构，使用ORM来访问数据库，当然你也可以使用pymysql等其它连接数据库的框架来使用原生sql语句访问数据库；

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201011094354927.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzA1OTI4NQ==,size_16,color_FFFFFF,t_70#pic_center)
代码解释在如下代码块中：

```python
# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from functools import partial
from contextlib import contextmanager
from server.config.setting import db_url
import logging


@contextmanager
def create_session(db_session):
    """
    创建一个会话生成器  不占用内存且具有上下文作用
    :param db_session: 一个虚拟的数据库会话对象
    :return: None Return
    """
    sess = db_session()
    try:
        # yield以上的代码是在上下文进入的时候执行  离开时执行下面的代码
        yield sess
        sess.commit()
    except Exception as e:
        # 出错的话则回滚
        logging.debug(str(e))
        sess.rollback()
    else:
        # 没出错则关闭会话连接
        sess.close()


# 创建物理连接  创建成功则输出
engine_one = create_engine(db_url['data_base_one'], echo=True)
# 创建虚拟连接  可以创建多个数据库连接对象
session_one = sessionmaker(bind=engine_one)
# 创建持久会话  可以创建多个数据库持久化连接会话
# partial的作用相当于把一个上下文函数编程一个类，这样我们可以通过with语句来操作上下文
# 使用方法是    
# with session_zs() as session:
#         print(session_zs)
#         print(session)
#         session.query()
session_zs = partial(create_session, db_session=session_one)


if __name__ == '__main__':
    with session_zs() as session:
        print(session_zs)
        print(session)
```
# 目录models
这个目录是放置我们的数据库表对象的文件，因为我们使用的是ORM来访问数据库，所以要先建立数据库表映射到对象的模型，ORM其实就是把数据库的表映射成一个对象，每一行数据都映射为Python的对象，对象的属性就是数据库表对应的数据，这样做好像方便我们访问数据库，但是也损失了一部分性能，，这是因为将数据库取出的数据转换为对象以及类型映射都需要花费时间。

我们看一下这部分的代码：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201011100708534.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzA1OTI4NQ==,size_16,color_FFFFFF,t_70#pic_center)
同样的，代码的解释都在下面贴出的原始代码中：

```python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Float, JSON, DATE, Text
from sqlalchemy.ext.declarative import declarative_base
from server.dbs.db import engine_one, session_zs
# 创建基础的元数据
base_one = declarative_base()


# 创建表对象orm,继承base_one
# 这里类名User就相当于数据库的表映射成的对象
# __tablename__指定我们的表名
# id name sex指定了类的属性，对应数据库表的字段名
class User(base_one):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    sex = Column(JSON)


if __name__ == '__main__':
    import json
    # 创建所有的与base_one关联的实体表
    base_one.metadata.create_all(bind=engine_one)

```
# 目录static
这个目录防止一些静态文件，比如图片、.html文件，js文件，pdf文件啊，视频啊等等；

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201011101139901.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzA1OTI4NQ==,size_16,color_FFFFFF,t_70#pic_center)
这一部分就是一些静态文件，比较简单，至于怎么通过http访问这些静态文件，我们后面会讲到。

# 目录templates
这个目录放置的是html模板文件，使用MVC架构的时候会使用到，鉴于现在都是前后端分离的问服务架构，所以这路我就没有加上这个目录，根据自己项目的实际情况进行添加吧，在github上我会逐步更新完善这样的架构，欢迎大家去githb查看。

# 总结
以上介绍了每个目录的作用，接下来我们梳理一下项目的整体运作流程：

## 第一步：启动项目
我们启动api文件夹下的api_server.py文件，ok那么现在我们的项目已经运作起来了；
## 第二步：处理请求
假设现在前端通过异步请求，发送过来一个get方式的请求，比如我们项目启动后，对应的ip以及接口是http://127.0.0.1:5000,这个时候前端发送过来一个请求链接是htpp://127.0.0.1:5000/,看到没，后面多了一个‘/’，这个多出来的‘/’就是路由，这个路由正好被我们的蓝图发现了，如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201011102312969.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzA1OTI4NQ==,size_16,color_FFFFFF,t_70#pic_center)
这个蓝图发现，请求的路由它正好有，而且是get请求，于是它把这个请求转发给这个路由下对应的get方法，get方法执行后把结果通过return返回给前端，前端接收到后端发送来的数据后再渲染在前端页面上，至此，一次http请求就完成了。

当然这只是一个简单的请求过程，对于复杂的项目还有其它许多的配置啊等等，不过再复杂的项目，也离不开我们基础的代码架构以及技术栈，只是积少成多，逐渐迭代的过程，这些代码机构以及技术栈都是可以复用的！

## 第三步：访问数据库
如第二步所示，当我们的后端接收到前端发送来的请求后，会根据请求的方式转发到不同的方法处理，那么我们如何访问数据库呢，上面我们已经创建了数据库的虚拟会话，接下来，我们通过访问数据库查询需要的数据，然后把查询到的数据返回给前端。

```python
# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from functools import partial
from contextlib import contextmanager
from server.config.setting import db_url
import logging


@contextmanager
def create_session(db_session):
    """
    创建一个会话生成器  不占用内存且具有上下文作用
    :param db_session: 一个虚拟的数据库会话对象
    :return: None Return
    """
    sess = db_session()
    try:
        # yield以上的代码是在上下文进入的时候执行  离开时执行下面的代码
        yield sess
        sess.commit()
    except Exception as e:
        # 出错的话则回滚
        logging.debug(str(e))
        sess.rollback()
    else:
        # 没出错则关闭会话连接
        sess.close()


# 创建物理连接  创建成功则输出
engine_one = create_engine(db_url['data_base_one'], echo=True)
# 创建虚拟连接  可以创建多个数据库连接对象
session_one = sessionmaker(bind=engine_one)
# 创建持久会话  可以创建多个数据库持久化连接会话
# partial的作用相当于把一个上下文函数编程一个类，这样我们可以通过with语句来操作上下文
# 使用方法是
# with session_zs() as session:
#         print(session_zs)
#         print(session)
#         session.query()
session_zs = partial(create_session, db_session=session_one)


if __name__ == '__main__':
    from server.models.example_model.example_model import User
    with session_zs() as session:
        data = session.query(User).all()
        print(session_zs)
        print(session)

```
上面我们创建了session_zs 这个对象，可以看作一个类，然后我们使用with语句来查询书库：

```python
from server.models.example_model.example_model import User
with session_zs() as session:
    data = session.query(User).all()
    print(session_zs)
    print(session)
```
如上代码，加入说我们查询的数据是user表的数据，返回值为data，那么接第二步处理请求哪里，可以将此查询到的数据返回给前端使用。

这里就用到了我们创建的ORM实体对象模型models，这就是ORM的魅力！

# 结语
这篇文章写的比较粗糙，因为我不是太喜欢写文章，写文章真的非常浪费时间，尤其是写一篇想让别人看得懂的文章，做笔记和写文章真的是非常不一样的，笔记只要自己看得懂，忘记的时候查看即可，而文章就不一样了，文章是为了让其他人看得懂；

所以，大家有不懂的可以私信问我吧，这篇文章我有空再做完善，毕竟这要真的写起来可以写一本书的，谢谢阅读！