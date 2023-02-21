import pymysql.cursors

Connect to the database
connection = pymysql.connect(host='172.25.0.101',
                             user='etl',
                             password='Vega123312##',
                             database='waka',
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        # Read a single record
        sql = """select user_id, group_concat(distinct cast(ccb.category_id as string)) as category
                from waka_pd_fact_reader as wr
                join content_category_brid as ccb
                on wr.content_id = ccb.category_id
                group by user_id order by user_id"""
        cursor.execute(sql)
        result = cursor.fetchmany(20)
        print(result)

