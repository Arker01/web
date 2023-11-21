from django.db import models

ID_LEN = 30
PASSWORD_LEN = 20
NAME_LEN = 10
PHONE_LEN = 11


# Create your models here.


class CCharField(models.Field):  # mysql中没有固定长字符串的东西，所以我们得自定义一个
    def db_type(self, connection):
        return 'char(%s)' % self.max_length


class Consumer(models.Model):
    Cid = models.CharField(primary_key=True, max_length=ID_LEN, verbose_name='账号')
    password = models.CharField(max_length=PASSWORD_LEN, verbose_name='密码')
    name = models.CharField(max_length=NAME_LEN, verbose_name='姓名')
    phone = CCharField(max_length=PHONE_LEN, verbose_name='电话')
    birth = models.DateField(verbose_name='生日')

    # 定义默认输出格式
    def __str__(self):
        return "%s:%s:%s:%s:%s" % (self.Cid, self.password, self.name, self.phone, self.birth)

    # 自定义对应的表名
    class Meta:
        db_table = "consumer"
        verbose_name = '消费者客户信息'
        verbose_name_plural = '消费者客户信息管理'


class Store(models.Model):
    Sid = models.CharField(primary_key=True, max_length=ID_LEN, verbose_name='店铺编号')
    Sname = models.CharField(max_length=NAME_LEN, verbose_name='店名')
    location = models.CharField(max_length=NAME_LEN, verbose_name='店铺地址')
    type = models.CharField(max_length=ID_LEN, verbose_name='店铺类型')
    year = models.DateField(verbose_name='创办年份')

    # 定义默认输出格式
    def __str__(self):
        return "%s:%s:%s:%s:%s" % (self.Sid, self.Sname, self.location, self.type, self.year)

    # 自定义对应的表名
    class Meta:
        db_table = "store"
        verbose_name = '店铺信息'
        verbose_name_plural = '店铺信息管理'


class Goods(models.Model):
    Gid = models.CharField(primary_key=True, max_length=ID_LEN, verbose_name='商品编号')
    Gname = models.CharField(max_length=NAME_LEN, verbose_name='商品名')
    type = models.CharField(max_length=ID_LEN, verbose_name='商品类型')
    price = models.IntegerField(verbose_name='商品类型')

    # 定义默认输出格式
    def __str__(self):
        return "%s:%s:%s:%s" % (self.Gid, self.Gname, self.type, self.price)

    # 自定义对应的表名
    class Meta:
        db_table = "goods"
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息管理'


class Comment(models.Model):
    Coid = models.CharField(primary_key=True, max_length=ID_LEN, verbose_name='评价编号')
    level = models.IntegerField(max_length=NAME_LEN, verbose_name='评价星级')
    comment = models.TextField(max_length=1000, verbose_name='评价内容')
    day = models.DateField(verbose_name='评价日期')
    person_id = models.CharField(foreign_key=True,max_length=ID_LEN,verbose_name="评价人账号")

    # 定义默认输出格式
    def __str__(self):

        return "%s:%s:%s:%s:%s" % (self.Coid, self.level, self.comment, self.day,self.person_id)

    # 自定义对应的表名
    class Meta:
        db_table = "comment"
        verbose_name = '评价信息'
        verbose_name_plural = '评价信息管理'


class Reply(models.Model):
    Rid = models.CharField(primary_key=True, max_length=ID_LEN, verbose_name='回复编号')
    comment = models.TextField(max_length=1000, verbose_name='回复内容')
    date = models.DateField(verbose_name='回复日期')
    person_id = models.CharField(foreign_key=True,max_length=ID_LEN,verbose_name="回复人账号")

    # 定义默认输出格式
    def __str__(self):

        return "%s:%s:%s:%s" % (self.Rid, self.comment, self.date,self.person_id)

    # 自定义对应的表名
    class Meta:
        db_table = "reply"
        verbose_name = '回复信息'
        verbose_name_plural = '回复信息管理'


class Owner(models.Model):
    Oid = models.CharField(primary_key=True, max_length=ID_LEN, verbose_name='商家账号')
    password = models.CharField(max_length=PASSWORD_LEN, verbose_name='密码')
    name = models.CharField(max_length=NAME_LEN, verbose_name='商家姓名')
    phone = CCharField(max_length=PHONE_LEN, verbose_name='商家电话')

    # 定义默认输出格式
    def __str__(self):
        return "%s:%s:%s:%s" % (self.Oid, self.password, self.name, self.phone)

    # 自定义对应的表名
    class Meta:
        db_table = "owner"
        verbose_name = '商家信息'
        verbose_name_plural = '商家信息管理'
