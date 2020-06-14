# 通用爬虫
>- configs/ 通用爬虫的配置
>- spiders/universal 通用爬虫
>- rules.py 存放爬取规则
>- urls.py 存放动态生成链接函数
>- utils.py 一些实用的函数集合  
>## CrawlSpider
>指定规则来实现页面提取，这些爬取规则由一个专门的数据结构Rule表示。
>Rule里包含了提取和跟进页面的配置，Spider会根据Rule来确定当前页面中的哪些
>链接需要继续爬取，哪些页面的爬取结果需要用到哪个方法解析。  
>Item Loader 使用Rule根据链接和爬取页面，Item Loader负责生成Item。  
>CrawlSpider继承自Spider类：  
>>* link_extractor 跟进链接
>>* rules 爬取规则属性，包含了一个或多个Rule对象  
>>* parse_start_url() 可重写方法  
>>* callback 每次从link_extractor中获取到链接时，该函数都会调用。该回调函数接收一个response作为第一个参数，
>>并返回一个包含Item或Request对象的列表。(注意：别覆盖parse函数)
>>* cb_kwargs 包含了返回给回调函数的参数  
>>* follow 布尔值，指定根据该规则从response提取的链接是否需要根据
>>* process_links 从link_extractor中获取到链接列表后，该函数被调用，主要用于过滤
>>* process_request 提取到request后，该函数就会被调用，对request进行处理，必须返回request或None
>
>## LinkExtractor类  
>> LinkExtractor(allow=(), deny=(), allow_domains=(), deny_domains=(), 
>>restrict_xpaths=(), restrict_css=(), tags=('a','area'), attrs=('href',))  
>>>* allow 正则表达式列表，从当前页面提取出的链接哪些是符合要求的   
>>>* restrict_xpath 限制从哪些区域爬取  
>>>* domains 符合要求的域名才会生成Request  
>
>## ItemLoader类
>负责提取item，主要包括了对item赋值，和提取item  
>add_xpath() add_css() add_value()等为item的字段赋值，
>default_output_processor 默认完整输出
><key>_out 作为item字段的处理器
>
>## UniversalSpider类
>主要用到了配置文件/configs/*.json
>格式如下：  
>```
>{
>   "spider": 爬虫类名 一般为universal,
>   "start_urls": 起始链接 分为静态和动态两种,
>   "allowed_domains": [] 允许跟进的域名,
>   "rules": "china", 这里使用rules.py中名为china的规则,
>   "item": {
>       "class": "NewsItem" 待填充的item,
>       "loader": "ChinaLoader" 使用的Item加载器,
>       "attrs": {} Item的字段的赋值规则
>   }
>}
>```
>起始链接可以静态或者是动态生成：  
>```
>"start_urls":{
>   “type": "static",
>   "value": [str, ...]
>}
>```
>或者
>```
>"start_urls":{
>   “type": "dynamic",
>   "method": "china",
>   "args": []
>}
>```
>会调用urls.china方法，并传入args列表，得到链接
>
>```
>"source": [
>	{
>		"method": "xpath",
>		"args": [
>			"//div[@id='chan_newsInfo']/text()"
>		],
>		"re": "来源：(.*?)"
>	}
>],
>```
>表示，为source字段赋值，使用add_xpath("//div[@id='chan_newsInfo']/text()")
>并从提取到的文本中，再以正则表达式"来源：(.*?)"提取出文本