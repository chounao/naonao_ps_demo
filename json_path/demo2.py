import json
# from jsonpath_ng import jsonpath, parse
import jsonpath
# 示例 JSON 数据
json_data = '''
{
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}
'''

# 将 JSON 数据解析为 Python 对象
data = json.loads(json_data)
a = jsonpath.jsonpath(data,'$.store.book[*].author')
print(a)
# # 使用 jsonpath 查询并提取数据
# author_expr = parse('$.store.book[*].author')
#
# authors = [match.value for match in author_expr.find(data)]
# print('Authors:', authors)
#
# # Output: Authors: ['Nigel Rees', 'Evelyn Waugh']
#
# price_expr = parse('$.store.book[*].price')
# prices = [match.value for match in price_expr.find(data)]
# print('Prices:', prices)
# # Output: Prices: [8.95, 12.99]
