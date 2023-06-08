# 读取包含所有代码和地址的txt文件
with open("all_codes.txt", "r",encoding='utf-8') as f:
    all_codes = dict(line.strip().split(":") for line in f)

# 读取需要查询的代码的txt文件
with open("query_codes.txt", "r",encoding='utf-8') as f:
    query_codes = [line.strip() for line in f]

# 遍历需要查询的代码，输出对应的地址
with open("result.txt", "w",encoding='utf-8') as f:
    for code in query_codes:
        province_code = code[:2] + "0000"
        province_name = all_codes[province_code]
        if(code in all_codes):
            address = all_codes[code]
            full_address = province_name + address
            f.write(full_address + "\n")
        else:
            f.write(province_name + "\n")