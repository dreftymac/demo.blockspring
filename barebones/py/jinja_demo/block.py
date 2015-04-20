import blockspring

def block(request, response):
	name = "Hi! My name is " + request.params["first_name"]
	age = " and my age is " + str(request.params["age"])

	response.addOutput("intro", name + age)
	response.end()

blockspring.define(block)
