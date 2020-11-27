from flask import Flask, redirect, render_template, request

base_grant_url = "https://n17.meraki.com/splash/grant"
user_continue_url = "https://google.com"
success_url = ""

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
	global base_grant_url
	global user_continue_url
	global success_url

	host = request.host_url
# 	base_grant_url = request.args.get('base_grant_url')
# 	user_continue_url = request.args.get('user_continue_url')
	node_mac = request.args.get('node_mac')
	client_ip = request.args.get('client_ip')
	client_mac = request.args.get('client_mac')
	success_url = host + "success"

	return render_template(
		"index.html",
		client_ip=client_ip,
		client_mac=client_mac,
		node_mac=node_mac,
		user_continue_url=user_continue_url,
		success_url=success_url,
	)


@app.route("/login", methods=["POST"])
def login():
	# redirect to splash page
	email = request.form['user_email_address']
	with open('a.csv', 'a+') as f:
		f.write(email+'\n')
	redirect_url = base_grant_url + "?continue_url=" + success_url
	return redirect(redirect_url)


@app.route("/success", methods=["GET"])
def success():
	global user_continue_url
	return render_template(
		"success.html",
		user_continue_url=user_continue_url,
	)


if __name__ == "__main__":
	app.run(debug=True)
