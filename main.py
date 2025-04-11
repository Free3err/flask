from flask import Flask, request, redirect, send_from_directory

app = Flask(__name__)


@app.route('/load_photo', methods=['GET', "POST"])
def choice():
    if request.method == "POST":
        img = request.files['file']
        img.save('static/img/avatar.png')
        return redirect("/load_photo", code=302)
    else:
        return (
            f"""
            <!DOCTYPE html>
            <html>
            <head>
            <link rel="stylesheet" href="/static/css/bootstrap.min.css">
            <title>Загрузка фотографии</title>
            </head>
            <body>
            <div class="container mt-4">
                <h1 class="text-center"><b>Загрузка фотографии</b></h1>
                <h4 class="text-center"><b>для участия в миссии</b></h4>
                <div class="alert alert-warning">
                    <form action="/load_photo" class="d-flex flex-column align-items-center" method="post" enctype=multipart/form-data>
                        <div class="mb-3">
                            <label class="form-label">Приложите фотографию</label>
                            <input type="file" class="form-control" name="file" accept="image/*" required/>
                        </div>
                        <img src="static/img/avatar.png" alt='' class="img-fluid mb-3 "/>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </div>
            </div>
            </body>
            </html>
            """
        )


@app.route('/static/<path>')
def stat(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(debug=True)
