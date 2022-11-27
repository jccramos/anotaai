import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def retry_get(*args, **kwargs):
    attempts = 1
    while attempts < 4:
        try:
            html = requests.get(*args, **kwargs)
            if 'Server Error' in html:
                raise ConnectionError
            return html
        except requests.exceptions.RequestException:
            print('ERRO', *args, **kwargs)
            attempts += 1
    return None


def get_where(soup):
    td = soup.find_all('td', class_="col-2")
    return str(td[0]).split(">")[4].split("<")[0]


def get_when(soup):
    span = soup.find_all('span')
    return str(span[3]).split(">")[1].split("<")[0]


def mk_table(url, where, when):
    tables =  pd.read_html(url)
    for table in tables:
        if table.shape[1] == 6:
            if type(table.iloc[0][0]) == np.float64:
                raw_table = table
    return (
        raw_table.drop(index=0, columns=0)
        .rename(
            columns={
                1: "descricao",
                2: "qtd",
                3: "un_comercial",
                4: "vl_unit",
                5: "vl_prod"
            }
        )
        .assign(local = where)
        .assign(dt_emissao = lambda df: when)
        .assign(qtd = lambda df: df["qtd"].apply(lambda x: int(x)/10000))
        .assign(vl_unit = lambda df: df["vl_unit"].apply(lambda x: int(x)/100))
        .assign(vl_prod = lambda df: df["vl_prod"].apply(lambda x: int(x)/100))
        .reset_index(drop=True)
        [
            [
                "local",
                "dt_emissao",
                "descricao",
                "qtd",
                "un_comercial",
                "vl_unit",
                "vl_prod"
            ]
        ]
    )


def main(url):
    r = retry_get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')

    where = get_where(soup)
    when = get_when(soup)

    table_item = mk_table(url, where, when)
    
    table_local = (
        table_item
        [["local", "dt_emissao", "vl_prod"]]
        .groupby(["local", "dt_emissao"])
        .sum()
        .reset_index()
    )
    
    return table_item, table_local
