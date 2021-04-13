from flask import Flask,render_template,request
import user_function
import json

app = Flask(__name__)

@app.route('/')
def first():
    return render_template("ajax_test.html")

@app.route("/getuniversityname",methods=['POST'])
def getuniversityname():
    query_code = "select YuanXiaoMinChen from dm_yuanxiao_zhuanye where ZhiYuanPiCi = '本科一批' and ZhiYuanLeiBie = '普通理科' and yuanxiaoDaiMa = '" + request.values.get("yxdm") + "' limit 1;"
    db_conn = user_function.db_conn_MySql()
    yxmc = user_function.query_db_MySql(db_conn,query_code)
    user_function.db_close_MySql(db_conn)
    if len(yxmc) == 0 :
        name = '计划院校代号：' + request.values.get("yxdm") + '不存在'
    else:
        name = yxmc[0][0]
    return name
    
@app.route("/getmajorname",methods=['POST'])
def getmajorname():
    query_code = "select ZhuanYeMinChen from dm_yuanxiao_zhuanye where ZhiYuanPiCi = '本科一批' and ZhiYuanLeiBie = '普通理科' and yuanxiaoDaiMa = '" + request.values.get("yxdm") + "' and ZhuanYeDaiHao = '" + request.values.get("zydm") + "' limit 1 ;"
    db_conn = user_function.db_conn_MySql()
    zymc = user_function.query_db_MySql(db_conn,query_code)
    user_function.db_close_MySql(db_conn)
    if len(zymc) == 0 :
        name = '计划院校专业代号：' + request.values.get("zydm") + '不存在'
    else:
        name = zymc[0][0]
    return name

if __name__ =='__main__':
    # 127.0.0.1为测试用，发布前应改为0.0.0.0
    app.run()
