from flask import Flask, render_template, request, redirect, url_for
import os
from database import init_database, add_candidate, add_job, get_candidates, get_jobs
from agents.recruitment_agent import recruitment_agent
from tools.resume_parser import parse_resume

app = Flask(__name__)
init_database()
os.makedirs("resumes", exist_ok=True)
os.makedirs("hr_documents", exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html", candidates=get_candidates(), jobs=get_jobs())

@app.route("/upload-resume", methods=["POST"])
def upload_resume():
    file = request.files.get("resume")
    if not file:
        return "Please upload a resume."
    if not file.filename.lower().endswith(".pdf"):
        return "Only PDF resumes are supported."
    path = os.path.join("resumes", file.filename)
    file.save(path)
    parsed = parse_resume(path)
    analysis = recruitment_agent("resume", parsed["text"])
    return render_template("resume.html", analysis=analysis, email=parsed["email"], phone=parsed["phone"])

@app.route("/add-job", methods=["POST"])
def create_job():
    add_job(request.form.get("title"), request.form.get("description"),
            request.form.get("skills"), request.form.get("experience"))
    return redirect(url_for("index"))

@app.route("/match", methods=["POST"])
def match():
    result = recruitment_agent("match", {
        "resume": request.form.get("resume"),
        "job": request.form.get("job")
    })
    return render_template("matching.html", result=result)

@app.route("/interview-questions", methods=["POST"])
def interview_questions():
    questions = recruitment_agent("interview", {
        "job_title": request.form.get("job_title"),
        "skills": request.form.get("skills")
    })
    return render_template("interview.html", questions=questions)

@app.route("/candidates")
def candidates():
    return render_template("candidates.html", candidates=get_candidates())

@app.route("/dashboard")
def dashboard():
    candidates = get_candidates()
    return render_template(
        "dashboard.html",
        total=len(candidates),
        shortlisted=sum(c[7] == "Shortlisted" for c in candidates),
        review=sum(c[7] == "Review" for c in candidates),
        rejected=sum(c[7] == "Rejected" for c in candidates)
    )

if __name__ == "__main__":
    app.run(debug=True)
