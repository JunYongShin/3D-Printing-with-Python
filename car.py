from flask import Flask, jsonify, request, abort, make_response


app = Flask(__name__)



def diction(make,model,year,color,numseats,owner,odo,passenger,listrip):
    '''
    takes inputs either in string or integer or lists
    and return as a dictionary
    '''
    dict = {
        'make':make,
        'model':model,
        'year':year,
        'color':color,
        'number of seats': numseats,
        'owner':owner,
        'odo': odo,
        'passenger':passenger,
        'lists of trip':[listrip]
        
    }
    
    return dict


def prnt(f):
    a=f['make']
    b=f['model']
    c=f['year']
    d=f['color']
    e=f['number of seats']
    f1=f['owner']
    g=f['odo']
    h=f['passenger']
    i=f['lists of trip']
            
    line1= f'make: {a}, model: {b}, year: {c}, color: {d}, nuber of seats: {e}, owner: {f1}, odo: {g}, passenger: {h}, lists of trips: {i}'
    return line1
    


car=diction('Tesla','X','2019','Black','5','Me','1900',['A','B','C'],['USA','CAN'])



@app.route('/')
def index():
    
    return prnt(car)

@app.route('/car', methods=['GET'])
def get_tasks():
    return jsonify({"car":car})

@app.route('/car/<string:key>', methods=['GET'])
def get_taskByID(key):
    
    keyed = car[key]
    if len(keyed)==0:
        abort(404)
    return jsonify({'property' : keyed})


@app.route('/car/trips', methods=['GET'])
def get_trip():
    
    keyed = car['lists of trip']
    if len(keyed)==0:
        abort(404)
    return jsonify({'trips' : keyed})





@app.route('/car/trips', methods=['POST'])
def new_task():
    if (not request.json) or (not ('title' in request.json)):
        abort(400)
    trips= car['lists of trip']
    t = request.json["trip"]
    trips.append(t)
    return jsonify({'trips':t}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'That ID is invalid'}),404)

if __name__ == '__main__':
    app.run(debug=True)



