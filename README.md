# 通用爬虫
>##CrawlSpider
>可以指定规则来实现页面的提取，这些爬取规则由一个专门的数据结构Rule表示。
>Rule里包含了提取和跟进页面的配置，Spider会根据Rule来确定当前页面中的哪些
>链接需要继续爬取，哪些页面的爬取结果需要用到哪个方法解析。<br>
>Item Loader 使用Rule根据链接和爬取页面，Item Loader负责生成Item。  
>CrawlSpider继承自Spider类：  
>>* rules 爬取规则属性，包含了一个或多个Rule对象  
>>* parse_start_url() 可重写方法  
>
>Rule  
>>* link_extractor LinkExtractor(allow=(), deny=(), allow_domains=(), deny_domains=(), 
>>restrict_xpaths=(), restrict_css=(), tags=('a','area'), attrs=('href',))  
>>>* allow 正则表达式列表，从当前页面提取出的链接哪些是符合要求的，  
>>>* restrict_xpath 限制从哪些区域爬取<br>
>>>* domains 符合要求的域名才会生成Request<br>
>
>>* callback 每次从link_extractor中获取到链接时，该函数都会调用。该回调函数接收一个response作为第一个参数，
>>并返回一个包含Item或Request对象的列表。(注意：别覆盖parse函数)
>>* cb_kwargs 包含了返回给回调函数的参数  
>>* follow 布尔值，指定根据该规则从response提取的链接是否需要根据
>>* process_links 从link_extractor中获取到链接列表后，该函数被调用，主要用于过滤
>>* process_request 提取到request后，该函数就会被调用，对request进行处理，必须返回request或None
