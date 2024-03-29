from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import re
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
from datetime import datetime
#Listas para crear el diccionario de regiones
RegionesDic=['Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Northern Hemisphere', 'Northern Hemisphere', 'Southern Hemisphere', 'Southern Hemisphere']
PaisesDic=['Afghanistan', 'Africa', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Asia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Europe', 'Faeroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North America', 'North Korea', 'North Macedonia', 'Norway', 'Oceania', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South America', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
DiccionarioRegiones={}
#Se crea el diccionario de regiones
for i in range(len(RegionesDic)):
    DiccionarioRegiones[PaisesDic[i]]=RegionesDic[i]
#titulos de la tabla para paises
titulos=['Entity','Year','Annual CO2 emissions (per capita)','Average monthly precipitation','Total GHG emissions excluding LUCF (CAIT)','Region']
titulos2=titulos
#####################################################################################################################################
#Se leen los excel y se toman los datos
emision = pd.read_excel("./datos/emisionCO2.xlsx")
pais1=emision['Entity'].values
years1=emision['Year'].values
emisiones1=emision['Annual CO2 emissions (per capita)'].values

tipoGraph=1
clickGraph=0
lluvia=pd.read_excel("./datos/lluvia.xlsx")
pais2=lluvia['Entity'].values
years2=lluvia['Year'].values
lluvias=lluvia['Average monthly precipitation'].values

paReg="pais"
emision2 = pd.read_excel("./datos/emisionGHC.xlsx")
pais3=emision2['Entity'].values
years3=emision2['Year'].values
emisiones2=emision2['Total GHG emissions excluding LUCF (CAIT)'].values
listTemClimate=[]
climateExcel=pd.read_excel("./datos/climate.xlsx")
regExcel=climateExcel['Entity']
dayExcel=climateExcel['Day']
tempExcel=climateExcel['temperature_anomaly']
listadevaloresPie=[0,0]
###################################################################################################################################


            


diccionario=emision.to_dict('records')

#Funcion que filtra los datos, lee todas las lineas de los excels, y asigna los valores correspondientes de fecha y pais, y crea un diccionario    
def filtrar():
    print("Empenzanod a filtrar datos")
    listaT1=[]
    listaT2=[]
    listaT3=[]
    listaT4=[]
    listaT5=[]
    listaT6=[]
    i=0
    x=0
    y=0
    val=False
    totalporcentaje=len(pais1)
    while i<len(pais1):
        
        if(years1[i]>=1990 and years1[i]<=2014):
            if pais1[i]==pais2[x] and years1[i]==years2[x]:
                
                if pais1[i]==pais3[y] and years1[i]==years3[y]:
                    listaT1.append(pais1[i])
                    listaT2.append(emisiones1[i])
                    listaT3.append(years1[i])
                    listaT4.append(diccionario[i])
                    listaT4[-1]['Average monthly precipitation']=lluvias[x]
                    listaT4[-1]['Total GHG emissions excluding LUCF (CAIT)']=emisiones2[y]
                    listaT4[-1]['Region']=DiccionarioRegiones[pais1[i]]
                    
                    listaT5.append(lluvias[x])
                    listaT6.append(emisiones2[y])
                    x=0
                    y=0
                    i+=1
                else:
                    y+=1
            else:
                x+=1
        else:
            i+=1
        if(x>=len(pais2)):
            val=True
            x=0
        if(y>=len(pais3)):
            val=True
            x=0
            y=0
        if(val):
            i+=1
            val=False
        
        
    return [listaT1,listaT2,listaT3,listaT4,listaT5,listaT6]


listaTemp=filtrar()
pais1=listaTemp[0]
emisiones1=listaTemp[1]
years1=listaTemp[2]

diccionario=listaTemp[3]
lluvias=listaTemp[4]
emisiones2=listaTemp[5]
total=0;
pais11=pais1
emisiones11=emisiones1
years11=years1
lluvias11=lluvias
emisiones22=emisiones2
#########################################################################################################################
#Funcion que lee el diccionario de regiones y asigna cada region a cada valor de la lista de diccionarios de la tabla
listClimate=[]
for i in range(len(regExcel)):
    if(regExcel[i]=='Southern Hemisphere' or regExcel[i]=='Northern Hemisphere'):
        val=True
        for o in listClimate:
            if(type(dayExcel[i])==type(datetime.now())):
                day=dayExcel[i].year
            elif (dayExcel[i].find('-')!=-1):
                day=dayExcel[i].split('-')[0]
            else:
                day=dayExcel[i].split('/')[-1]
            if(regExcel[i]==o['Region'] and day==o['Year']):
                o['Climate']+=tempExcel[i]
                val=False
                break
        if(val):
            if(type(dayExcel[i])==type(datetime.now())):
                day=dayExcel[i].year
            elif (dayExcel[i].find('-')!=-1):
                day=dayExcel[i].split('-')[0]
            else:
                day=dayExcel[i].split('/')[-1]
            listClimate.append({'Region':regExcel[i],'Year':day,'Climate':0})
for i in listClimate:
    i['Climate']=round((i['Climate']/12),2)


#################################################################################################################################
#Funcion que suma los valores de cierta categoria para crear el grafico de pastel correspondiente
def actualizarTotal():
    global listadevaloresPie
    tempTtt=[0,0,0]
    for i in range(len(emisiones1)):
        tempTtt[0]+=emisiones1[i]
        tempTtt[1]+=lluvias[i]
        tempTtt[2]+=emisiones2[i]
    listadevaloresPie[1]=tempTtt
    return tempTtt
            
    
    





#######################################################################    
lltt=[]
for i in pais1:
    if(not(i in lltt)):
        lltt.append(i)
###########################################################################
paiselect=["Afghanistan","Mundo"]
nClicks=0
#############################################################################
#Funcion que suma los valores de cierta categoria pero solo del pais o region seleccionada para realizar el grafico de pastel
def sumarValues(paisName):
    global pais1,emisiones1,listadevaloresPie
    total=0
    listaSum=[]
    if tipoGraph==0:
        listaSum=emisiones1
    elif tipoGraph==1:
        listaSum=lluvias
    else:
        listaSum=emisiones2
    for i in range(len(pais1)):
        if(pais1[i]==paisName):
            total+=listaSum[i]
    listadevaloresPie[0]=total
    return total
##############################################################################
#Funcion para pasar a la misma escala los valores de GHG,CO2,LLuvia para poder ser vizualizada en el mismo grafico de lineas
def yearsValues(paisName):
    global pais1,emisiones1,years1,listTemClimate
    max1=0
    max2=0
    max3=0
    max4=0
    lTemp=[[],[],[],[],[]]
    for i in range(len(pais1)):
        if(pais1[i]==paisName):
            max1+=emisiones1[i]
            max2+=lluvias[i]
            max3+=emisiones2[i]
            if(paReg=='region'):
                max4+=listTemClimate[i]
    for i in range(len(pais1)):
        if(pais1[i]==paisName):
            lTemp[0].append(years1[i])
            lTemp[1].append((emisiones1[i]*100)/max1)
            lTemp[2].append((lluvias[i]*100)/max2)
            lTemp[3].append((emisiones2[i]*100)/max3)
            if(paReg=='region'):
                lTemp[4].append(((listTemClimate[i]*100)/max4)/5+3)
    return lTemp



###############################################################################################################
#Inicia el html
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout =html.Div(html.Div(html.Div([
    
    dcc.Input(id="paisRegion", type="text", value="pais",style={'display':'none'}),
    dcc.Input(id="pruebast", type="text", value="ddd",style={'display':'none'}),
    dcc.Input(id="pruebast4", type="text", value="ddd",style={'display':'none'}),
    dcc.Input(id="pruebast2", type="text", value="ddd",style={'display':'none'}),
    dcc.Input(id="pruebast3", type="text", value="ddd",style={'display':'none'}),
    dcc.Input(id="values", type="text", value="Annual CO2 emissions (per capita)", style={'display':'none'}),
    html.Div([(html.Div([dcc.Graph(id="line-chart")],className="row rowline")),(html.Div([html.Div([html.Div([dcc.Checklist(options=[{'label': 'CO2', 'value': 'CO2'},{'label': 'GHG', 'value': 'GHG'},{'label': 'Lluvia', 'value': 'Lluvia'}],value=['CO2', 'GHG','Lluvia'],id="CheckFiltro",className='checkFiltro',labelStyle={'display': 'inline-block'})],className="row"),html.Div([html.Button('Cambiar Grafico',id="changeGraph",n_clicks=0)],className="row")],className="col col-lg-2"),html.Div([html.Div([dcc.Input(id="tipoGraphTitulo", type="text", value="C02")],className="row"),html.Div([dcc.Graph(id="pie-chart")],className="row")],className="col")],className="row rowPie"))],className="col colMain"),
    html.Div([html.Div([html.Div([dcc.Input(id="search", type="search",className="form-control")],className="col colInputSearch"),html.Div([dcc.Input(id="names", type="text", value="Afghanistan")],className="col"),html.Div([html.Button('Ver por Regiones',id="botonReg", className="regionButton",n_clicks=0)],className="col")],className="row"),dash_table.DataTable(
        
        id='table',
        columns=[{"name": i, "id": i} for i in titulos2],
        style_cell = dict(textAlign="center",fontSize=10),
        data=diccionario,
        page_size=25,
        
       
        style_header=dict(backgroundColor="paleturquoise"),
        
        fill_width=False
    )],className="col colMain"),
    
],className="row"),className="container"),style={'margin-top':'2%'},className="container-fluid porPais")

#Finaliza el html
########################################################################################################
#genera una lista de 2 valores, para el grafico de pie
def generarListaChart(names):
    return [sumarValues(str(names)),(actualizarTotal()[tipoGraph])-sumarValues(str(names))]
#############################################################################################
#Genera el grafico de pastel
@app.callback(
    Output("pie-chart", "figure"), 
    [Input("names", "value"), 
     Input("values", "value")])
def generate_chart(names, values):
    global paiselect,tipoGraph
    paiselect[0]=names
    fig = px.pie(emision, values=generarListaChart(names), names=paiselect)
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=['pink','green'], line=dict(color='#000000', width=2)))
    fig.update_layout(paper_bgcolor='rgba(85, 85, 85, 0)',font_color="white")
    fig.update_layout(
    legend=dict(
        font=dict(
            family="Courier",
            size=12,
            color="white",
        )
    )
) 
    return fig

###########################################################################################################
#Cambia el pais o region seleccionada dependiendo cual se seleccione de la tabla

@app.callback(
    Output("names", "value"), 
    [Input("table", "active_cell"),Input("names", "value"),Input("table", "page_current"),Input("changeGraph", "n_clicks")])
def change(names,actual,page,click):
    global clickGraph,tipoGraph
    if click!=clickGraph:
        clickGraph+=1
        tipoGraph+=1
    if tipoGraph==3:
        tipoGraph=0

    if(page==None):
        page=0
    
    if(names==None or names["column"]!=0):
        return actual
    else:
        return pais1[names["row"]+(page*25)]
############################################################################################################
#Cambia el label del titulo del grafico dependiendo de cual se selecciona
@app.callback(
    Output("tipoGraphTitulo", "value"), 
    [Input("names", "value")])
def changeTitulo(names):
    global tipoGraph
    if tipoGraph==0:
        return "CO2"
    elif tipoGraph==1:
        return "GHG"
    else:
        return "Lluvias"
    
##########################################################################################################
#Genera el grafico de lineas
@app.callback(
    Output("line-chart", "figure"), 
    [Input("names", "value"),Input("paisRegion", "value")])
def update_line_chart(pais1,value):
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=yearsValues(pais1)[0], y=yearsValues(pais1)[1], name='CO2',
                         line=dict(color='black', width=4)))
    fig.add_trace(go.Scatter(x=yearsValues(pais1)[0], y=yearsValues(pais1)[2], name='Lluvia',
                         line=dict(color='blue', width=4)))
    fig.add_trace(go.Scatter(x=yearsValues(pais1)[0], y=yearsValues(pais1)[3], name='GHG',
                         line=dict(color='brown', width=4)))
    if(str(value)=='region'):
        fig.add_trace(go.Scatter(x=yearsValues(pais1)[0], y=yearsValues(pais1)[4], name='Climate',
                         line=dict(color='gray', width=4)))

    fig.update_xaxes(title_text="Año")
    fig.update_layout(plot_bgcolor='rgb(55,136,174)',paper_bgcolor='rgba(85, 85, 85, 0)',font_color="white")


    fig.update_layout(
    legend=dict(
        font=dict(
            family="Courier",
            size=12,
            color="white",
        )
    )
) 
    return fig

##################################################################################################################
#Cambia el tipo de tabla, ya sea para region o para pais
@app.callback(
    Output("paisRegion", "value"), 
    [Input("botonReg", "n_clicks")])
def updatePais(clicks):
    global paReg,nClicks,titulos2
    if clicks==0:
        return 'pais'
    if clicks!=nClicks:
        if paReg =='pais':
            nClicks=clicks
            paReg='region'
            titulos2=['Region','Year','Annual CO2 emissions (per capita)','Average monthly precipitation','Total GHG emissions excluding LUCF (CAIT)','Climate']
            return 'region'
        else:
            nClicks=clicks
            paReg='pais'
            titulos2=['Entity','Year','Annual CO2 emissions (per capita)','Average monthly precipitation','Total GHG emissions excluding LUCF (CAIT)','Region']
            return 'pais'
    else:
        return paReg



#####################################################################################################################
#Actualiza la tabla para dar paises o regiones, tambien hace funcionar el buscador por pais o region
@app.callback(
    Output("table", "data"), 
    [Input("search", "value"),Input("paisRegion", "value")])
def updateTable(valor,region):
            global pais1,emisiones1,years1,lluvias,emisiones2,listTemClimate
        
            if(valor is None):
                dTemp=makeDicc(region,diccionario)
                if(str(region)=='pais'):
                        pais1=pais11
                        emisiones1=emisiones11
                        years1=years1
                        lluvias=lluvias11
                        emisiones2=emisiones22
                        return dTemp
                
                else:
                    pais1=[]
                    emisiones1=[]
                    years1=[]
                    lluvias=[]
                    emisiones2=[]
                    listTemClimate=[]
                    for i in dTemp:
                        for o in listClimate:
                            if(i['Region']==o['Region'] and i['Year']==o['Year']):
                                i['Climate']=o['Climate']
                                break
                        listTemClimate.append(i['Climate'])
                        pais1.append(i['Region'])
                        emisiones1.append(i['Annual CO2 emissions (per capita)'])
                        years1.append(i['Year'])
                        lluvias.append(i['Average monthly precipitation'])
                        emisiones2.append(i['Total GHG emissions excluding LUCF (CAIT)'])
                    return dTemp
                    
            else:
                dTemp=[]
                pais1=[]
                emisiones1=[]
                years1=[]
                lluvias=[]
                emisiones2=[]
                listTemClimate=[]
                if(str(region)=='pais'):
                    for i in diccionario:
                        if(i['Entity'].upper()== str(valor).upper() or i['Entity'].upper().find(str(valor).upper())!=-1 ):
                            dTemp.append(i)
                else:
                    for i in diccionario:
                        if(i['Region'].upper()== str(valor).upper() or i['Region'].upper().find(str(valor).upper())!=-1 ):
                            dTemp.append(i)
                dTemp=makeDicc(region,dTemp)
                for i in dTemp:
                    for o in listClimate:
                            if(i['Region']==o['Region'] and i['Year']==o['Year']):
                                i['Climate']=o['Climate']
                                break
                    listTemClimate.append(i['Climate'])
                    if(str(region)=='pais'):
                        pais1.append(i['Entity'])
                    else:
                        pais1.append(i['Region'])
                    emisiones1.append(i['Annual CO2 emissions (per capita)'])
                    years1.append(i['Year'])
                    lluvias.append(i['Average monthly precipitation'])
                    emisiones2.append(i['Total GHG emissions excluding LUCF (CAIT)'])
                return dTemp
#################################################################################################
#Actualiza el diccionario de la tabla, utilizando el buscador
def makeDicc(region,dicc):
    global titulos2
    if(str(region)=='pais'):
        
        return dicc
    else:
       
        diccTemp=[]
        valor1=0
        valor2=0
        valor3=0
        
        for i in dicc:
            val=True
            for o in diccTemp:
                if i['Year']==o['Year'] and i['Region']==o['Region']:
                    o['Annual CO2 emissions (per capita)']+=i['Annual CO2 emissions (per capita)']
                    o['Average monthly precipitation']+=i['Average monthly precipitation']
                    o['Total GHG emissions excluding LUCF (CAIT)']+=i['Total GHG emissions excluding LUCF (CAIT)']
                    val=False
                    break
            if(val):
                diccTemp.append({'Region':i['Region'],'Year':i['Year'],'Annual CO2 emissions (per capita)':i['Annual CO2 emissions (per capita)'],'Average monthly precipitation':i['Average monthly precipitation'],'Total GHG emissions excluding LUCF (CAIT)':i['Total GHG emissions excluding LUCF (CAIT)']})
        return diccTemp




    

#####################################################################################################################
#actualiza los titulos de la tabla, al momento de cambiar de vista de pais o region
@app.callback(
    Output("table", "columns"),[Input("botonReg", "n_clicks")])
def updateColumns(dd):
    a= [{"name": i, "id": i} for i in titulos2]
    return a
################################################################



app.run_server(debug=True)
