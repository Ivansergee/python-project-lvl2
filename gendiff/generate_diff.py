def generate_diff(data1, data2):

    data = {*data1, *data2}
    diff_log = []

    for key in data:
        if key in data1:
            if key in data2:
                if data1[key] == data2[key]:
                    res = [(' ', key, data1[key])]
                else:
                    res = [('-', key, data1[key]), ('+', key, data2[key])]
            else:
                res = [('+', key, data1[key])]
        else:
            res = [('+', key, data2[key])]
        diff_log.extend(res)

    diff_log.sort(key=lambda i: i[1])
    
