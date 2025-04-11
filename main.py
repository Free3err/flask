from flask import Flask, request, redirect, send_from_directory, url_for

app = Flask(__name__)


@app.route('/carousel', methods=['GET'])
def choice():
    return (
        f"""
            <!DOCTYPE html>
            <html>
            <head>
            <link rel="stylesheet" href="{url_for('static', filename='css/bootstrap.min.css')}">
            <script src="{url_for('static', filename='css/bootstrap.bundle.min.js')}"></script>
            <title>Пейзажи Марса</title>
            </head>
            <body>
            <div class="container mt-5" style="max-width: 800px;">
                <h1 class="text-center mb-4">Пейзажи Марса</h1>
                <div id="carouselExampleIndicators" class="carousel slide">
                  <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                  </div>
                  <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img class="d-block w-100" src="{url_for('static', filename='img/1.jpg')}">
                        </div>
                        <div class="carousel-item">
                            <img class="d-block w-100" src="{url_for('static', filename='img/2.jpg')}">
                        </div>
                        <div class="carousel-item">
                            <img class="d-block w-100" src="{url_for('static', filename='img/3.png')}">
                        </div>
                        <div class="carousel-item">
                            <img class="d-block w-100" src="{url_for('static', filename='img/4.png')}">
                        </div>
                        <div class="carousel-item">
                            <img class="d-block w-100" src="{url_for('static', filename='img/5.jpg')}">
                        </div>
                    </div>
                  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                  </button>
                  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                  </button>
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
