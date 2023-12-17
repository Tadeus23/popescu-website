import click
from config import cv_data
import json


def setup_cli_commands(app):
    @app.cli.command("get-cv")
    def print_cv_data():
        try:
            response = {
                "Personal Info": cv_data.get("personal_info", {}),
                "Experience": cv_data.get("experience_data", []),
                "Education": cv_data.get("education_data", []),
                "Skills": cv_data.get("skills_data", []),
                "Certifications": cv_data.get("certifications_data", [])
            }
            click.echo(json.dumps(response, indent=4))
        except Exception as e:
            click.echo(f"Error occurred: {e}")

    @app.cli.command("add-skill")
    @click.option("--skill", prompt="Enter new skill name", help="New skill name")
    @click.option("--years-exp", prompt="Enter years of experience", help="Years of experience")
    def add_skill_cli(skill, years_exp):
        try:
            new_skill = {"skill": skill, "years_exp": years_exp}
            skills_data = cv_data.setdefault("skills_data", [])
            skills_data.append(new_skill)
            click.echo("Skill added successfully:")
            click.echo(json.dumps(new_skill, indent=2))
        except Exception as e:
            click.echo(f"Error occurred while adding skill: {e}")

    @app.cli.command("delete-skill")
    @click.argument("index", type=int)
    def delete_skill_cli(index):
        try:
            skills_data = cv_data.get("skills_data", [])
            if 0 <= index < len(skills_data):
                deleted_skill = skills_data.pop(index)
                click.echo(f"Skill at index {index} deleted successfully:")
                click.echo(json.dumps(deleted_skill, indent=2))
            else:
                click.echo("Invalid index.")
        except Exception as e:
            click.echo(f"Error occurred while deleting skill: {e}")

    @app.cli.command("update-skill")
    @click.argument("index", type=int)
    @click.option("--skill", prompt="Enter updated skill name", help="Updated skill name")
    @click.option("--years-exp", prompt="Enter updated years of experience", help="Updated years of experience")
    def update_skill_cli(index, skill, years_exp):
        try:
            skills_data = cv_data.get("skills_data", [])
            if 0 <= index < len(skills_data):
                updated_skill = {"skill": skill, "years_exp": years_exp}
                skills_data[index].update(updated_skill)
                click.echo(f"Skill at index {index} updated successfully:")
                click.echo(json.dumps(skills_data[index], indent=2))
            else:
                click.echo("Invalid index.")
        except Exception as e:
            click.echo(f"Error occurred while updating skill: {e}")

    return setup_cli_commands
