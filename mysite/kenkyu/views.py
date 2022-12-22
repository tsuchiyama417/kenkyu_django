from django.shortcuts import render

# import : model, form
from kenkyu.models import Organism
from mysite.forms import AnimalChoiceForm

import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot
from plotly.tools import FigureFactory as ff


def make_graph(df):
    
    # Plotlyで三次元グラフ表示を行う
    # アミノ酸ベクトルについてはdetail.htmlを参照
    # 引数：生物種の名前、生物種配列
    # 返り値：PlotlyのFigureオブジェクト
    
    # アミノ酸ベクトルの定義
    amino_dic = {"A":(2.060, -0.669, 1.083), "C":(0.000, -3.718, 1.859), "D":(1.201, -0.390, 1.263),
                "E":(-0.689, -0.948, 1.172), "F":(-1.662, -2.286, 1.413), "G":(0.000, 2.300, 1.150),
                "H":(0.000, -1.643, 1.643), "I":(-1.444, 1.987, 1.228), "K":(0.727, 1.000, 1.236),
                "L":(-1.930, -0.627, 1.015), "M":(1.902, -2.616, 1.617), "N":(0.818, -1.125, 1.391),
                "P":(-1.259, -0.409, 1.324), "Q":(1.336, 0.434, 1.405), "R":(0.000, 1.257, 1.257),
                "S":(1.385, 1.906, 1.178), "T":(-0.747, 1.028, 1.271), "V":(-2.212, 0.719, 1.163),
                "W":(3.726, 1.211, 1.959), "Y":(-1.460, 0.474, 1.535)}
    fig = go.Figure()
    # 座標を生成してプロット
    for data in df.itertuples():
        animal_name = data[2]
        org_arr = data[3]
        arr_x = [0]; arr_y = [0]; arr_z = [0]
        for i in range(len(org_arr)):
            arr_x.append(arr_x[i] + amino_dic[org_arr[i]][0])
            arr_y.append(arr_y[i] + amino_dic[org_arr[i]][1])
            arr_z.append(arr_z[i] + amino_dic[org_arr[i]][2])
        fig.add_trace(go.Scatter3d(x=arr_x, y=arr_y, z=arr_z, mode="lines", line=dict(width=7),name=animal_name))
    fig.update_layout(title = "animal_graph_3D", width=1000, height=1000, plot_bgcolor="grey", paper_bgcolor="grey")
    
    return fig


# Create your views here.
def base(request):
    
    # メインページ
    # 生物種の三次元グラフ表示を行う
    # 生物種配列はDBで管理している
    # チェックした選択肢（生物種）をPlotlyで表示する

    context = {}
    
    if request.method == "GET":
        # データの取得
        df = pd.DataFrame(list(Organism.objects.all().values()), index=["0", "1", "2", "3", "4", "5", "6", "7", "8"])
        # プロット
        res = make_graph(df)
        plot_fig = plot(res, output_type="div", include_plotlyjs=False)
        context["chart"] = plot_fig

    if request.method == "POST":
        # チェックした生物種番号を受け取る
        form = AnimalChoiceForm(request.POST)
        
        # 選択肢の抽出
        if form.is_valid():
            select = form.cleaned_data.get("select")
            # 適用ボタンの動作
            if "btn_apply" in request.POST:
                # データの取得
                df = pd.DataFrame(list(Organism.objects.all().values()), index=["0", "1", "2", "3", "4", "5", "6", "7", "8"])
                df = df.loc[form.cleaned_data["select"]]
                # プロット
                res = make_graph(df)
                plot_fig = plot(res, output_type="div", include_plotlyjs=False)
                context["chart"] = plot_fig

    # 選択肢の表示
    choice = AnimalChoiceForm()
    context["form"] = choice
    
    return render(request, "mysite/base.html", context)


def detail(request):
    return render(request, "mysite/detail.html")


