##"       左侧不留白".lstrip()
##"右侧不留白       ".rsrtip()
##"       都不留白       ".srtip()
###括号里填入部分字符可以直接删去，但是是按照单个字符单位去剔除
##"www . ilovefishc.com" .removeprefix( "www." )
##"www . ilovefishc.com" .removesuffix( ".com" )
#删除的是匹配的整体字符串

#拆分和拼接
"www.ilovefishc.com".partition(".")#从左到右

"www.ilovefishc.com".rpartition(".")#从右到左

"苟日新，日日新，交日新".split('，',1)#从左到右,后面的参数时确定切几次

"苟日新，日日新，交日新".rsplit('，')#从右到左

"苟日新\n日日新\r交日新\n".splitlines()#直接按行返回

#拼接
".".join(["a","b","c","d"])
".".join(("a","b","c","d"))
#join效率高于“+”
