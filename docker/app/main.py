from fastapi import FastAPI
from .triton import run
# from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:8000",
#     "172.17.0.1"
#     "127.0.0.1"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
app = FastAPI()


@app.get("/triton-api")
def read_root():
    return run()
@app.get("/" ,response_class=HTMLResponse)
def read_page():
    data = run()
    return """
<html lang="en">
<head>
<title>TRITON</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <link rel="shortcut icon" href="#">
</head>
<style>
    table, th, td {
      border:1px solid rgb(0, 151, 151);
    }
    body{
    background: rgb(39, 40, 41);
    color: rgb(255, 255, 255);
    }
    h1, h2 {
        color: rgb(0, 195, 255);
    }
    </style>"""+  f"""
<body>
           <h1>TRITON</h1>
        <h2>GAIN : ${data["Gain"]}€</h2>
        <table >
  <tr>
    <th>Current Unit Price </th>
    <th> Value (705.864 units)</th>
    <th>Clear Value (- 160 fee)</th>
    <th>Gain</th>
    <th>Gain %</th>
  </tr>
  <tr>
    <td>${data['current unit Price']}€</td>
    <td>${data['Value (705.864 units)']}€</td>
    <td>${data['Clear_Value (- 160 fee)']}€</td>
    <td>${data['Gain']}€</td>
    <td> ${data['Gain_%']}%</td>
  </tr>

</table>
</body>
    </html>
    """