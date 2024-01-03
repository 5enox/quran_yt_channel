'''
I came across a video in facebook shorts and decided to make this script to make an automated youtube channel for quran
should be both hard and fun and helpful, alhamdulilah
#############################
for now I'm planning on looking for an api or just scrape the quran off of a website i just found 
and use speec recognition to get which verse is been read at when and use moviepy to edit a nice UI ofr the video incha allah
then It's either youtube api or selenium to upload the final video, hope this will go as planned.
'''

# this is the code for the flask that will handle the bas64 file encryption

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_data", methods=["GET"])
def get_data():
    data = {"message": "This is a GET response!"}
    return jsonify(data)
  

@app.route("/upload_file", methods=["POST"])
def upload_file():
    if request.method == "POST":
        uploaded_file = request.files["file"]  # Access the uploaded file object
        if (a := uploaded_file.filename):  # Check for non-empty filename
            uploaded_file.save(f"uploads/{a}")
            return jsonify({"message": "File uploaded successfully!"})
        else:
            return jsonify({"message": "File Has No Name / non existence"})
    else:
            return jsonify({"error": "No file selected for upload"})


if __name__ == '__main__':
    app.run(debug=True)