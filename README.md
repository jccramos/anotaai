<h1>Anota-Ai Python-API</h1>

<h2>Welcome</h2>

<p>to Anota-ai API.&nbsp;<strong>Anota-ai is a mobile application that aims to enable the user to have detailed financial control (at the item level) in an agile and effective way, allowing him to map his lifestyle.</strong></p>

<p>Anota-ai&nbsp;application emerged in an academic context, at the federal university of santa catarina (<a href="https://ufsc.br/">UFSC</a>),&nbsp;conceived and initially developed by students of the Information Systems Course, during the General Systems Theory course. Currently, the project is devides between the mobile application and the Python-API that supports the app. To summarize, I mean that the mobile application is developed in other repository, that you can see <a href="https://github.com/CristianeMaragno/anota-ai">here</a>.</p>

<p>So<strong> what api is currently doing </strong>is fulfilling a request that delivers a <a href="https://www.gov.br/fazenda/pt-br">link to the Ministry of Finance</a>, where you can find detailed information about a tax coupon printed at the time of a purchase. The delivered link is generated through the QR-Code present on the printed coupon itself.</p>

<ul>
	<li>Here is an example of the request:</li>
</ul>

<hr />
<p style="margin-left:40px">```curl -X POST https://api-anotai.herokuapp.com/anotai -H &#39;Content-Type: application/json&#39; -d &#39;{&quot;url&quot;: &quot;https://sat.sef.sc.gov.br/nfce/consulta?p=42220902314041001583650080000025361825952526|2|1|1|E38A1560B7B59971A5DDE40975DA38A73B564F56&quot;}&#39;```</p>

<hr />
<ul>
	<li>And here, is the json cotaining the same information present on the&nbsp; printed coupon:</li>
</ul>

<hr />
<p style="margin-left:40px">```{&quot;local&quot;:{&quot;0&quot;:&quot;IGUASPORT LTDA&quot;,&quot;1&quot;:&quot;IGUASPORT LTDA&quot;,&quot;2&quot;:&quot;IGUASPORT LTDA&quot;,&quot;3&quot;:&quot;IGUASPORT LTDA&quot;,&quot;4&quot;:&quot;IGUASPORT LTDA&quot;,&quot;5&quot;:&quot;IGUASPORT LTDA&quot;,&quot;6&quot;:&quot;IGUASPORT LTDA&quot;,&quot;7&quot;:&quot;IGUASPORT LTDA&quot;,&quot;8&quot;:&quot;IGUASPORT LTDA&quot;},&quot;dt_emissao&quot;:{&quot;0&quot;:&quot;24\/09\/2022 17:34:03-03:00&quot;,&quot;1&quot;:&quot;24\/09\/2022 17:34:03-03:00&quot;,&quot;2&quot;:&quot;24\/09\/2022 17:34:03-03:00&quot;,&quot;3&quot;:&quot;24\/09\/2022 17:34:03-03:00&quot;,&quot;4&quot;:&quot;24\/09\/2022 17:34:03-03:00&quot;,&quot;5&quot;:&quot;24\/09\/2022 17:34:03-03:00&quot;,&quot;6&quot;:&quot;24\/09\/2022 17:34:03-03:00&quot;,&quot;7&quot;:&quot;24\/09\/2022 17:34:03-03:00&quot;,&quot;8&quot;:&quot;24\/09\/2022 17:34:03-03:00&quot;},&quot;descricao&quot;:{&quot;0&quot;:&quot;TONEMAT AOP2 M Sans taille&quot;,&quot;1&quot;:&quot;#PR# CTA MH100 ROXO FEM M&quot;,&quot;2&quot;:&quot;CSA AMAR KIPSTA BRASIL FEM COPA 202 XS&quot;,&quot;3&quot;:&quot;TOP ALCA RETA 500 PTO S&quot;,&quot;4&quot;:&quot;SH 2EM1 NEW 120 PTO OI22 M&quot;,&quot;5&quot;:&quot;CHINELO PTO IPANEMA GLITZZ FEM O 4142&quot;,&quot;6&quot;:&quot;PILATES MINIBAND LIGHT Sans taille&quot;,&quot;7&quot;:&quot;HALTER EMBORRACHADO 1KG T Sans taille&quot;,&quot;8&quot;:&quot;JR500 Rubber Bleu Sans taille&quot;},&quot;qtd&quot;:{&quot;0&quot;:1.0,&quot;1&quot;:1.0,&quot;2&quot;:1.0,&quot;3&quot;:1.0,&quot;4&quot;:1.0,&quot;5&quot;:1.0,&quot;6&quot;:1.0,&quot;7&quot;:2.0,&quot;8&quot;:1.0},&quot;un_comercial&quot;:{&quot;0&quot;:&quot;UN&quot;,&quot;1&quot;:&quot;UN&quot;,&quot;2&quot;:&quot;UN&quot;,&quot;3&quot;:&quot;UN&quot;,&quot;4&quot;:&quot;UN&quot;,&quot;5&quot;:&quot;UN&quot;,&quot;6&quot;:&quot;UN&quot;,&quot;7&quot;:&quot;UN&quot;,&quot;8&quot;:&quot;UN&quot;},&quot;vl_unit&quot;:{&quot;0&quot;:269.99,&quot;1&quot;:49.99,&quot;2&quot;:59.99,&quot;3&quot;:99.99,&quot;4&quot;:79.99,&quot;5&quot;:39.99,&quot;6&quot;:44.99,&quot;7&quot;:29.99,&quot;8&quot;:39.99},&quot;vl_prod&quot;:{&quot;0&quot;:269.99,&quot;1&quot;:49.99,&quot;2&quot;:59.99,&quot;3&quot;:99.99,&quot;4&quot;:79.99,&quot;5&quot;:39.99,&quot;6&quot;:44.99,&quot;7&quot;:59.98,&quot;8&quot;:39.99}}```</p>

<hr />
<p>Anotai-api is being able to do this via data scraping, which is accomplished by the <a href="https://github.com/jccramos/anotai/blob/main/crawler.py#L31">mk_table</a> function,&nbsp;which in turn uses the request library to get the source code of the html page and BeautifulSoup/Pandas to extract the information from the html code, and turn it into structured data.</p>

<h2>Get Started</h2>

<ol>
	<li>Clone this repo inside a virtual-enviroment, and install with pip the librarys listed in requirements.text, of if you prefer, we rommend you to install poetry, and run Make Install. Poetry creates the virtual-enviroment when you do it.</li>
	<li>To run this project go into the&nbsp;directory you cloned this repo, actrivate your virtual enviroment and&nbsp;run `python3.10.8 run app.py`, or if you prefered to install poetry, justo go into the direcory you cloned this repo, and run `poetry run python app.py`</li>
	<li>Open the local link (devolpment mode), and in other terminal just copy and paste the same code used in the example above, and showed bellow:</li>
</ol>

<p style="margin-left:40px">```curl -X POST http://127.0.0.1:5000/anotai -H &#39;Content-Type: application/json&#39; -d &#39;{&quot;url&quot;: &quot;https://sat.s&quot;https://sat.sef.sc.gov.br/nfce/consulta?p=42220902314041001583650080000025361825952526|2|1|1|E38A1560B7B59971A5DDE40975DA38A73B564F56&quot;}&#39;```</p>

<p style="margin-left:40px">At this point, you must get a json data structure informing the tax cupom contet.</p>

<h2>Deploy</h2>

<p>Currently the deploy is beeing done using <a href="https://devcenter.heroku.com/categories/reference">Heroku</a> (Platform as a Service, PaaS). The WEB API is available for POST requests via <a href="http://is available for POST requests via https://api-anotai.herokuapp.com/">https://api-anotai.herokuapp.com/</a>.</p>

<h2>Future Features</h2>

<p>Well, thanks if you&#39;ve read this far. Feel free to suggest any features or contribute with us. So far it&#39;s still an academic Python API, but we intend to make it bigger. Discussions about the future are happening now, the way to make this data available to the user is still being defined, as well as the use of the data by the Anota-Ai application. Among the upcoming features, there are some that we would like to highlight such as:</p>

<ol>
	<li>Create classification for each item type;</li>
	<li>Create visuals, in addition to tables, for users to track their spending;</li>
	<li>Make it possible for users to share data in order to compare prices in certain locations;</li>
</ol>

<p>Come and join us to help us create an item-level financial app that enables the user to map their lifestyle and effectively control their spending.</p>

<hr />
<p>&nbsp;</p>
