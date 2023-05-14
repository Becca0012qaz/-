from flask import Flask, render_template, request
from functions.connect_to_db import SQLcommand
from functions.draw_chart import DrawChart
from datetime import datetime


app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html', message='Hello Flask!')
  
  if request.form.get('options'):
    value = request.form.get('options')
    dataset = SQLcommand().get(f'SELECT time, likes, reactions, shares, comments FROM facebook_posts WHERE MONTH(time) = {value} AND YEAR(time) = 2023 ORDER BY time')
    data_dict = [{'time': data[0], 'likes': data[1], 'reactions': data[2], 'shares': data[3], 'comments': data[4]} for data in dataset]
    return render_template('index.html', message=f'2023年{value}月', data=data_dict, selected_value=value)

  # if request.form.get('button') == 'line':
  #   dataset = SQLcommand().get('SELECT DATE_FORMAT(time, "%Y") AS year, COUNT(*) FROM facebook_posts GROUP BY year ORDER BY year')
  #   x, y = [element[0] for element in dataset], [element[1] for element in dataset]
  #   chart_html = DrawChart().line('Posts of Year', 'Year', 'Posts', x, y)
  #   return render_template('index.html', chart_html=chart_html)

  if request.form.get('button') == 'line':
      dataset = SQLcommand().get('SELECT shop_name AS name, DATE_FORMAT(date, "%Y-%M") AS sales_month, SUM(monthly_sales * price) AS total_sales FROM products_info WHERE date>=start AND date<=end GROUP BY name, sales_month')
      x = [element[1] for element in dataset]  # 年月資料
      y_data = {}  # 每個商家的銷售額資料

      for element in dataset:
          shop_name = element[0]
          sales = element[2]
          if shop_name not in y_data:
              y_data[shop_name] = []
          y_data[shop_name].append(sales)

      
      chart_html = DrawChart().lines7('月銷售額','年月份','銷售總額', x, y_data)
      return render_template('index.html', chart_html=chart_html)

  
  if request.form.get('button') == 'bar':
    dataset = SQLcommand().get('SELECT shop_name AS name, SUM(fans_count) AS fans, SUM(rating_counts) AS rating FROM offical_data GROUP BY name ORDER BY fans DESC')
    x, y, y2 = [element[0] for element in dataset], [element[1] for element in dataset], [element[2] for element in dataset]
    print(x)
    chart_html = DrawChart().bar('競品總覽', '商店名稱', '粉絲數', '評價數', x, y, y2)
    return render_template('index.html', chart_html=chart_html)
  # if request.form.get('button') == 'bar':
  #     dataset = SQLcommand().get('SELECT shop_name AS name, SUM(fans_count) AS fans, SUM(rating_counts) AS rating, SUM(products_count) AS products FROM offical_data GROUP BY name')
  #     x, y, y2, y3 = [element[0] for element in dataset], [element[1] for element in dataset], [element[2] for element in dataset], [element[3] for element in dataset]
  #     chart_html = DrawChart().bar_with_line('競品總覽', '商店名稱','粉絲數', '評價數', '商品數', x, y, y2, y3)
  #     return render_template('index.html', chart_html=chart_html)


  
  if request.form.get('button') == 'date':
    start = request.form.get('start')
    end = request.form.get('end')
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')
    if start_date < end_date:
      return render_template('test.html', start=start, end=end)
    else:
      return render_template('index.html', message='結束日期不能早於開始日期！')
  
  if request.form.get('button') == 'login':
    account = request.form.get('account')
    password = request.form.get('password')
    return render_template('test.html', start=account, end=password)

  value = request.form.get('button')
  dataset = SQLcommand().get(f'SELECT time, likes, reactions, shares, comments FROM facebook_posts ORDER BY time DESC LIMIT {value}')
  data_dict = [{'time': data[0], 'likes': data[1], 'reactions': data[2], 'shares': data[3], 'comments': data[4]} for data in dataset]
  return render_template('index.html', message=f'資料庫前{value}筆資料', data=data_dict)

@app.route('/1')
def template1():
  return render_template('template1.html')

@app.route('/2')
def template2():
  return render_template('template2.html')

@app.route('/3')
def template3():
  return render_template('template3.html')

@app.route('/4',  methods=['GET', 'POST'])
def template4():
  return render_template('template4.html', message=f'資料庫前{value}筆資料', data=data_dict)

  


@app.route('/5')
def template5():
  return render_template('template5.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')
