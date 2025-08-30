from flask import Flask, request
from pyngrok import ngrok

app = Flask(__name__)

public_url = ngrok.connect(5000)
print("公開url:", public_url)

@app.route('/', methods=['GET', 'POST'])
def greet():
  if request.method == 'POST':
    name = request.form.get('name', '名無し')
    return f"<h2>こんにちは{name}さん！</h2><a href='/'戻る</a>"
  return '''
    <form method='POST'>
      お名前: <input type='text' name='name'>
      <input type='submit' value='挨拶'>
    </form>
  '''

app.run(port=5000)