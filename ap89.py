from flask import Flask, render_template, url_for, request, redirect
import config

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
    <html>
        <head>
            <title> XD </title>
            <style>
                @keyframes p1frame {{
                    0% {{ transform: translate(0px, 0px); color: #1b1919; }}
                    25% {{ transform: translate(50px , -50px); color: #464646; }}
                    50% {{ color: #969696; }}
                    75% {{ transform: translate(-50px , 50px); color: #464646; }}
                    100% {{ transform: translate(0px, 0px); color: #000000; }}
                }}
                body {{
                    background-color: #292929;
                    color: white;
                    font-family: Arial, sans-serif;
                    text-align: center;
                }}
                a {{
                    display: block;
                    color: #092b9e;
                    font-size: 20px;
                    margin: 10px auto;
                    text-decoration: none;
                }}
                a:hover {{
                    color: #ff5500;
                }}
            </style>
        </head>
        <body>
            <h1> Selam! </h1>
            <p> Ben Dodukan89! Aşağıda merak ettiğin yerler varsa bir bakmanı isterim :D </p>
            
            <a href="{url_for('home01')}">Teknoloji bağımlılığı hakkında bilgiler!</a>
            <a href="{url_for('home02')}">Ultrakill</a>
            <a href="{url_for('sifre01')}">Yetkili Harici Giremez</a>
            <a href="{url_for('sifre02')}">Yetkili Harici Giremez</a>
        </body>
    </html>
    '''

@app.route('/teknoloji-bagimliligi')
def home01():
    return render_template('index.html')

@app.route('/ultrakill')
def home02():
    return render_template("M3L1.html")

@app.route('/sifre-kontrol', methods=['GET', 'POST'])
def sifre01():
    if request.method == 'POST':
        girilen_sifre = request.form.get('sifre')
        config.ilksifre

        print("Girilen şifre:", girilen_sifre)
        print("Doğru şifre:", config.ilksifre)
        if girilen_sifre.strip() == config.ilksifre.strip():
            return redirect(url_for("yetkili_sayfa"))
        else:
            return "Yanlış şifre! Tekrar deneyin.", 403
        
    return '''
<!DOCTYPE html>
<html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Güvenlik Duvarı</title>
        <style>
            body {
                text-align: center;
                background-color: #121212;
                color: white;
                font-family: Arial, sans-serif;
            }
            h2 {
                text-align: center;
                font-size: 24px;
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin-top: 20px;
            }
            input {
                padding: 10px;
                width: 200px;
                font-size: 16px;
                margin-bottom: 10px;
                border: 1px solid white;
                background: transparent;
                color: white;
                border-radius: 5px;
                text-align: center;
            }
            input::placeholder {
                color: rgba(255, 255, 255, 0.7);
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
                border-radius: 5px;
                transition: 0.3s;
            }
            button:hover {
                background-color: #ff5500;
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <h2>Bu sayfaya erişmek için şifre girin:</h2>
        <form method="POST">
            <input type="password" name="sifre" placeholder="Şifre girin..." required>
            <br>
            <button type="submit">Giriş</button>
        </form>
    </body>
</html>
'''

@app.route('/sifre-kontrol-2', methods=['GET', 'POST'])
def sifre02():
    if request.method == 'POST':
        girilen_sifre = request.form.get('sifre')
        config.ikincisifre

        print("Girilen şifre:", girilen_sifre)
        print("Doğru şifre:", config.ikincisifre)
        if girilen_sifre.strip() == config.ikincisifre.strip():
            return redirect(url_for("fazladan_bir_sayfa"))
        else:
            return "Yanlış şifre! Tekrar deneyin.", 403
        
    return '''
    <!DOCTYPE html>
    <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Güvenlik Duvarı</title>
            <style>
                body {
                    text-align: center;
                    background-color: #121212;
                    color: white;
                    font-family: Arial, sans-serif;
                }
                h2 {
                    text-align: center;
                    font-size: 24px;
                }
                form {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    margin-top: 20px;
                }
                input {
                    padding: 10px;
                    width: 200px;
                    font-size: 16px;
                    margin-bottom: 10px;
                    border: 1px solid white;
                    background: transparent;
                    color: white;
                    border-radius: 5px;
                    text-align: center;
                }
                input::placeholder {
                    color: rgba(255, 255, 255, 0.7);
                }
                button {
                    padding: 10px 20px;
                    font-size: 16px;
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    cursor: pointer;
                    border-radius: 5px;
                    transition: 0.3s;
                }
                button:hover {
                    background-color: #ff5500;
                    transform: scale(1.05);
                }
            </style>
        </head>
        <body>
            <h2>Bu sayfaya erişmek için şifre girin:</h2>
            <form method="POST">
                <input type="password" name="sifre" placeholder="Şifre girin..." required>
                <br>
                <button type="submit">Giriş</button>
            </form>
        </body>
    </html>
    '''

@app.route('/Nurihemdem-Devleti')
def yetkili_sayfa():
    return render_template("Web89.html")

@app.route('/XD')
def fazladan_bir_sayfa():
    return render_template('Web55.html')

if __name__ == '__main__':
    app.run(debug=True)