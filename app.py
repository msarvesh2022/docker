from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = '''
<!doctype html>
<title>Multiplication Table</title>
<h2>Enter a number to get its multiplication table:</h2>
<form method="post">
  <input type="number" name="number" required>
  <input type="submit" value="Get Table">
</form>
{% if table %}
  <h3>Multiplication Table for {{ number }}:</h3>
  <ul>
    {% for row in table %}
      <li>{{ row }}</li>
    {% endfor %}
  </ul>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def multiplication_table():
    table = None
    number = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
        except (ValueError, KeyError):
            table = ["Invalid input. Please enter a valid number."]
    return render_template_string(HTML_FORM, table=table, number=number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 
    