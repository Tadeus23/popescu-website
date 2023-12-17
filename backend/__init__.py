from flask import Flask, render_template, Response, jsonify
import json
import os
from config import cv_data


def create_app():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, '../static')
    template_dir = os.path.join(base_dir, '../templates')

    app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

    def handle_missing_key(data, key, default=None):
        try:
            return data.get(key, default)
        except Exception as e:
            app.logger.error(f"Error handling key '{key}': {e}")
            return default

    def jsonify_with_unicode(data, indent=None):
        try:
            return Response(json.dumps(data, ensure_ascii=False, indent=indent), mimetype='application/json')
        except Exception as e:
            app.logger.error(f"JSON conversion error: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @app.route('/')
    def home():
        try:
            experiences = handle_missing_key(cv_data, "experience_data", [])
            educations = handle_missing_key(cv_data, "education_data", [])
            return render_template('index.html', experiences=experiences, educations=educations)
        except Exception as e:
            app.logger.error(f"Error in home route: {e}")
            return render_template('error.html'), 500

    @app.route('/personal', methods=['GET'])
    def get_personal_info():
        try:
            personal_info = handle_missing_key(cv_data, "personal_info", {})
            return jsonify_with_unicode(personal_info, indent=4)
        except Exception as e:
            app.logger.error(f"Error fetching personal info: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @app.route('/experience', methods=['GET'])
    def get_experience():
        try:
            experience_data = handle_missing_key(cv_data, "experience_data", [])
            return jsonify_with_unicode(experience_data, indent=4)
        except Exception as e:
            app.logger.error(f"Error fetching experience data: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @app.route('/education', methods=['GET'])
    def get_education():
        try:
            education_data = handle_missing_key(cv_data, "education_data", [])
            return jsonify_with_unicode(education_data, indent=4)
        except Exception as e:
            app.logger.error(f"Error fetching education data: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @app.route('/skills', methods=['GET'])
    def get_skills():
        try:
            skills_data = handle_missing_key(cv_data, "skills_data", [])
            return jsonify_with_unicode(skills_data, indent=4)
        except Exception as e:
            app.logger.error(f"Error fetching skills data: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    @app.route('/certifications', methods=['GET'])
    def get_certifications():
        try:
            certifications_data = handle_missing_key(cv_data, "certifications_data", [])
            return jsonify_with_unicode(certifications_data, indent=4)
        except Exception as e:
            app.logger.error(f"Error fetching certifications data: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

    return app
