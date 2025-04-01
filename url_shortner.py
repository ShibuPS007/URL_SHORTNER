from flask import Flask, request,redirect,jsonify,render_template
import mysql.connector
import hashlib
import base64

app=Flask(__name__)


DB_CONFIG={
    'host':'localhost',
    'user':'root',
    'password':'Idly2004',
    'database':'url_shortner'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def generate_short_url(long_url):
    hash_object=hashlib.sha256(long_url.encode())
    short_hash=base64.urlsafe_b64encode(hash_object.digest())[:6].decode()

    return short_hash

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten',methods=['POST'])
def shorten_url():
    long_url=request.form.get('long_url')
    if not long_url:
        return "Invalid URL", 400
    
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT short_url FROM url_mapping WHERE long_url=%s", (long_url,))
    existing_entry=cursor.fetchone()
    if existing_entry:
        conn.close()
        return f"Shortened URL: <a href='https://de/{existing_entry['short_url']}' target='_blank'>https://de/{existing_entry['short_url']}</a>"
   
    short_url=generate_short_url(long_url)
    cursor.execute("INSERT INTO url_mapping (long_url,short_url) VALUES (%s,%s)",(long_url,short_url))

    conn.commit()
    conn.close()

    return f"Shortened URL: <a href='https://de/{short_url}' target='_blank'>https://de/{short_url}</a>"
@app.route('/<short_url>',methods=['GET'])
def redirect_url(short_url):
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)

    cursor.execute("SELECT long_url FROM url_mapping WHERE short_url =%s",(short_url,))
    entry=cursor.fetchone()
    if entry:
        cursor.execute("UPDATE url_mapping SET clicks = clicks + 1 WHERE short_url = %s", (short_url,))

        conn.commit()
        conn.close()
        return redirect(entry['long_url'])
    
    conn.close()
    return "ERROR : URL not found",404




if __name__ == '__main__':
    app.run(debug=True)  # Starts the Flask server in debug mode
