# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:35:40 2022

@author: Yuwen.Fang
"""

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import numpy as np
import streamlit as st  # pip install streamlit

timeSelect = '110/12/'
file_name = '11012報表之圖表區-增訂需管控項目.xlsx'
sheet_name = '總表new'

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="迪化廠資料初步展示", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ---- #
@st.cache
# 進流水量&放流水量
def flow_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,B,CJ")
    df.columns = ['日期','進流水量','放流水量']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

def BOD_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,G,W,AE,AL,BS,CO,DR,DY,GI")
    df.columns = ['日期','進流渠道','初沉池進','初沉池出','迴流液匯合池流量計',
                  '二沈池出水','放流水','回收水','帶濾式污泥濃縮機濾液','緊急排水']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.replace(['停機'], float(0.0))
    df = df.fillna(0.0)
    return df

def COD_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,H,X,AF,AM,BT,CP,DS,DZ,GJ")
    df.columns = ['日期','進流渠道','初沉池進','初沉池出','迴流液匯合池流量計',
                  '二沈池出水','放流水','回收水','帶濾式污泥濃縮機濾液','緊急排水']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df['回收水'] = df['回收水'].replace(['停機'], float(0.0))
    df['帶濾式污泥濃縮機濾液'] = df['帶濾式污泥濃縮機濾液'].replace(['停機'], float(0.0))
    df = df.fillna(0.0)
    return df

def ss_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,I,Y,AG,AK,AU,AV,AW,AX,BF,BG,BH,BI,BU,CF,CG,CQ,DT,EJ,EK,EQ,ES,FH,FI,FQ,FS,GA,GH")
    df.columns = ['日期','進流渠道','初沉池進','初沉池出','迴流液匯合池流量計',
                  '初沉污泥-1','初沉污泥-1(揮發性)','初沉污泥-2','初沉污泥-2(揮發性)',
                  '深層階段曝氣槽-好氧','深層階段曝氣槽-缺氧','深層階段曝氣槽-好氧(揮發性)',
                  '深層階段曝氣槽-缺氧(揮發性)','二沈池出水','迴流污泥','迴流污泥(揮發性)',
                  '放流水','回收水','帶濾式濃縮機進流污泥','帶濾式濃縮機進流污泥(揮發性)',
                  '厭氧消化槽進流污泥','厭氧消化槽進流污泥(揮發性)','厭氧消化槽出流污泥',
                  '厭氧消化槽出流污泥(揮發性)','帶濾式脫水機進流污泥','帶濾式脫水機進流污泥(揮發性)',
                  '帶濾式脫水機濾液','緊急排水']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.replace(['停機'], float(0.0))
    df = df.fillna(0.0)
    return df

def removal_rate_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,AO,AP,AQ,DC,DB,DA,DD,DU,DV,DW")
    df.columns = ['日期','初沉池-BOD','初沉池-COD','初沉池-ss',
                  '全廠-BOD','全廠-COD','全廠-ss','全廠-氨氮',
                  '回收水-BOD','回收水-COD','回收水-ss']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    num = df._get_numeric_data()
    num[num < 0] = np.nan
    df = df.replace(['-'], np.nan)
    df = df.replace(['--'], np.nan)
    df['初沉池-BOD'] = df['初沉池-BOD']*100
    df['初沉池-COD'] = df['初沉池-COD']*100
    df['初沉池-ss'] = df['初沉池-ss']*100
    df['全廠-BOD'] = df['全廠-BOD']*100
    df['全廠-COD'] = df['全廠-COD']*100
    df['全廠-ss'] = df['全廠-ss']*100
    df['全廠-氨氮'] = df['全廠-氨氮']*100
    
    return df

#刮泥機台數
def machine_number_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,AA,BZ,EM,GG")
    df.columns = ['日期','初沉刮泥機台數','二沉池刮泥機台數','濃縮機運轉中台數','脫水機運轉中台數']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#迴流液匯合池流量計
def flowmeter_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,AJ")
    df.columns = ['日期','日流量(CMD)']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#深層階段曝氣槽 (不確定是否要把SVI,污泥齡,微食比全部放在一起看)
def aeration_tank_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,BJ,BK,BL")
    df.columns = ['日期','SVI(ml/g)','污泥齡(day)','微食比']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#乾燥系統
def dry_sys_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,GO,GR,GS,GT,GW,GX,GY,GZ,HA")
    df.columns = ['日期','乾燥後污泥餅含水率(%)','乾燥污泥產量(kg)','消化瓦斯(FE-0907A)用量(m3)','天然瓦斯用量(m3)',
                  '1號乾燥機運轉溫度','2號乾燥機運轉溫度','用電錶燈用量(kwH)','回收水用量(m3)','自來水用量(m3)']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    df = df.replace(['-'], float(0.0))
    df = df.replace(['停機'], float(0.0))
    df = df.replace(['未出料'], float(0.0))
    return df

#放流抽水機
#電流值
def outfall_pump_elect_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,HD,HE,HF,HG")
    df.columns = ['日期','P-0606A','P-0606B','P-0606C','P-0606D']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df
#軸承溫度
def outfall_pump_temp_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,HH,HI,HJ,HK")
    df.columns = ['日期','P-0606A','P-0606B','P-0606C','P-0606D']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df
#全廠本月用電量
def electricity_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,HM")
    df.columns = ['日期','用電量']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#厭氧消化槽進流污泥
#日產氣量
def anaerobic_gas_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,EZ,FA,FB")
    df.columns = ['日期','A槽','C槽', '消化鍋爐瓦斯']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#溫度
def anaerobic_temp_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,FC,FD")
    df.columns = ['日期','A槽','C槽']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#次氯酸鈉NaOCL
def NaOCL_L_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,JK,JL,JN,JP,JR,JT,JV")
    df.columns = ['日期','除臭大樓補充2A','固大除臭補充2B','消毒總用量','除臭總補充量','次氯酸鈉NaOCL總用量',
                  '消毒契約用量上限4ppm','除臭契約用量上限2.39ppm']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

def NaOCL_kg_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,JM,JO,JQ,JS,JU,JW,JX,JY,JZ")
    df.columns = ['日期','乾燥水肥消化除臭量','消毒總用量','除臭總補充量','次氯酸鈉NaOCL總用量',
                  '消毒契約用量上限4ppm','除臭契約用量上限2.39ppm','總使用量','消毒上限值檢查',
                  '(車1)化學加藥室進藥量']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#氫氧化鈉 NaOH
def NaOH_L_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,KF,KG,KJ")
    df.columns = ['日期','往除臭大樓3A','往固大除臭3B','總用量']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

def NaOH_kg_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,KI,KK")
    df.columns = ['日期', '化學加藥室NaOH槽進藥量','補充量(比重使用1.22)']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#硫酸 H2SO4
def H2SO4_L_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,KL,KM,KP")
    df.columns = ['日期','往除臭大樓4A','往固大除臭4B','總用量']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

def H2SO4_kg_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,KO,KQ")
    df.columns = ['日期', '化學加藥室H2SO4進藥量','總用量(比重使用1.4)']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#化學加藥室 氫氧化鈉&硫酸 槽液位(meter)
def NaOH_H2SO4_height_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,KH,KN")
    df.columns = ['日期','氫氧化鈉NaOH','硫酸H2SO4']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#進藥量(鹽酸&亞氯酸鈉)進藥量
def NaOH_H2SO4_input_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,KR,KS")
    df.columns = ['日期','鹽酸HCl','亞氯酸鈉NaClO2']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#高分子Polymer
def polymer_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,KU,KV,KW")
    df.columns = ['日期','使用量','脫水機','濃縮機']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    df = df.replace('-', float(0.0))
    return df

#本月自來水使用量
def water_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,KX")
    df.columns = ['日期','使用量']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#自動水質監測(下載)
def auto_download_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,MB,MC,MD")
    df.columns = ['日期','COD','ss','氨氮']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

#水肥站
def trash_kg_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,ME,MF,MG")
    df.columns = ['日期','水肥+生廚餘','生廚餘','水肥']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

def trash_car_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,MH,MI,MJ")
    df.columns = ['日期','水肥+生廚餘','生廚餘','水肥']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

def digester_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,OC")
    df.columns = ['日期','A+C槽']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    df = df.fillna(0.0)
    return df

def bill_get_data():
    df = pd.read_excel(file_name,
                       sheet_name,
                       skiprows=2,
                       usecols="A,NY,NZ,OA,OB")
    df.columns = ['日期','自來水總金額(元)','自來水度數(度)','台電總金額(元)','台電度數(度)']

    # 篩選(條件*1)
    df = df[df['日期'].str.startswith(timeSelect, na=False)]
    return df[0:1]
   

# ------ 各參數 ------------------------------------------------------
df_flow = flow_get_data()
df_BOD = BOD_get_data()
df_COD = COD_get_data()
df_ss = ss_get_data()
df_removal_rate = removal_rate_get_data()
df_machine_number = machine_number_get_data()
df_flowmeter = flowmeter_get_data()
df_aeration_tank = aeration_tank_get_data()
df_dry_sys = dry_sys_get_data()
df_outfall_pump_elect = outfall_pump_elect_get_data()
df_outfall_pump_temp = outfall_pump_temp_get_data()
df_electricity = electricity_get_data()
df_anaerobic_gas = anaerobic_gas_get_data()
df_anaerobic_temp = anaerobic_temp_get_data()
df_NaOCL_L = NaOCL_L_get_data()
df_NaOCL_kg = NaOCL_kg_get_data()
df_NaOH_L = NaOH_L_get_data()
df_NaOH_kg = NaOH_kg_get_data()
df_H2SO4_L = H2SO4_L_get_data()
df_H2SO4_kg = H2SO4_kg_get_data()
df_NaOH_H2SO4_height = NaOH_H2SO4_height_get_data()
df_NaOH_H2SO4_input = NaOH_H2SO4_input_get_data()
df_polymer = polymer_get_data()
df_water = water_get_data()
df_auto_download = auto_download_get_data()
df_trash_kg = trash_kg_get_data()
df_trash_car = trash_car_get_data()
df_digester = digester_get_data()
df_bill = bill_get_data()


# ---- MAINPAGE ---- #
st.title(":bar_chart: 迪化廠資料初步展示")
st.markdown("##")

# bill --------------------------------
water_money = int(df_bill["自來水總金額(元)"])
water_degree = int(df_bill["自來水度數(度)"])
electicity_money = int(df_bill["台電總金額(元)"])
electicity_degree = int(df_bill["台電度數(度)"])

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("自來水:")
    st.subheader(f"金額 NTD $ {water_money:,}")
    st.subheader(f"度數 {water_degree:,}")
with right_column:
    st.subheader("台電:")
    st.subheader(f"金額 NTD $ {electicity_money:,}")
    st.subheader(f"度數 {electicity_degree:,}")

# BOD [LINE CHART] --------------------
fig_flow = px.line(df_flow, x='日期', y=['進流水量','放流水量'], orientation="h",
                  title="<b>進流水量&放流水量(CMD)</b>",template="plotly_white", width=1350)
fig_flow.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_flow)

# BOD [LINE CHART] --------------------
fig_BOD = px.line(df_BOD, x='日期', y=['進流渠道','初沉池進','初沉池出','迴流液匯合池流量計',\
                                      '二沈池出水','放流水','回收水','帶濾式污泥濃縮機濾液','緊急排水'], orientation="h",
                  title="<b>生化需氧量BOD(mg/L)</b>",template="plotly_white")
fig_BOD.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# COD [LINE CHART] ---------------------
fig_COD = px.line(df_COD, x='日期', y=['進流渠道','初沉池進','初沉池出','迴流液匯合池流量計','二沈池出水','放流水','回收水','帶濾式污泥濃縮機濾液','緊急排水'], orientation="h",
                  title="<b>化學需氧量COD(mg/L)</b>",template="plotly_white")
fig_BOD.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_BOD, use_container_width=True)
right_column.plotly_chart(fig_COD, use_container_width=True)

# ss [LINE CHART] ---------------------
fig_ss = px.line(df_ss, x='日期', y=['進流渠道','初沉池進','初沉池出','迴流液匯合池流量計',
                                     '初沉污泥-1','初沉污泥-1(揮發性)','初沉污泥-2','初沉污泥-2(揮發性)',
                                     '深層階段曝氣槽-好氧','深層階段曝氣槽-缺氧','深層階段曝氣槽-好氧(揮發性)',
                                     '深層階段曝氣槽-缺氧(揮發性)','二沈池出水','迴流污泥','迴流污泥(揮發性)',
                                     '放流水','回收水','帶濾式濃縮機進流污泥','帶濾式濃縮機進流污泥(揮發性)',
                                     '厭氧消化槽進流污泥','厭氧消化槽進流污泥(揮發性)','厭氧消化槽出流污泥',
                                     '厭氧消化槽出流污泥(揮發性)','帶濾式脫水機進流污泥','帶濾式脫水機進流污泥(揮發性)',
                                     '帶濾式脫水機濾液','緊急排水'],
                   title="<b>懸浮固體ss(mg/L)</b>",template="plotly_white")
fig_ss.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# removal rate [SCATTER CHART] ---------------------
fig_removal_rate = px.scatter(df_removal_rate, x='日期', y=['初沉池-BOD','初沉池-COD','初沉池-ss',
                                                 '全廠-BOD','全廠-COD','全廠-ss','全廠-氨氮',
                                                 '回收水-BOD','回收水-COD','回收水-ss'],
                   title="<b>去除率(%)</b>",template="plotly_white")
fig_removal_rate.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_ss, use_container_width=True)
right_column.plotly_chart(fig_removal_rate, use_container_width=True)

# df_flowmeter [line CHART] ---------------------
fig_flowmeter = px.line(df_flowmeter, x='日期', y='日流量(CMD)',
                                title="<b>迴流液匯合池流量計</b>",template="plotly_white")
fig_flowmeter.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# df_aeration_tank [scatter CHART] ---------------------
fig_aeration_tank = px.scatter(df_aeration_tank, x='日期', y=['SVI(ml/g)','污泥齡(day)','微食比'],
                                title="<b>深層階段曝氣槽</b>",template="plotly_white")
fig_aeration_tank.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_flowmeter, use_container_width=True)
right_column.plotly_chart(fig_aeration_tank, use_container_width=True)

# df_machine_number [BAR CHART] ---------------------
fig_machine_number_1 = px.bar(df_machine_number, x='日期', y=['初沉刮泥機台數','二沉池刮泥機台數'],
                                title="<b>刮泥機台數</b>",template="plotly_white")
fig_machine_number_1.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
fig_machine_number_2 = px.bar(df_machine_number, x='日期', y=['濃縮機運轉中台數','脫水機運轉中台數'],
                              title="<b>運轉中台數</b>", template="plotly_white")
fig_machine_number_2.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_machine_number_1, use_container_width=True)
right_column.plotly_chart(fig_machine_number_2, use_container_width=True)


# df_dry_sys [scatter CHART] ---------------------
#'乾燥後污泥餅含水率(%)','乾燥污泥產量(kg)','消化瓦斯(FE-0907A)用量(m3)','天然瓦斯用量(m3)',
#'1號乾燥機運轉溫度','2號乾燥機運轉溫度','用電錶燈用量(kwH)','回收水用量(m3)','自來水用量(m3)'
              
fig_dry_sys_1 = px.line(df_dry_sys, x='日期', y='乾燥後污泥餅含水率(%)',
                         title="<b>乾燥系統</b>",template="plotly_white")
fig_dry_sys_1.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_dry_sys_2 = px.line(df_dry_sys, x='日期', y='乾燥污泥產量(kg)',
                        template="plotly_white")
fig_dry_sys_2.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_dry_sys_1, use_container_width=True)
right_column.plotly_chart(fig_dry_sys_2, use_container_width=True)

fig_dry_sys_3 = px.line(df_dry_sys, x='日期', y=['消化瓦斯(FE-0907A)用量(m3)','天然瓦斯用量(m3)'],
                        template="plotly_white")
fig_dry_sys_3.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_dry_sys_4 = px.line(df_dry_sys, x='日期', y=['回收水用量(m3)','自來水用量(m3)'],
                        template="plotly_white")
fig_dry_sys_4.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_dry_sys_3, use_container_width=True)
right_column.plotly_chart(fig_dry_sys_4, use_container_width=True)

fig_dry_sys_5 = px.line(df_dry_sys, x='日期', y=['1號乾燥機運轉溫度','2號乾燥機運轉溫度'],
                        template="plotly_white")
fig_dry_sys_5.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_dry_sys_6 = px.line(df_dry_sys, x='日期', y='用電錶燈用量(kwH)',
                        template="plotly_white")
fig_dry_sys_6.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_dry_sys_5, use_container_width=True)
right_column.plotly_chart(fig_dry_sys_6, use_container_width=True)

# df_outfall_pump [LINE CHART] ---------------------
fig_outfall_pump_elect = px.line(df_outfall_pump_elect, x='日期', y=['P-0606A','P-0606B','P-0606C','P-0606D'],
                                 title="<b>放流抽水機-電流值(A)</b>", template="plotly_white")
fig_outfall_pump_elect.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_outfall_pump_temp = px.line(df_outfall_pump_temp, x='日期', y=['P-0606A','P-0606B','P-0606C','P-0606D'],
                        title="<b>放流抽水機-軸承溫度(攝氏度C)</b>", template="plotly_white")
fig_dry_sys_6.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_outfall_pump_elect, use_container_width=True)
right_column.plotly_chart(fig_outfall_pump_temp, use_container_width=True)


#厭氧消化槽進流污泥
#日產氣量
# df_anaerobic [LINE CHART] ---------------------
fig_anaerobic_gas = px.line(df_anaerobic_gas, x='日期', y=['A槽', 'C槽', '消化鍋爐瓦斯'],
                          title="<b>厭氧消化槽進流污泥-日產氣量(m3)</b>",template="plotly_white")
fig_anaerobic_gas.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_anaerobic_temp = px.line(df_anaerobic_temp, x='日期', y=['A槽', 'C槽'],
                          title="<b>厭氧消化槽進流污泥-溫度(攝氏度C)</b>",template="plotly_white")
fig_anaerobic_temp.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_anaerobic_gas, use_container_width=True)
right_column.plotly_chart(fig_anaerobic_temp, use_container_width=True)

# df_electricity [LINE CHART] --------------------- (不知道單位)
fig_electricity = px.line(df_electricity, x='日期', y=['用電量'],
                                title="<b>全廠本月用電量</b>",template="plotly_white", width=1300)
fig_electricity.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_electricity)

#次氯酸鈉NaOCL
#df_NaOCL [LINE CHART] ---------------------
fig_NaOCL_L = px.line(df_NaOCL_L, x='日期', y=['除臭大樓補充2A','固大除臭補充2B','消毒總用量',
                                               '除臭總補充量','次氯酸鈉NaOCL總用量','消毒契約用量上限4ppm',
                                               '除臭契約用量上限2.39ppm'],
                      title="<b>次氯酸鈉NaOCL(L)</b>",template="plotly_white")
fig_NaOCL_L.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_NaOCL_kg = px.line(df_NaOCL_kg, x='日期', y=['乾燥水肥消化除臭量','消毒總用量','除臭總補充量',
                                                 '次氯酸鈉NaOCL總用量','消毒契約用量上限4ppm','除臭契約用量上限2.39ppm',
                                                 '總使用量','消毒上限值檢查','(車1)化學加藥室進藥量'],
                        title="<b>次氯酸鈉NaOCL(kg)</b>",template="plotly_white")
fig_NaOCL_kg.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_NaOCL_L, use_container_width=True)
right_column.plotly_chart(fig_NaOCL_kg, use_container_width=True)

#氫氧化鈉 NaOH
# df_NaOH [LINE CHART] ---------------------
fig_NaOH_L = px.line(df_NaOH_L, x='日期', y=['往除臭大樓3A','往固大除臭3B','總用量'],
                          title="<b>氫氧化鈉NaOH(L)</b>",template="plotly_white")
fig_NaOH_L.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_NaOH_kg = px.line(df_NaOH_kg, x='日期', y=['化學加藥室NaOH槽進藥量','補充量(比重使用1.22)'],
                        title="<b>氫氧化鈉NaOH(kg)</b>",template="plotly_white")
fig_NaOCL_kg.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_NaOH_L, use_container_width=True)
right_column.plotly_chart(fig_NaOH_kg, use_container_width=True)

#硫酸 H2SO4
# df_H2SO4 [LINE CHART] ---------------------
fig_H2SO4_L = px.line(df_H2SO4_L, x='日期', y=['往除臭大樓4A','往固大除臭4B','總用量'],
                          title="<b>硫酸H2SO4(L)</b>",template="plotly_white")
fig_H2SO4_L.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_H2SO4_kg = px.line(df_H2SO4_kg, x='日期', y=['化學加藥室H2SO4進藥量','總用量(比重使用1.4)'],
                        title="<b>硫酸H2SO4(kg)</b>",template="plotly_white")
fig_H2SO4_kg.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_H2SO4_L, use_container_width=True)
right_column.plotly_chart(fig_H2SO4_kg, use_container_width=True)

#化學加藥室 氫氧化鈉&硫酸 槽液位
# df_NaOH_H2SO4_height [LINE CHART] ---------------------
fig_NaOH_H2SO4_height = px.line(df_NaOH_H2SO4_height, x='日期', y=['氫氧化鈉NaOH','硫酸H2SO4'],
                          title="<b>化學加藥室槽液位(Meter)</b>",template="plotly_white")
fig_NaOH_H2SO4_height.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

#進藥量(鹽酸&亞氯酸鈉)進藥量
#df_NaOH_H2SO4_input
fig_NaOH_H2SO4_input = px.line(df_NaOH_H2SO4_input, x='日期', y=['鹽酸HCl','亞氯酸鈉NaClO2'],
                          title="<b>進藥量(kg)</b>",template="plotly_white")
fig_NaOH_H2SO4_input.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_NaOH_H2SO4_height, use_container_width=True)
right_column.plotly_chart(fig_NaOH_H2SO4_input, use_container_width=True)

#高分子Polymer
# df_polymer [LINE CHART] ---------------------
fig_polymer_1 = px.line(df_polymer, x='日期', y=['使用量'],
                      title="<b>高分子Polymer使用量(kg)</b>",template="plotly_white")
fig_polymer_1.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

fig_polymer_2 = px.line(df_polymer, x='日期', y=['脫水機','濃縮機'],
                      title="<b>高分子Polymer(CMD)</b>",template="plotly_white")
fig_polymer_2.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_polymer_1, use_container_width=True)
right_column.plotly_chart(fig_polymer_2, use_container_width=True)

#本月自來水使用量 (不知道單位)
fig_water = px.line(df_water, x='日期', y=['使用量'],
                      title="<b>自來水使用量</b>",template="plotly_white")
fig_water.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
 
#自動水質監測(下載)
fig_auto_download = px.line(df_auto_download, x='日期', y=['COD','ss','氨氮'],
                      title="<b>自動水質監測(mg/L)</b>",template="plotly_white")
fig_auto_download.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_water, use_container_width=True)
right_column.plotly_chart(fig_auto_download, use_container_width=True) 

#水肥站
#投肥量
fig_trash_kg = px.line(df_trash_kg, x='日期', y=['水肥+生廚餘','生廚餘','水肥'],
                      title="<b>投肥量(kg)</b>",template="plotly_white")
fig_trash_kg.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
 
#投肥車次
fig_trash_car = px.line(df_trash_car, x='日期', y=['水肥+生廚餘','生廚餘','水肥'],
                      title="<b>投肥車次(車次)</b>",template="plotly_white")
fig_trash_car.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_trash_kg, use_container_width=True)
right_column.plotly_chart(fig_trash_car, use_container_width=True) 



#df_digester [LINE CHART] ---------------------
fig_digester = px.line(df_digester, x='日期', y=['A+C槽'],
                      title="<b>消化瓦斯產氣量(m3)</b>",template="plotly_white")
fig_digester.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_digester)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)