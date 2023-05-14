from pyecharts.charts import Bar, Line
from pyecharts import options as opts

class DrawChart:
  def bar(self, title, x_label, y_label1, y_label2, x, y, y2):
    chart = Bar()
    chart.add_xaxis(x)
    chart.add_yaxis(y_label1, y)
    chart.add_yaxis(y_label2, y2)
    yaxis_opts=[
    opts.AxisOpts(name=y_label1),
    opts.AxisOpts(name=y_label2)]
    chart.set_global_opts(
        title_opts=opts.TitleOpts(title=title),
        xaxis_opts=opts.AxisOpts(name=x_label),
    )
    chart_html = chart.render_embed()
    return chart_html

  # def bar_with_line(self, title, x_label, y_label1, y_label2, y_label3, x, y, y2, y3):
  #   bar_chart = Bar()
  #   line_chart = Line()

  #   bar_chart.add_xaxis(x)
  #   bar_chart.add_yaxis(y_label1, y)
  #   bar_chart.add_yaxis(y_label2, y2)
  #   yaxis_opts=[
  #   opts.AxisOpts(name=y_label1),
  #   opts.AxisOpts(name=y_label2)]
  #   bar_chart.set_global_opts(
  #       title_opts=opts.TitleOpts(title=title),
  #       xaxis_opts=opts.AxisOpts(name=x_label),
  #   )
  #   line_chart.add_xaxis(x)
  #   line_chart.add_yaxis(y_label3, y3)
  #   line_chart.set_global_opts(
  #       title_opts=opts.TitleOpts(title=title),
  #       xaxis_opts=opts.AxisOpts(name=x_label),
  #       yaxis_opts=opts.AxisOpts(name=y_label3),
  #   )

  #   chart = line_chart.overlap(bar_chart)
  #   chart_html = chart.render_embed()
  #   return chart_html


  def line(self, title, x_label, y_label, x, y):
    chart = Line()
    chart.add_xaxis(x)
    chart.add_yaxis(y_label, y)
    
    chart.set_global_opts(
      title_opts=opts.TitleOpts(title=title),
      xaxis_opts=opts.AxisOpts(name=x_label),
      yaxis_opts=opts.AxisOpts(name=y_label),
      
    )
    chart_html = chart.render_embed()
    return chart_html
  
  def lines7(self, title, x_label, y_label, x, y):
    chart = Line()
    chart.add_xaxis(x)

    for shop_name, sales in y.items():
        chart.add_yaxis(shop_name, sales)

    chart.set_global_opts(
        title_opts=opts.TitleOpts(title=title),
        xaxis_opts=opts.AxisOpts(name=x_label),
        yaxis_opts=opts.AxisOpts(name=y_label),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )

    chart_html = chart.render_embed()
    return chart_html

