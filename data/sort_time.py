import mongoengine as me
from .sort import Sort
'''
{
    "SortTime": {
        "name": "bubble_sort",
        "sorts": ["sort_id1", "sort_id2"]
    }
}
'''
class SortTime(me.Document):
    name = me.StringField(required=True)
    sorts = me.ListField(me.ReferenceField(Sort))

    meta = {
        'db_alias': 'sortdb',
        'collection': 'sort_times'
    }

    def __str__(self):
        return f" name = {self.name} sorts = {self.sorts}"