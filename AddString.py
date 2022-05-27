path = 'C:\\Users\\DELL\\Desktop\\insertSQL.txt'
result = 'C:\\Users\\DELL\\Desktop\\result.txt'
with open(path) as f:
    for line in f:
        #print(line[-39:-1])
        text = 'INSERT INTO orders(order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id,staff_id) VALUES('
        text += line[124:133]
        text += 'to_date' + '(' + line[-39:-34] + '/' + line[-34:-32] + '/' + line[-32:-29] + ',' + "'YYYY/MM/DD'" + ')' + line[-29]
        text += 'to_date' + '(' + line[-28:-23] + '/' + line[-23:-21] + '/' + line[-21:-18] + ',' + "'YYYY/MM/DD'" + ')' + line [-18]
        text += 'to_date' + '(' + line[-17:-12] + '/' + line[-12:-10] + '/' + line[-10:-7] + ',' + "'YYYY/MM/DD'" + ')' + line [-7]
        text += line[-6:-1]
        # print(text)
        with open(result, 'a') as r:
            r.write(text)
            r.write('\n')
        