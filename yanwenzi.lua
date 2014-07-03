function yanwenzi()
	return "T.T"
end

ime.register_trigger("yanwenzi","yanwenzi",{"ywz","yanwenzi","yan","yy"},{})
--这一行的作用是将函数"HelloWorld"注册为谷歌拼音输入法的一个整合扩展。
--第一个参数是扩展对应的入口函数"HelloWorld"，
--第二个参数是简短说明文字，
--第三个参数给出希望将扩展关联到哪个或哪几个用户输入串
--，第四个参数给出希望将扩展关联到哪个或哪几个特定的候选词（这里是空表，表示不关联）。
function yanwenziComm()
	return {"-___-","^_^"}
end
ime.register_command("yw", "yanwenziComm", "颜文字")

function HelloWorld()
  return "Hello,World!"
end

ime.register_trigger("HelloWorld", "test", { "hello" }, {})