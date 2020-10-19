
from flask import Flask, render_template
from sensor_info import return_current_time, return_current_date, return_current_temp

app = Flask(__name__)
sensor_id = 'id0101'

current_time = return_current_time()
current_date = return_current_date()
current_temp = return_current_temp(sensor_id)

print(current_time)

# TODO header instruction needed set cache to 0
@app.route('/')
def environment_dashboard():
    return render_template('homepage.html', date=current_date, time=current_time, temp=current_temp)


if __name__ == "__main__":
    app.run(port=3639, debug=True)