from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/<gurih>')
def hello_world(gurih):
    return gurih

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/crot', methods=['POST'])
def login():
	return request.form['anu']


@app.route("/input/nama")
def nama():
    nama = [
        {
            'nama_depan':'ema',
            'nama_belakang':'ainun'
        },
        {
            'nama_depan':'riandaka',
            'nama_belakang':'rizal'
        },
        {
            'nama_depan':'naufal',
            'nama_belakang':'ramadhan'
        }
    ]
    return jsonify({'daftar nama':nama})
