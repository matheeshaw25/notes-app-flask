from website import create_app

app =create_app()

if __name__ == '__main__':
    app.run(debug=True) # run the webserver (debug=True because whenever we make a change it will automatically run webserver)