def web_page():
  html = """<html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * {
          box-sizing: border-box;
        }

        input[type=text], input[type=password], input[type=number] {
          width: 100%;
          padding: 12px;
          border: 1px solid #ccc;
          border-radius: 4px;
          resize: vertical;
        }

        label {
          padding: 12px 12px 12px 0;
          display: inline-block;
        }

        input[type=submit] {
          background-color: #04AA6D;
          color: white;
          padding: 12px 20px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          float: right;
        }

        input[type=submit]:hover {
          background-color: #45a049;
        }

        .container {
          border-radius: 5px;
          background-color: #f2f2f2;
          padding: 20px;
        }

        .col-25 {
          float: left;
          width: 25%;
          margin-top: 6px;
        }

        .col-75 {
          float: left;
          width: 75%;
          margin-top: 6px;
        }

        .row:after {
          content: "";
          display: table;
          clear: both;
        }
    </style>

    </head>
      <body>
      <div class="container">
      <h2>Setup</h2>
          <form action="/onSubmit">
            <h4>Wifi Config!</h4>
            <div class="row">
                <div class="col-25">
                  <label for="ssid">SSID:</label><br>
                </div>
                <div class="col-75">
                  <input type="text" id="ssid" name="ssid" required placeholder="Enter wifi name">
                </div>
            </div>

            <div class="row">
                <div class="col-25">
                  <label for="password">Password:</label><br>
                </div>
                <div class="col-75">
                  <input type="password" id="password" name="password" required placeholder="Enter wifi password" >
                </div>
            </div>
            <br><br>
            <h4>MQTT Config!</h4>
            <div class="row">
                <div class="col-25">
                  <label for="ip">IP/Domain:</label><br>
                </div>
                <div class="col-75">
                  <input type="text" id="ip" name="ip" required placeholder="Enter Broker ip / Domain Name">
                </div>
            </div>
            
            <div class="row">
                <div class="col-25">
                  <label for="port">Port:</label><br>
                </div>
                <div class="col-75">
                  <input type="number" id="port" name="port" required>
                </div>
            </div>
            <br>
            
            <div class="row">
                <input type="submit" value="Submit">
            </div>
          </form>
        </div>
      </body>
  </html>"""
  return html
