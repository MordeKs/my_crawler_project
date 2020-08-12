# -*- encoding: utf-8 -*-
"""
@File    : sub.py
@Time    : 2020/8/12 17:31
@Author  : Morde
@Software: PyCharm
@Description:
"""
import re
html = """
    <div id="cnblogs_post_body" class="blogpost-body cnblogs-markdown">
    <h2 id="title-python正则表达式中的resdate-2014-12-21-095554categories-pythontags-正则表达式python">title: Python正则表达式中的re.S<br>
date: 2014-12-21 09:55:54<br>
categories: [Python]<br>
tags: [正则表达式,python]</h2>
<p>在Python的正则表达式中，有一个参数为re.S。它表示“.”（不包含外侧双引号，下同）的作用扩展到整个字符串，包括“\n”。看如下代码：</p>
<pre><code class="hljs python"><span class="hljs-keyword">import</span> re
a = <span class="hljs-string">'''asdfsafhellopass:
	234455
	worldafdsf
	'''</span>
b = re.findall(<span class="hljs-string">'hello(.*?)world'</span>,a)
c = re.findall(<span class="hljs-string">'hello(.*?)world'</span>,a,re.S)
<span class="hljs-keyword">print</span> <span class="hljs-string">'b is '</span> , b
<span class="hljs-keyword">print</span> <span class="hljs-string">'c is '</span> , c
</code></pre>
<p>运行结果如下：</p>
<pre><code class="hljs coffeescript">b <span class="hljs-keyword">is</span>  []
c <span class="hljs-keyword">is</span>  [<span class="hljs-string">'pass:\n\t234455\n\t'</span>]
</code></pre>
<p>正则表达式中，“.”的作用是匹配除“\n”以外的任何字符，也就是说，它是在一行中进行匹配。这里的“行”是以“\n”进行区分的。a字符串有每行的末尾有一个“\n”，不过它不可见。</p>
<p>如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。</p>
<p>在re.py库的介绍中有以下语句：</p>
<blockquote>
<p>"."      Matches any character except a newline.</p>
</blockquote>
<blockquote>
<p>S  DOTALL      "." matches any character at all, including the newline.</p>
</blockquote>
<p>这里特别感谢评论中叫做Style的朋友指出了我的错误。</p>

</div>
"""

a = re.sub(r'<.*?>','',html,flags=re.S)
print(a)