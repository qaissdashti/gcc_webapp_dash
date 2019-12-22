import pandas as pd
import plotly.graph_objs as go


def clean_file_qaiss(dataset, keep_col = ['Country Name', '2000', '2018']):
    df=pd.read_csv(dataset, skiprows=4)
    df = df[keep_col]
    country_list_arab = ['Kuwait', 'Saudi Arabia', 'Oman', 'Qatar', 'Bahrain', 'United Arab Emirates', 'Spain']
    df = df[df['Country Name'].isin(country_list_arab)]
    df_melt = df.melt(id_vars='Country Name', value_vars=['2000', '2018'])
    df_melt.columns = ['country', 'year', 'gdp']
    df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year
    return df_melt


def return_figures():
    graph_one = []
    df = clean_file_qaiss('data/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_566085.csv')
    country_list_arab = ['Kuwait', 'Saudi Arabia', 'Oman', 'Qatar', 'Bahrain', 'United Arab Emirates', 'Spain']
    
    for country in country_list_arab:
        x_val = df[df['country'] == country].year.tolist()
        y_val = df[df['country'] == country].gdp.tolist()
        graph_one.append(
        go.Scatter(
        x = x_val,
        y = y_val,
        mode = 'lines',
        name = country)
        )
        
    layout_one = dict(title = 'Gulfies GDP comparison 2000 to 2018 <br> with Spain',
                xaxis = dict(title = 'Year',
                  autotick=False, tick0=2000, dtick=25),
                yaxis = dict(title = 'Gulf GDP'),
                )
    
    #chart two
    graph_two = []
    df = clean_file_qaiss('data/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_566085.csv')
    df.columns = ['country','year','gdp']
    df.sort_values('gdp', ascending=False, inplace=True)
    df = df[df['year'] == 2018] 

    graph_two.append(
      go.Bar(
      x = df.country.tolist(),
      y = df.gdp.tolist(),
      )
    )

    layout_two = dict(title = 'Gulfies GDP Bar Chart 2018 VS Spain ',
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'GDP'),
                )
    
    
    graph_three = []
    df = clean_file_qaiss('data/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_566054.csv')
    country_list_arab = ['Kuwait', 'Saudi Arabia', 'Oman', 'Qatar', 'Bahrain', 'United Arab Emirates', 'Spain']
    
    for country in country_list_arab:
        x_val = df[df['country'] == country].year.tolist()
        y_val = df[df['country'] == country].gdp.tolist()
        graph_three.append(
        go.Scatter(
        x = x_val,
        y = y_val,
        mode = 'lines',
        name = country)
        )
        
    layout_three = dict(title = 'Gulfies GDP / capita comparison 2000 to 2018 <br> with Spain',
                xaxis = dict(title = 'Year',
                  autotick=False, tick0=2000, dtick=25),
                yaxis = dict(title = 'Gulf GDP/Capita'),
                )
    
    
    graph_four = []
    df = clean_file_qaiss('data/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_566054.csv')
    country_list_arab = ['Kuwait', 'Saudi Arabia', 'Oman', 'Qatar', 'Bahrain', 'United Arab Emirates', 'Spain']
    
    for country in country_list_arab:
        x_val = df[df['country'] == country].year.tolist()
        y_val = df[df['country'] == country].gdp.tolist()
        graph_four.append(
        go.Bar(
        x = df.country.tolist(),
        y = df.gdp.tolist(),
        )
        )

    layout_four = dict(title = 'Gulfies GDP/Capita as Bar 2018 VS Spain ',
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'GDP/Capita'),
                )
    
    
    
    
    
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    
    return figures
    