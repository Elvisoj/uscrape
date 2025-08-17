from flask import Blueprint, jsonify
from app.extensions import db
from app.scrapper import run_post_scrapper


scrapper_bp = Blueprint('scrapper', __name__, url_prefix='/api')

@scrapper_bp.route('/scrape', methods=['POST'])
def trigger_scrapper():
    try:
        run_post_scrapper()
        return jsonify({"message": "Scraper started successfully!"}), 200
    except Exception as e:
        import traceback
        traceback.print_exc()  # logs full error in Render
        return jsonify({"error": str(e)}), 500