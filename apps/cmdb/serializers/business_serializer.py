# @Time    : 2019/2/27 10:42
from rest_framework import serializers
from ..models import Business, DeviceInfo


class BusinessSerializer(serializers.ModelSerializer):
    """
    业务序列化
    """
    # 当序列化时出现需求和数据库中的字段名不一致时，可以使用 source 字段连接到数据库中的字段，
    # 如前端要求 {"host": ""}，而数据库中的字段是 {"deviceinfo_set": ""}，可以使用 source 字段连接到数据库中的字段
    hosts = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=DeviceInfo.objects.all(),
                                               source='deviceinfo_set')

    class Meta:
        model = Business
        fields = '__all__'
