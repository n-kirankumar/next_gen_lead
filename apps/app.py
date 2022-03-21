from config.next_gen_lead_config import *
from models.dealer_model import *
from models.product_enquiry_model import *

@app.route('/sign_in', methods=['GET'])
def home():
    current_date = date.today()
    result = session.query(Dealer).filter(Dealer.userName == request.args.get("username"), Dealer.passWord == request.args.get("password")).all()
    if result:
        yesterday_date = current_date - timedelta(days = 2)
        result1 = session.query(Table22).filter(Table22.date == str(yesterday_date),Table22.Name == request.args.get("name")).all()
        result1 = [i.__dict__ for i in result1]
        return str(result1)

    else:
        return "invalid credentials"

app.run(debug=False)


# @app.route('/deete_record',methods = ['DELETE'])
# def delete_method():
#     try:
#         result = session.query()










@app.route('/post_data', methods = ['POST'])
def insert_data():
    json_1 = request.get_json(force=True)
    for index,item in enumerate(json_1):
        record = Dealer(Name = item ["name"],
                        Password = item["password"])

    session.addall ([record])
    session.commit()