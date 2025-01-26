from string_utils import StringUtils
#
utils = StringUtils()
#
#
# print(utils.capitilize(None))

text = '1-2-3'
separator = '-'
a = utils.to_list(text, separator)

utils.to_list(text, separator)

print(type(a))
