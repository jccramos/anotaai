# Anota-Ai Python-API
## Welcome

_to Anota-ai API_. **Anota-ai is a mobile application that aims to enable the user to have detailed financial control (at the item level) in an agile and effective way, allowing him to map his lifestyle.**

Anota-ai application emerged in an academic context, at the federal university of santa catarina ([UFSC](https://ufsc.br/)), conceived and initially developed by students of the Information Systems Course, during the General Systems Theory course. Currently, the project is devides between the mobile application and the Python-API that supports the app. To summarize, I mean that the mobile application is developed in other repository, that you can see [here](https://github.com/CristianeMaragno/anota-ai).

So what api is currently doing is fulfilling a request that delivers a link to the (Ministry of Finance)[https://www.gov.br/fazenda/pt-br], where you can find detailed information about a tax coupon printed at the time of a purchase. The delivered link is generated through the QR-Code present on the printed coupon itself.

- Here is an example of the request:
```
curl -X POST https://api-anotai.herokuapp.com/anotai -H 'Content-Type: application/json' -d '{"url": "https://sat.sef.sc.gov.br/nfce/consulta?p=42220902314041001583650080000025361825952526|2|1|1|E38A1560B7B59971A5DDE40975DA38A73B564F56"}'
```
- And here, is the json cotaining the same information present on the  printed coupon:
```
{"local":{"0":"IGUASPORT LTDA","1":"IGUASPORT LTDA","2":"IGUASPORT LTDA","3":"IGUASPORT LTDA","4":"IGUASPORT LTDA","5":"IGUASPORT LTDA","6":"IGUASPORT LTDA","7":"IGUASPORT LTDA","8":"IGUASPORT LTDA"},"dt_emissao":{"0":"24\/09\/2022 17:34:03-03:00","1":"24\/09\/2022 17:34:03-03:00","2":"24\/09\/2022 17:34:03-03:00","3":"24\/09\/2022 17:34:03-03:00","4":"24\/09\/2022 17:34:03-03:00","5":"24\/09\/2022 17:34:03-03:00","6":"24\/09\/2022 17:34:03-03:00","7":"24\/09\/2022 17:34:03-03:00","8":"24\/09\/2022 17:34:03-03:00"},"descricao":{"0":"TONEMAT AOP2 M Sans taille","1":"#PR# CTA MH100 ROXO FEM M","2":"CSA AMAR KIPSTA BRASIL FEM COPA 202 XS","3":"TOP ALCA RETA 500 PTO S","4":"SH 2EM1 NEW 120 PTO OI22 M","5":"CHINELO PTO IPANEMA GLITZZ FEM O 4142","6":"PILATES MINIBAND LIGHT Sans taille","7":"HALTER EMBORRACHADO 1KG T Sans taille","8":"JR500 Rubber Bleu Sans taille"},"qtd":{"0":1.0,"1":1.0,"2":1.0,"3":1.0,"4":1.0,"5":1.0,"6":1.0,"7":2.0,"8":1.0},"un_comercial":{"0":"UN","1":"UN","2":"UN","3":"UN","4":"UN","5":"UN","6":"UN","7":"UN","8":"UN"},"vl_unit":{"0":269.99,"1":49.99,"2":59.99,"3":99.99,"4":79.99,"5":39.99,"6":44.99,"7":29.99,"8":39.99},"vl_prod":{"0":269.99,"1":49.99,"2":59.99,"3":99.99,"4":79.99,"5":39.99,"6":44.99,"7":59.98,"8":39.99}}
```

Anotai-api is being able to do this via data scraping, which is accomplished by the [mk_table](https://github.com/jccramos/anotai/blob/main/crawler.py#L31) function, which in turn uses the request library to get the source code of the html page and BeautifulSoup/Pandas to extract the information from the html code, and turn it into structured data.

## Get Started
1. Clone this repo inside a virtual-enviroment, and install with pip the librarys listed in requirements.text, of if you prefer, we rommend you to install poetry, and run Make Install. Poetry creates the virtual-enviroment when you do it.
2. To run this project go into the directory you cloned this repo, actrivate your virtual enviroment and run `python3.10.8 run app.py`, or if you prefered to install poetry, justo go into the direcory you cloned this repo, and run `Make app dry`
3. Open the local link (devolpment mode), and in other terminal just copy and paste the same code used in the example above, and showed bellow:
```curl -X POST http://127.0.0.1:5000/anotai -H 'Content-Type: application/json' -d '{"url": "https://sat.s"https://sat.sef.sc.gov.br/nfce/consulta?p=42220902314041001583650080000025361825952526|2|1|1|E38A1560B7B59971A5DDE40975DA38A73B564F56"}'```
At this point, you must get a json data structure informing the tax cupom contet.

## Deploy
Currently the deploy is beeing done using [Heroku](https://devcenter.heroku.com/categories/reference) (Platform as a Service, PaaS). The WEB API is available for **POST requests** via [https://api-anotai.herokuapp.com/](https://api-anotai.herokuapp.com/).

## Future Features
Well, thanks if you've read this far. Feel free to suggest any features or contribute with us. So far it's still an academic Python API, but we intend to make it bigger. Discussions about the future are happening now, the way to make this data available to the user is still being defined, as well as the use of the data by the Anota-Ai application. Among the upcoming features, there are some that we would like to highlight such as:

1. Create classification for each item type;
2. Create visuals, in addition to tables, for users to track their spending;
3. Make it possible for users to share data in order to compare prices in certain locations;

Come and join us to help us create an item-level financial app that enables the user to map their lifestyle and effectively control their spending.

