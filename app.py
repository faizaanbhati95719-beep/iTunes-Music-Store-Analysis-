from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    # check_same_thread=False is needed for SQLite + Flask
    conn = sqlite3.connect('itunes_analysis.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    try:
        conn = get_db_connection()
        
        # 1. Get the actual list (Top 500 for performance)
        query = "SELECT artist_id, name FROM artist ORDER BY name ASC LIMIT 500"
        data = conn.execute(query).fetchall()
        
        # 2. Get the absolute total count in the DB
        total_query = "SELECT COUNT(*) as total FROM artist"
        total_count = conn.execute(total_query).fetchone()['total']
        
        conn.close()
        
        return jsonify({
            "artists": [dict(row) for row in data],
            "db_total": total_count
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/api/artist-details/<int:artist_id>')
def artist_details(artist_id):
    conn = None
    try:
        conn = get_db_connection()
        
        # 1. Fetch Albums
        album_query = "SELECT * FROM album WHERE artist_id = ?"
        albums_raw = conn.execute(album_query, (artist_id,)).fetchall()
        
        # 2. Fetch Track Count using a JOIN (More reliable)
        track_query = """
            SELECT COUNT(*) as count 
            FROM track 
            JOIN album ON track.album_id = album.album_id 
            WHERE album.artist_id = ?
        """
        tracks_raw = conn.execute(track_query, (artist_id,)).fetchone()
        
        # Handle potential case sensitivity in column names (title vs Title)
        album_list = []
        for row in albums_raw:
            # Keys in sqlite3.Row are accessible via row.keys()
            cols = row.keys()
            if 'title' in cols:
                album_list.append(row['title'])
            elif 'Title' in cols:
                album_list.append(row['Title'])

        return jsonify({
            "albums": album_list,
            "track_count": tracks_raw['count'] if tracks_raw else 0
        })

    except Exception as e:
        print(f"!!! DATABASE ERROR for ID {artist_id}: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)