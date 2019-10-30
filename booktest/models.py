from django.db import models


# Create your models here.
class AreaInfo(models.Model):
    '''地区模型类'''
    atitle = models.CharField(verbose_name='标题', max_length=128)  # 地区名
    # 自关联属性
    aParent = models.ForeignKey('self', null=True, blank=True)  # 允许为空，后天也允许为空

    def __str__(self):
        return self.atitle

    def title(self):
        # 重写方法, 方法默认不能排序
        return self.atitle

    # 给方法增加一个属性admin_order_field
    title.admin_order_field = 'atitle'  # 指定方法根据排序的字段
    # title.admin_order_field = 'id'  # 根据属性排序
    title.short_description = '地区名称'  # 指定方法的对应的列的标题

    def parent(self):
        if self.aParent is None:
            return ''
        return self.aParent.atitle  # 返回父级地区地区标题
    parent.short_description = '父级地区名'