from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

<link rel="stylesheet" href="assets/style.css">
</head>

<body>
<div class="top">
<img src="assets/images/logo.jpg" alt="logo-icon"/>
<a href=" " >Home</a>
<a href=" " >Women</a>
<a href=" " >Men</a>
<a href=" " >Kids</a>
<a href=" " >Brands</a>
<a href=" " >Contact</a>
<div class="input-box">
<i class="bi bi-search"></i>
<input  type="text" name="Search-item" placeholder="Search"/>
</div>
</div>
<div class="brand">
<h1><i>DASHING TRENDS</i></h1>
</div>
<div class="container">
<div class="cards">
<div class="card">
  <img src="assets/images/card.jpg" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Fashion</h5>
    <p class="card-text">Explore 100 years fashion trends of Dashing Trends!!</p>
    <a href="#" class="btn btn-primary">Explore!</a>
  </div>
</div>

<div class="card">
  <img src="assets/images/jk.jpeg" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Shop</h5>
    <p class="card-text">Best selling products of 2024!!</p>
    <a href="#" class="btn btn-primary">Explore!</a>
  </div>
</div>
</div>

<div class="carousel">
<div id="carouselExampleIndicators" class="carousel slide">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="assets/images/car1.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="assets/images/line.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="assets/images/shirt.jpg" class="d-block w-100" alt="...">
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

</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>

</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        if self.path == '/assets/style.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('assets/style.css', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/assets/images/logo.jpg':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            with open('assets/images/logo.jpg', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/assets/images/car1.jpg':
            self.send_response(200)
            self.send_header('Content-type', 'image/avif')
            self.end_headers()
            with open('assets/images/car1.jpg', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/assets/images/brand.jpg':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpg')
            self.end_headers()
            with open('assets/images/brand.jpg', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/assets/images/line.jpg':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpg')
            self.end_headers()
            with open('assets/images/line.jpg', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/assets/images/shirt.jpg':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpg')
            self.end_headers()
            with open('assets/images/shirt.jpg', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/assets/images/card.jpg':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpg')
            self.end_headers()
            with open('assets/images/card.jpg', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/assets/images/jk.jpeg':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            with open('assets/images/jk.jpeg', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running...")
httpd.serve_forever()