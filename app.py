import os
import threading
from flask import Flask, render_template, request
from datetime import datetime
import json
from pprint import pprint
from core import CalendarClient


app = Flask(__name__)

cal = CalendarClient()


@app.route('/live')
def live():
    return dict(status='OK')


@app.route('/')
def test_handle():
    f = open('trans-config.json')
    data = json.load(f)
    gen = cal_generate(data)
    return render_template('index.html', transactions=gen)


# TODO: need refactor
def cal_generate(data):
    new_data = []
    cal_range = cal.rest_of_month()
    for date_obj in cal_range:
        for dat in data:
            if dat['repeated']['enable'] == True and cal.is_cron_date(dat['repeated']['period'], date_obj):
                new_data.append(
                    get_ops_data(dat, date_obj)
                )
            elif dat['repeated']['enable'] == False and cal.is_date(dat['repeated']['period'], date_obj):
                new_data.append(
                    get_ops_data(dat, date_obj)
                )

    return new_data


def get_ops_data(data, date: datetime = None):
    return dict(
        id=data['operation_id'],
        # harcode
        calendarId='1',
        title=f"{data['value']}, {data['currency']}",
        body=data['body'],
        # harcode
        category='time',
        start=date,
        end=date
    )


@app.route('/daily')
def daily_scalp():
    result_sum = 0
    f = open('trans-config.json')
    data = json.load(f)
    for op in data:
        if op['repeated']['enable'] == True:
            period = op['repeated']['period']
            if cal.is_today(period):
                result_sum += op['value']
            print(f'{period}\n')
            print(cal.is_today(period))

    return f'Сумма за сегодня {result_sum}'


if __name__ == '__main__':

    if os.environ.get('ENV') == 'o-dev':
        app.debug = True

    app.run(host='0.0.0.0', port=80)
